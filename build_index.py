import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import INDEX_DIR

def main():
    chunk_file = INDEX_DIR / "chunks.jsonl"
    rows = [json.loads(line) for line in chunk_file.read_text(encoding="utf-8").splitlines()]
    texts = [row["text"] for row in rows]

    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    vectors = vectorizer.fit_transform(texts)

    np.save(INDEX_DIR / "vectors.npy", vectors.toarray())

    # FIX: Convert numpy int64 to normal Python int so JSON can save it
    vocab = {k: int(v) for k, v in vectorizer.vocabulary_.items()}
    (INDEX_DIR / "vocab.json").write_text(json.dumps(vocab), encoding="utf-8")

    print("Search index created (vectors.npy + vocab.json)")

if __name__ == "__main__":
    main()
