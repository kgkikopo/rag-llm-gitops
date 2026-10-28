import os
import json
import logging
import urllib.parse
import yaml
import requests
import psycopg
from pgvector.psycopg import register_vector
import gradio as gr

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("rag-ui")

# --- Configuration ---
APP_TITLE = os.environ.get("APP_TITLE", "OpenShift 4.22 Documentation Assistant")
EMBEDDING_MODEL_NAME = os.environ.get("EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-0.6B")
COLLECTION_NAME = os.environ.get("PGVECTOR_COLLECTION_NAME", "docs")
CONFIG_FILE = os.environ.get("CONFIG_FILE", "/opt/app-root/config/config.yaml")

# Database parameters
DB_HOST = os.environ.get("DB_HOST", "pgvector-postgresql")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "vectordb")
DB_USER = os.environ.get("DB_USERNAME", os.environ.get("DB_USER", "postgres"))
DB_PASS = os.environ.get("DB_PASS", os.environ.get("DB_PASSWORD", "postgres"))
PGVECTOR_URL = os.environ.get("PGVECTOR_URL", "")

# Parse PGVECTOR_URL if provided
if PGVECTOR_URL:
    try:
        clean_url = PGVECTOR_URL.replace("postgresql+psycopg://", "postgresql://")
        parsed = urllib.parse.urlparse(clean_url)
        if parsed.hostname:
            DB_HOST = parsed.hostname
        if parsed.port:
            DB_PORT = str(parsed.port)
        if parsed.username:
            DB_USER = parsed.username
        if parsed.password:
            DB_PASS = parsed.password
        if parsed.path and len(parsed.path) > 1:
            DB_NAME = parsed.path.lstrip("/")
    except Exception as e:
        logger.warning(f"Could not parse PGVECTOR_URL ({e}), using individual env vars.")

# LLM parameters
VLLM_URL = os.environ.get("VLLM_URL", "http://vllm-inference-service-predictor:8080/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "google/gemma-3-4b-it")
TEMPERATURE = float(os.environ.get("TEMPERATURE", "1.0"))
TOP_P = float(os.environ.get("TOP_P", "0.95"))
TOP_K = int(os.environ.get("TOP_K", "64"))
MAX_TOKENS = int(os.environ.get("MAX_TOKENS", "2048"))

if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, "r") as f:
            cfg = yaml.safe_load(f)
            if cfg and "llm_providers" in cfg:
                for prov in cfg["llm_providers"]:
                    if prov.get("enabled", True) and "models" in prov:
                        for m in prov["models"]:
                            if m.get("enabled", True):
                                if "url" in m and m["url"]:
                                    VLLM_URL = m["url"]
                                if "name" in m and m["name"]:
                                    MODEL_NAME = m["name"]
                                for p in m.get("params", []):
                                    if p.get("name") == "temperature":
                                        TEMPERATURE = float(p.get("value", 1.0))
                                    elif p.get("name") == "top_p":
                                        TOP_P = float(p.get("value", 0.95))
                                    elif p.get("name") == "top_k":
                                        TOP_K = int(p.get("value", 64))
                                    elif p.get("name") == "max_new_tokens":
                                        MAX_TOKENS = int(p.get("value", 4096))
                                break
            if cfg and "default_model" in cfg and cfg["default_model"]:
                default_m = cfg["default_model"]
                # Prefer short name without org prefix (e.g. gemma-3-4b-it) to match vLLM served model
                MODEL_NAME = default_m.split("/")[-1] if "/" in default_m else default_m
        logger.info(f"Loaded config from {CONFIG_FILE}: URL={VLLM_URL}, Model={MODEL_NAME}")
    except Exception as e:
        logger.warning(f"Failed to parse {CONFIG_FILE} ({e}), using default LLM settings.")

# --- Lazy Embeddings Model ---
_embed_model = None

def get_embed_model():
    global _embed_model
    if _embed_model is None:
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL_NAME} on CPU...")
        from sentence_transformers import SentenceTransformer
        _embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME, device="cpu")
        logger.info("Embedding model loaded successfully.")
    return _embed_model

def get_db_connection():
    conn = psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        autocommit=True
    )
    register_vector(conn)
    return conn

# --- Retrieval Function ---
def retrieve_docs(query: str, top_k: int = 4):
    """Embeds query and queries PGVector for top matching documentation snippets."""
    try:
        model = get_embed_model()
        try:
            query_embedding = model.encode(query, prompt_name="query").tolist()
        except Exception:
            query_embedding = model.encode(query).tolist()

        with get_db_connection() as conn:
            with conn.cursor() as cur:
                # Check for langchain-postgres v2 direct table (e.g. "docs")
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = %s
                    );
                """, (COLLECTION_NAME,))
                if cur.fetchone()[0]:
                    sql = f"""
                        SELECT content, langchain_metadata, (embedding <=> %s::vector) AS distance
                        FROM "{COLLECTION_NAME}"
                        ORDER BY distance ASC
                        LIMIT %s;
                    """
                    cur.execute(sql, (query_embedding, top_k))
                    rows = cur.fetchall()
                else:
                    # Check legacy langchain_pg_collection schema
                    cur.execute("""
                        SELECT EXISTS (
                            SELECT FROM information_schema.tables 
                            WHERE table_name = 'langchain_pg_collection'
                        );
                    """)
                    if not cur.fetchone()[0]:
                        return [], f"Database table '{COLLECTION_NAME}' not yet created. The documentation ingestion job may still be running."

                    sql = """
                        SELECT e.document, e.cmetadata, (e.embedding <=> %s::vector) AS distance
                        FROM langchain_pg_embedding e
                        JOIN langchain_pg_collection c ON e.collection_id = c.uuid
                        WHERE c.name = %s
                        ORDER BY distance ASC
                        LIMIT %s;
                    """
                    cur.execute(sql, (query_embedding, COLLECTION_NAME, top_k))
                    rows = cur.fetchall()

                docs = []
                for doc_text, metadata, dist in rows:
                    source = "Unknown"
                    if isinstance(metadata, dict):
                        source = metadata.get("source", metadata.get("title", "OpenShift 4.22 Docs"))
                    elif isinstance(metadata, str):
                        try:
                            m_dict = json.loads(metadata)
                            source = m_dict.get("source", m_dict.get("title", "OpenShift 4.22 Docs"))
                        except Exception:
                            source = metadata
                    docs.append({
                        "content": doc_text,
                        "source": source,
                        "distance": float(dist)
                    })
                return docs, None
    except Exception as e:
        logger.error(f"Error querying PGVector: {e}")
        return [], str(e)

# --- LLM Invocation ---
def find_working_vllm_url() -> str:
    global VLLM_URL
    candidates = [
        "http://vllm-inference-service-predictor:8080/v1",
        "http://vllm-inference-service-predictor.rag-llm.svc.cluster.local:8080/v1",
        "http://vllm-inference-service-predictor:80/v1",
        VLLM_URL
    ]
    seen = set()
    for u in candidates:
        if u and u not in seen:
            seen.add(u)
            try:
                r = requests.get(f"{u.rstrip('/')}/models", timeout=2, verify=False)
                if r.status_code == 200:
                    logger.info(f"Verified working vLLM endpoint: {u}")
                    VLLM_URL = u
                    return u
            except Exception:
                continue
    return VLLM_URL

def get_active_model_name() -> str:
    global MODEL_NAME
    base_url = find_working_vllm_url()
    try:
        r = requests.get(f"{base_url.rstrip('/')}/models", timeout=3, verify=False)
        if r.status_code == 200:
            data = r.json().get("data", [])
            if data and "id" in data[0]:
                MODEL_NAME = data[0]["id"]
                return MODEL_NAME
    except Exception:
        pass
    if "/" in MODEL_NAME:
        return MODEL_NAME.split("/")[-1]
    return MODEL_NAME

DEFAULT_SYSTEM_PROMPT = (
    "You are an OpenShift Container Platform 4.22 documentation assistant. "
    "Your purpose is to provide accurate, production-ready technical assistance based on official OpenShift 4.22 specifications. "
    "Provide exact CLI commands (`oc ...`) and complete, valid YAML manifests where applicable. "
    "When documentation tool results are provided, ground your answer strictly in that context. "
    "For general greetings and casual remarks, respond politely and concisely without searching documentation."
)

def call_llm(messages: list[dict], max_tokens: int = MAX_TOKENS) -> str:
    """Calls vLLM OpenAI-compatible chat completions endpoint (synchronous)."""
    target_url = find_working_vllm_url()
    url = f"{target_url.rstrip('/')}/chat/completions"
    active_model = get_active_model_name()
    payload = {
        "model": active_model,
        "messages": messages,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": max_tokens
    }
    try:
        resp = requests.post(url, json=payload, timeout=180, verify=False)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.ConnectionError:
        fallback = "http://vllm-inference-service-predictor:8080/v1/chat/completions"
        if url != fallback:
            try:
                resp = requests.post(fallback, json=payload, timeout=180)
                resp.raise_for_status()
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            except Exception:
                pass
        return f"[Connection Error] Unable to connect to inference service at {url}."
    except Exception as e:
        alt_model = MODEL_NAME if active_model != MODEL_NAME else active_model.split("/")[-1]
        if alt_model != active_model:
            try:
                payload["model"] = alt_model
                resp = requests.post(url, json=payload, timeout=120, verify=False)
                resp.raise_for_status()
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            except Exception:
                pass
        return f"[Error] LLM request failed: {e}"

def call_llm_stream(messages: list[dict], max_tokens: int = MAX_TOKENS):
    """Streams completions from vLLM using Server-Sent Events (SSE)."""
    target_url = find_working_vllm_url()
    url = f"{target_url.rstrip('/')}/chat/completions"
    active_model = get_active_model_name()
    payload = {
        "model": active_model,
        "messages": messages,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": max_tokens,
        "stream": True
    }
    try:
        resp = requests.post(url, json=payload, stream=True, timeout=180, verify=False)
        resp.raise_for_status()
        for line in resp.iter_lines():
            if line:
                decoded = line.decode("utf-8").strip()
                if decoded.startswith("data: "):
                    data_str = decoded[6:]
                    if data_str == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data_str)
                        choices = chunk.get("choices", [])
                        if choices:
                            delta = choices[0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                yield content
                    except Exception:
                        continue
    except requests.exceptions.ConnectionError:
        fallback = "http://vllm-inference-service-predictor:8080/v1/chat/completions"
        if url != fallback:
            try:
                resp = requests.post(fallback, json=payload, stream=True, timeout=180)
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if line:
                        decoded = line.decode("utf-8").strip()
                        if decoded.startswith("data: "):
                            data_str = decoded[6:]
                            if data_str == "[DONE]":
                                break
                            try:
                                chunk = json.loads(data_str)
                                choices = chunk.get("choices", [])
                                if choices:
                                    delta = choices[0].get("delta", {})
                                    content = delta.get("content", "")
                                    if content:
                                        yield content
                            except Exception:
                                continue
                return
            except Exception:
                pass
        yield f"\n\n[Connection Error] Unable to connect to inference service at {url}."
    except Exception as e:
        yield f"\n\n[Error] LLM streaming failed: {e}"

def is_casual_greeting(msg: str) -> bool:
    """Detects simple conversational pleasantries that do not require tool retrieval."""
    clean = msg.strip().lower().rstrip("!.,?")
    greetings = {
        "hi", "hello", "hey", "good morning", "good afternoon", "good evening",
        "howdy", "sup", "thanks", "thank you", "thx", "bye", "goodbye", "who are you"
    }
    return clean in greetings

# --- Chat Assistant Logic ---
def chat_respond(user_message: str, chat_history: list):
    history = list(chat_history) if chat_history else []
    if not user_message or not user_message.strip():
        yield "", history
        return

    # 1. Immediately append user turn and placeholder assistant turn
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": "..."})
    yield "", history

    # Build conversation context with static system prompt
    messages = [{"role": "system", "content": DEFAULT_SYSTEM_PROMPT}]
    # Add previous dialogue history (up to last 6 turns)
    for item in history[:-2][-6:]:
        if isinstance(item, dict):
            role = item.get("role", "user")
            content = item.get("content", "")
            if role == "assistant" and "</details>" in content:
                # Strip tool card HTML from prior turns so LLM context remains clean text
                content = content.split("</details>", 1)[-1].strip()
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})

    # 2. Check if query is a greeting
    if is_casual_greeting(user_message):
        messages.append({"role": "user", "content": user_message})
        accumulated = ""
        for chunk in call_llm_stream(messages, max_tokens=256):
            accumulated += chunk
            history[-1] = {"role": "assistant", "content": accumulated}
            yield "", history
        return

    # 3. Technical question: execute tool call to search OpenShift 4.22 documentation
    tool_banner = (
        f'<details open style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 12px; margin-bottom: 12px; font-family: system-ui, -apple-system, sans-serif;">\n'
        f'<summary style="cursor: pointer; font-weight: 600; color: #0284c7;">⚙️ <b>Tool Call</b>: <code>search_openshift_docs(query="{user_message}")</code></summary>\n'
        f'<div style="margin-top: 6px; font-size: 13px; color: #64748b;">Searching PGVector for matching OpenShift 4.22 documentation chunks...</div>\n'
        f'</details>'
    )
    history[-1] = {"role": "assistant", "content": tool_banner}
    yield "", history

    docs, error_msg = retrieve_docs(user_message, top_k=4)

    if docs:
        snippets_html = []
        context_blocks = []
        sources = set()
        for idx, doc in enumerate(docs, 1):
            src = doc.get("source", "Unknown")
            sources.add(src)
            content_snippet = doc.get("content", "")
            preview = content_snippet[:220].replace("<", "&lt;").replace(">", "&gt;") + "..."
            dist = doc.get("distance", 0.0)
            score = max(0.0, 1.0 - dist)

            snippets_html.append(
                f'<div style="margin-top: 6px; padding: 6px 10px; background: #ffffff; border-radius: 4px; border-left: 3px solid #0284c7;">'
                f'<div style="font-weight: 600; font-size: 12px; color: #0f172a;">[{idx}] {src} <span style="font-weight: normal; color: #64748b;">(Score: {score:.2f})</span></div>'
                f'<div style="font-size: 12px; color: #475569; margin-top: 2px;">{preview}</div>'
                f'</div>'
            )
            context_blocks.append(f"--- Document Snippet [{idx}] (Source: {src}) ---\n{content_snippet}")

        tool_card = (
            f'<details style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 8px 12px; margin-bottom: 12px; font-family: system-ui, -apple-system, sans-serif;">\n'
            f'<summary style="cursor: pointer; font-weight: 600; color: #0284c7;">🔧 <b>Tool Result</b>: <code>search_openshift_docs</code> &mdash; {len(docs)} OpenShift 4.22 documentation snippets retrieved</summary>\n'
            f'<div style="margin-top: 8px;">\n'
            f"{''.join(snippets_html)}\n"
            f'</div>\n'
            f'</details>'
        )

        context_str = "\n\n".join(context_blocks)
        augmented_prompt = (
            f"[Official OpenShift 4.22 Documentation Tool Output]:\n{context_str}\n\n"
            f"User Question: {user_message}"
        )
        messages.append({"role": "user", "content": augmented_prompt})

        # 4. Stream response from vLLM
        full_response = tool_card + "\n\n"
        for chunk in call_llm_stream(messages):
            full_response += chunk
            history[-1] = {"role": "assistant", "content": full_response}
            yield "", history

        # Append source references at end
        sources_list = "\n".join([f"- `{s}`" for s in sorted(sources)])
        final_answer = f"{full_response}\n\n---\n**Referenced Documentation Sources:**\n{sources_list}"
        history[-1] = {"role": "assistant", "content": final_answer}
        yield "", history

    else:
        # Fallback if no documents found or error occurred
        tool_card = (
            f'<details style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 8px 12px; margin-bottom: 12px; font-family: system-ui, -apple-system, sans-serif;">\n'
            f'<summary style="cursor: pointer; font-weight: 600; color: #c2410c;">⚠️ <b>Tool Result</b>: <code>search_openshift_docs</code> &mdash; No documents found ({error_msg or "Empty collection"})</summary>\n'
            f'</details>'
        )
        messages.append({"role": "user", "content": user_message})
        full_response = tool_card + "\n\n"
        for chunk in call_llm_stream(messages):
            full_response += chunk
            history[-1] = {"role": "assistant", "content": full_response}
            yield "", history

# --- Comparison Logic ---
def compare_query(query: str):
    if not query.strip():
        return "Please enter a question to compare.", "Please enter a question to compare."

    # 1. Base Model Call (Zero context injection)
    base_messages = [
        {"role": "system", "content": "You are a helpful cloud and Kubernetes engineer. Answer the following question accurately."},
        {"role": "user", "content": query}
    ]
    base_output = call_llm(base_messages)

    # 2. RAG Model Call (With OpenShift 4.22 retrieval)
    docs, error_msg = retrieve_docs(query, top_k=4)
    if docs:
        context_blocks = []
        sources = set()
        for idx, doc in enumerate(docs, 1):
            context_blocks.append(f"[{idx}] {doc['content']}")
            sources.add(doc['source'])
        context_str = "\n\n".join(context_blocks)
        rag_messages = [
            {
                "role": "system",
                "content": (
                    "You are an OpenShift 4.22 documentation assistant. "
                    "Use the following official OpenShift 4.22 documentation to answer the user's question accurately. "
                    "Provide exact OpenShift commands (`oc ...`) and native OpenShift resources (e.g. Routes, SCCs, ImageStreams).\n\n"
                    f"Context:\n{context_str}"
                )
            },
            {"role": "user", "content": query}
        ]
        rag_body = call_llm(rag_messages)
        sources_list = "\n".join([f"- `{s}`" for s in sorted(sources)])
        rag_output = f"{rag_body}\n\n---\n**Retrieved Sources (OpenShift 4.22 Docs):**\n{sources_list}"
    else:
        rag_output = f"Retrieval returned no documents. ({error_msg or 'Empty collection'})\n\nDirect answer:\n" + call_llm([
            {"role": "system", "content": "You are an OpenShift 4.22 documentation assistant."},
            {"role": "user", "content": query}
        ])

    return base_output, rag_output

# --- Status Check ---
def check_status():
    status = []
    # Test DB
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                # Check for direct collection table (langchain-postgres v2)
                cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s);", (COLLECTION_NAME,))
                if cur.fetchone()[0]:
                    cur.execute(f'SELECT count(*) FROM "{COLLECTION_NAME}";')
                    count = cur.fetchone()[0]
                    status.append(f"PGVector Database: Connected (Host: {DB_HOST}, Port: {DB_PORT}, DB: {DB_NAME})")
                    status.append(f"Indexed Documentation Chunks in '{COLLECTION_NAME}': {count}")
                else:
                    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'langchain_pg_embedding');")
                    if cur.fetchone()[0]:
                        cur.execute("SELECT count(*) FROM langchain_pg_embedding;")
                        count = cur.fetchone()[0]
                        status.append(f"PGVector Database: Connected (Host: {DB_HOST}, Port: {DB_PORT}, DB: {DB_NAME})")
                        status.append(f"Indexed Documentation Chunks: {count}")
                    else:
                        status.append(f"PGVector Database: Connected, but table '{COLLECTION_NAME}' not yet created (ingestion in progress).")
    except Exception as e:
        status.append(f"PGVector Database: Error ({e})")

    # Test LLM
    try:
        r = requests.get(f"{VLLM_URL.rstrip('/')}/models", timeout=5)
        if r.status_code == 200:
            status.append(f"vLLM Inference Service: Available (URL: {VLLM_URL}, Model: {MODEL_NAME})")
        else:
            status.append(f"vLLM Inference Service: HTTP {r.status_code} at {VLLM_URL}")
    except Exception as e:
        status.append(f"vLLM Inference Service: Unreachable at {VLLM_URL} ({e})")

    status.append(f"Embedding Model: {EMBEDDING_MODEL_NAME}")
    return "\n".join(status)

# --- Gradio Application UI ---
custom_css = """
footer {visibility: hidden}
.output-box { min-height: 350px; font-family: monospace; font-size: 14px; }
"""

with gr.Blocks(title=APP_TITLE, css=custom_css) as demo:
    gr.Markdown(f"# {APP_TITLE}")
    gr.Markdown("Interactive OpenShift Container Platform 4.22 assistant demonstrating Retrieval-Augmented Generation (RAG).")

    with gr.Tabs():
        with gr.TabItem("Documentation Assistant"):
            chatbot = gr.Chatbot(height=520, show_label=False)
            with gr.Row():
                msg_input = gr.Textbox(
                    placeholder="Ask a question about OpenShift 4.22 (e.g., How do I configure edge TLS termination for a route?)...",
                    show_label=False,
                    scale=9
                )
                send_btn = gr.Button("Send", variant="primary", scale=1)
            clear_btn = gr.Button("Clear Conversation")

            send_btn.click(chat_respond, inputs=[msg_input, chatbot], outputs=[msg_input, chatbot])
            msg_input.submit(chat_respond, inputs=[msg_input, chatbot], outputs=[msg_input, chatbot])
            clear_btn.click(lambda: [], None, chatbot)

        with gr.TabItem("Base vs. RAG Comparison"):
            gr.Markdown("### Compare Standard Base Model Output vs. RAG-Augmented Output")
            gr.Markdown("Test a query simultaneously on the base LLM (no documentation) and the RAG assistant (grounded in OpenShift 4.22 docs):")

            compare_input = gr.Textbox(
                label="Prompt / Task",
                placeholder="Enter an OpenShift question or select an example below...",
                lines=2
            )

            gr.Examples(
                examples=[
                    ["How do I expose my web application service frontend-svc on port 8080 with edge TLS termination?"],
                    ["How do I allow a pod running under service account deploy-sa to access host path mounts or run privileged?"],
                    ["How do I track and deploy container image updates automatically in a namespace?"],
                    ["What is the default storage class and how do I mount an existing PVC in my deployment?"]
                ],
                inputs=compare_input
            )

            compare_btn = gr.Button("Run Comparison", variant="primary")

            with gr.Row():
                with gr.Column():
                    gr.Markdown("#### Base Model (Without Retrieval)")
                    base_output = gr.Markdown(elem_classes=["output-box"])
                with gr.Column():
                    gr.Markdown("#### RAG Assistant (With OpenShift 4.22 Docs)")
                    rag_output = gr.Markdown(elem_classes=["output-box"])

            compare_btn.click(compare_query, inputs=compare_input, outputs=[base_output, rag_output])

        with gr.TabItem("System Status"):
            gr.Markdown("### Cluster Backend & Index Status")
            status_box = gr.Textbox(label="Status", lines=8, interactive=False)
            refresh_btn = gr.Button("Refresh Status")
            refresh_btn.click(check_status, None, status_box)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
