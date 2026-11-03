"""Embed the portal snapshot and publish a complete PGVector index."""

import json
import logging
import os
import time
from types import SimpleNamespace
from uuid import uuid4

import psycopg
from psycopg import sql
from psycopg.types.json import Json
from sentence_transformers import SentenceTransformer
import torch

from portal_loader import GitLoader

logger = logging.getLogger(__name__)


def connect():
    for attempt in range(10):
        try:
            return psycopg.connect(
                host=os.environ["DB_HOST"], port=os.environ["DB_PORT"],
                dbname=os.environ["DB_NAME"], user=os.environ["DB_USERNAME"],
                password=os.environ["DB_PASS"], connect_timeout=5,
            )
        except psycopg.OperationalError:
            if attempt == 9:
                raise
            logger.warning("Waiting for PGVector, attempt %d/10", attempt + 1)
            time.sleep(2)


def load_model(device):
    if device == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError(f"CUDA requested but unavailable (PyTorch CUDA build: {torch.version.cuda})")
        logger.info("Using CUDA device %s", torch.cuda.get_device_name(0))
    start = time.monotonic()
    model = SentenceTransformer(os.environ["EMBEDDING_MODEL"], device=device)
    # Run an actual forward pass before connecting to PostgreSQL.
    sample = model.encode(["OpenShift documentation"], show_progress_bar=False)
    logger.info("Model ready on %s in %.1fs", model.device, time.monotonic() - start)
    return model, len(sample[0])


def publish_index(conn, table_name, model, dimensions, docs, batch_size):
    table = sql.Identifier("public", table_name)
    staging = sql.Identifier("pg_temp", "portal_snapshot_stage")
    embed_seconds = write_seconds = 0.0
    with conn.cursor() as cursor:
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
        cursor.execute(sql.SQL("""
            CREATE TEMP TABLE portal_snapshot_stage (
                langchain_id uuid PRIMARY KEY,
                content text NOT NULL,
                embedding vector({}),
                langchain_metadata json
            ) ON COMMIT DROP
        """).format(sql.Literal(dimensions)))
        copy_query = sql.SQL("COPY {} (langchain_id, content, embedding, langchain_metadata) FROM STDIN").format(staging)

        for offset in range(0, len(docs), batch_size):
            batch = docs[offset:offset + batch_size]
            texts = [doc.page_content.replace("\x00", "") for doc in batch]
            start = time.monotonic()
            vectors = model.encode([text.replace("\n", " ") for text in texts],
                                   batch_size=batch_size, show_progress_bar=False)
            embed_elapsed = time.monotonic() - start
            start = time.monotonic()
            with cursor.copy(copy_query) as copy:
                for doc, text, vector in zip(batch, texts, vectors, strict=True):
                    copy.write_row((uuid4(), text, json.dumps(vector.tolist(), allow_nan=False),
                                    Json(doc.metadata)))
            write_elapsed = time.monotonic() - start
            embed_seconds += embed_elapsed
            write_seconds += write_elapsed
            logger.info("Staged %d/%d chunks (embedding %.2fs, COPY %.2fs)",
                        offset + len(batch), len(docs), embed_elapsed, write_elapsed)

        start = time.monotonic()
        cursor.execute(sql.SQL("CREATE TABLE IF NOT EXISTS {} (LIKE {} INCLUDING ALL)").format(table, staging))
        cursor.execute(sql.SQL("TRUNCATE TABLE {}").format(table))
        cursor.execute(sql.SQL("""
            INSERT INTO {} (langchain_id, content, embedding, langchain_metadata)
            SELECT langchain_id, content, embedding, langchain_metadata FROM {}
        """).format(table, staging))
        if cursor.rowcount != len(docs):
            raise RuntimeError(f"Expected {len(docs)} indexed chunks, inserted {cursor.rowcount}")
    conn.commit()
    logger.info("Published %d chunks (embedding %.1fs, COPY %.1fs, publish %.1fs)",
                len(docs), embed_seconds, write_seconds, time.monotonic() - start)


def main():
    logging.basicConfig(level=os.environ.get("LOG_LEVEL", "info").upper(),
                        format="%(asctime)s %(levelname)s %(message)s")
    device = os.environ["EMBEDDING_DEVICE"]
    batch_size = int(os.environ["EMBEDDING_BATCH_SIZE"])
    if batch_size < 1:
        raise ValueError("Embedding batch size must be positive")
    model, dimensions = load_model(device)
    config = SimpleNamespace(
        repo_sources=json.loads(os.environ["REPO_SOURCES"]),
        chunk_size=int(os.environ["CHUNK_SIZE"]),
        chunk_overlap=int(os.environ["CHUNK_OVERLAP"]),
    )
    docs = GitLoader(config).load()
    with connect() as conn:
        publish_index(conn, os.environ["PGVECTOR_COLLECTION_NAME"],
                      model, dimensions, docs, batch_size)


if __name__ == "__main__":
    main()
