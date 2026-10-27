# OpenShift 4.22 Documentation Assistant with LLM and RAG

## Introduction

This repository provides a GitOps deployment using the [**Validated Patterns**](https://validatedpatterns.io/) framework for an **OpenShift 4.22 Documentation Assistant**. It deploys a Large Language Model (LLM) augmented with Retrieval-Augmented Generation (RAG) using documentation from OpenShift Container Platform (OCP) 4.22.

The application includes an interface to compare responses generated directly by the base model with responses augmented by retrieved documentation.

### Components

- **Documentation Ingestion**: Ingests documentation from the `enterprise-4.22` branch of [`openshift/openshift-docs`](https://github.com/openshift/openshift-docs).
- **Model Stack**:
  - **LLM**: `google/gemma-3-4b-it` served via vLLM in 16-bit precision (`--dtype=half`).
  - **Embeddings**: `Qwen/Qwen3-Embedding-0.6B`.
  - **Vector Database**: `PGVECTOR` (PostgreSQL with `pgvector` extension).
- **Comparison Interface**: Allows testing queries side-by-side to observe base model output versus retrieval-augmented output.
- **GitOps Management**: Provisioned and reconciled through OpenShift GitOps (Argo CD) and Helm.

---

## Architecture & Resource Usage

```
+-----------------------------------------------------------------------------------------+
|                                    OpenShift Cluster                                    |
|                                                                                         |
|  +--------------------+        +---------------------+        +----------------------+  |
|  | OpenShift GitOps   | -----> | vLLM Serving        | -----> | NVIDIA GPU Node      |  |
|  | (Argo CD & Helm)   |        | google/gemma-3-4b-it|        | (16GB VRAM, e.g. T4) |  |
|  +--------------------+        | 16-bit, 64k context |        | Usage: ~11.3 GB      |  |
|            |                   +---------------------+        +----------------------+  |
|            v                              ^                              ^              |
|            |                              |                              |              |
|  +--------------------+        +---------------------+                   |              |
|  | Documentation UI   | -----> | RAG Assistant Engine|                   |              |
|  | - Chat Interface   |        | (LangChain / Gradio)|                   |              |
|  | - Comparison Tab   |        +---------------------+                   |              |
|  +--------------------+                   |                              |              |
|                                           v                              |              |
|                                +---------------------+                   |              |
|                                | PGVector Database   |                   |              |
|                                | (PostgreSQL 16)     |                   |              |
|                                +---------------------+                   |              |
|                                           ^                              |              |
|                                           | Ingestion                    |              |
|                                +---------------------+                   |              |
|                                | populate-vectordb   |                   |              |
|                                | - Qwen3-Embedding   | ------------------+              |
|                                | - OCP 4.22 Git Docs |                                  |
|                                +---------------------+                                  |
+-----------------------------------------------------------------------------------------+
```

### GPU Memory Allocation (16-Bit Precision, 64k Context)

Gemma-3-4B uses a hybrid sliding window attention mechanism (local layers at 1,024 tokens, global full-attention layers):
- **Model Weights (FP16)**: ~8.6 GB
- **CUDA Overhead & Activations**: ~1.2 GB
- **KV Cache (64k context)**: ~1.46 GB
- **Estimated GPU Memory**: **~11.3 GB**, running on a 16 GB GPU instance (such as AWS `g4dn.xlarge` / NVIDIA T4).

---

## Repository Structure

1. **`charts/all/vllm-inference-service`**: Deploys `google/gemma-3-4b-it` using vLLM on a GPU-enabled node.
2. **`charts/all/rag-llm`**:
   - **`pgvector`**: PostgreSQL deployment with the `pgvector` extension.
   - **`populate-vectordb` Job**: Clones `openshift/openshift-docs` (`enterprise-4.22`), chunks markdown/adoc sources (chunk size: 2048, overlap: 200), computes embeddings, and stores them in PostgreSQL.
   - **`llm-ui`**: Gradio-based web interface with chat and comparison modes.

---

## Deployment & Configuration

### 1. Prerequisites
- Red Hat OpenShift Container Platform cluster.
- At least one GPU node provisioned with NVIDIA GPU Operator and Node Feature Discovery.
- A Hugging Face account with access to [google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) and a [Hugging Face User Access Token](https://huggingface.co/settings/tokens).
- A fork of this repository (`rag-llm-gitops`).

### 2. Configure Secrets
On your bastion or management host:

1. Copy the secret template:
   ```sh
   cp values-secret.yaml.template ~/values-secret-rag-llm-gitops.yaml
   ```
2. Populate the Hugging Face token and PostgreSQL credentials:
   ```yaml
   secrets:
     - name: hfmodel
       vaultPrefixes:
       - hub
       fields:
       - name: hftoken
         value: "hf_xxxxxxxxxxxxxxxxxxxxxx" # Hugging Face Read Token
     - name: pgvector
       vaultPrefixes:
       - hub
       fields:
       - name: username
         value: "postgres"
       - name: password
         value: "postgres"
       - name: databasename
         value: "vectordb"
   ```
3. Load the secrets into Vault:
   ```sh
   ./pattern.sh make load-secrets
   ```

### 3. Deploy the Pattern
Install the pattern:
```sh
./pattern.sh make install
```
Argo CD will synchronize the components, deploy PGVector, execute the documentation population job, initialize the vLLM service, and start the UI.

---

## Example Queries and Comparison

The following queries can be tested in the UI to compare responses from the base model against the RAG-augmented model:

| Query / Topic | Base Model (Without RAG) | RAG Assistant (With OpenShift 4.22 Docs) |
| :--- | :--- | :--- |
| **Edge Route Configuration**<br>*"How do I expose my web application service frontend-svc on port 8080 with edge TLS termination?"* | Typically generates standard Kubernetes `Ingress` manifests with ingress controller annotations. | Provides the native OpenShift `Route` resource (`kind: Route`, `spec.tls.termination: edge`) or the corresponding `oc create route edge` command. |
| **Security Context Constraints**<br>*"How do I allow a pod running under service account deploy-sa to access host path mounts or run privileged?"* | Typically suggests Kubernetes `PodSecurityPolicy` or container securityContext fields without cluster-level SCC authorization. | References OpenShift Security Context Constraints (SCC) and the `oc adm policy add-scc-to-user privileged -z deploy-sa` command. |
| **Container Images**<br>*"How do I track and deploy container image updates automatically in a namespace?"* | References external image polling tools or fixed image tags in Deployments. | References OpenShift `ImageStream` resources, `oc import-image`, and image triggers. |
| **Storage**<br>*"What is the default storage class and how do I mount an existing PVC in my deployment?"* | References generic storage classes (`standard`, `hostpath`). | References OpenShift 4.22 CSI storage classes (`gp3-csi`, `odf`) and volume mounting syntax. |

---

## Verifying Deployment

1. **Verify Pods in `rag-llm` Namespace**:
   ```sh
   oc get pods -n rag-llm
   ```
   Expected pods:
   - `pgvector-postgresql-...` (PostgreSQL vector database)
   - `populate-vectordb-...` (Completed documentation embedding job)
   - `llm-ui-...` (Gradio assistant frontend)

2. **Verify Pods in `vllm` Namespace**:
   ```sh
   oc get pods -n vllm
   ```
   - `hf-text-generation-server-...` (Running `google/gemma-3-4b-it` on GPU)

3. **Access Application**:
   Navigate to OpenShift Web Console -> **Networking** -> **Routes** in the `rag-llm` namespace to access the application URL.
