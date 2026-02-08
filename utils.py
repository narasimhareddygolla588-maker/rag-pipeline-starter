from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DOC_DIR = DATA_DIR / "sample_docs"
INDEX_DIR = DATA_DIR / "index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)

def load_docs():
    docs = []
    for file in DOC_DIR.glob("*.txt"):
        docs.append((file.name, file.read_text(encoding="utf-8")))
    return docs

def chunk_text(text, chunk_size=500, overlap=80):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks
