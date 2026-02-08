import json
from utils import load_docs, chunk_text, INDEX_DIR

def main():
    records = []
    for doc_name, text in load_docs():
        chunks = chunk_text(text)
        for idx, chunk in enumerate(chunks):
            records.append({
                "doc": doc_name,
                "chunk_id": idx,
                "text": chunk
            })

    output_file = INDEX_DIR / "chunks.jsonl"
    with output_file.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")

    print(f"Ingested {len(records)} chunks")

if __name__ == "__main__":
    main()
