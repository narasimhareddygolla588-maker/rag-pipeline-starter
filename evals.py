from rag_answer import main

QUESTIONS = [
    "What is the refund policy?",
    "How long is the warranty?"
]

def run_evals():
    for q in QUESTIONS:
        main(q, top_k=2)

if __name__ == "__main__":
    run_evals()
