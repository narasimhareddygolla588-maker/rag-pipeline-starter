import argparse
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import INDEX_DIR

def load_index():
    vectors = np.load(INDEX_DIR / "vectors.npy")
    vocab = json.loads((INDEX_DIR / "vocab.json").read_text())
    vectorizer = TfidfVectorizer(stop_words="english", vocabulary=vocab)
    rows = [json.loads(line) for line in (INDEX_DIR / "chunks.jsonl").read_text().splitlines()]
    return vectors, vectorizer, rows

def main(question, top_k=3):
    vectors, vectorizer, rows = load_index()
    query_vec = vectorizer.fit_transform([question]).toarray()
    scores = cosine_similarity(query_vec, vectors)[0]

    top_indices = scores.argsort()[::-1][:top_k]

    print("\nQUESTION:", question)
    print("\nANSWER:")
    for idx in top_indices:
        row = rows[int(idx)]
        print(f"- ({row['doc']}#chunk{row['chunk_id']}) {row['text'][:150]}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", required=True)
    args = parser.parse_args()
    main(args.q)
