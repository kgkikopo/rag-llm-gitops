"""Load the verified Markdown corpus and preserve section citations."""

import json
import logging
import re
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

logger = logging.getLogger(__name__)
HEADING = re.compile(r"^ {0,3}(#{2,6})\s+(.+?)\s*$")
NUMBER = re.compile(r"^(\d+(?:\.\d+)+)\.\s+")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")


def chapter_paths(toc):
    paths = {}
    for category in toc:
        for manual in category["manuals"]:
            for chapter in manual["chapters"]:
                parent = [manual["title"], chapter["title"]]
                paths[chapter["path"]] = parent
                for section in chapter["subchapters"]:
                    paths[section["path"]] = [*parent, section["title"]]
    return paths


def sections(text, row, root_path):
    """Split at indexed headings outside fenced code, retaining parent titles."""
    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Missing document heading in {row['path']}")
    current = row
    stack = []
    body = []
    fence = None
    headings = iter(row["headings"])
    expected = next(headings, None)
    for line in lines[1:]:
        marker = FENCE.match(line)
        if fence:
            body.append(line)
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
        heading = HEADING.match(line)
        if not fence and expected and heading:
            title = heading[2]
            number = NUMBER.match(title)
            matches = (number[1] == expected["section_number"] if number
                       else expected["section_number"] is None and title == expected["title"])
            if matches:
                yield root_path + [name for _, name in stack], current, "".join(body)
                depth = len(heading[1])
                while stack and stack[-1][0] >= depth:
                    stack.pop()
                stack.append((depth, expected["title"]))
                current = expected
                expected = next(headings, None)
                body = []
                continue
        body.append(line)
    if expected:
        raise ValueError(f"Indexed heading missing from {row['path']}: {expected['title']}")
    yield root_path + [name for _, name in stack], current, "".join(body)


def load_corpus(root, chunk_size, chunk_overlap):
    toc = json.loads((root / "toc.json").read_text(encoding="utf-8"))
    paths = chapter_paths(toc)
    seen = set()
    with (root / "index.jsonl").open(encoding="utf-8") as index:
        for line in index:
            row = json.loads(line)
            path = row["path"]
            file = (root / path).resolve()
            if path in seen or not file.is_relative_to(root.resolve()) or file.suffix != ".md":
                raise ValueError(f"Invalid or duplicate corpus path: {path}")
            seen.add(path)
            docs = []
            for titles, section, body in sections(file.read_text(encoding="utf-8"), row, paths[path]):
                if not body.strip():
                    continue
                heading_path = " > ".join(titles)
                prefix = heading_path + "\n\n"
                size = chunk_size - len(prefix)
                if size <= 0:
                    raise ValueError(f"Chunk size is too small for the heading path in {path}")
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=size, chunk_overlap=min(chunk_overlap, size - 1),
                )
                url = section["source_url"]
                for chunk in splitter.split_text(body):
                    docs.append(Document(
                        page_content=prefix + chunk,
                        metadata={
                            "source": url,
                            "source_url": url,
                            "heading_path": heading_path,
                            "path": path,
                            "version": row["version"],
                            "section_number": section["section_number"],
                            "chunk_id": len(docs),
                        },
                    ))
            for doc in docs:
                doc.metadata["chunk_total"] = len(docs)
            yield from docs
    if seen != paths.keys():
        raise ValueError("The corpus index and table of contents disagree")


class GitLoader:
    """Adapter for the vector-embedder job's Git loader entry point."""

    def __init__(self, config):
        self.config = config

    def load(self):
        chunks = []
        for entry in self.config.repo_sources:
            with TemporaryDirectory() as temp:
                checkout = Path(temp) / "repo"
                subprocess.run(["git", "init", "--quiet", str(checkout)], check=True)
                subprocess.run(
                    ["git", "fetch", "--quiet", "--depth", "1", "--", entry["repo"], entry["branch"]],
                    cwd=checkout, check=True,
                )
                subprocess.run(["git", "checkout", "--quiet", "--detach", "FETCH_HEAD"],
                               cwd=checkout, check=True)
                chunks.extend(load_corpus(checkout / entry["path"], self.config.chunk_size,
                                          self.config.chunk_overlap))
        if not chunks:
            raise ValueError("The Markdown corpus produced no chunks")
        logger.info("Loaded %d Markdown chunks with published citations", len(chunks))
        return chunks
