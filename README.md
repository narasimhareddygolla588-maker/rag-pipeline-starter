# RAG Pipeline Starter (Python)

This project demonstrates a simple end-to-end Retrieval-Augmented Generation (RAG) workflow.

## What this project does
- Ingests text documents
- Splits them into chunks
- Builds a searchable index
- Retrieves relevant chunks for a question
- Returns answers with citations

## How to run
pip install -r requirements.txt
python src/ingest.py
python src/build_index.py
python src/rag_answer.py --q "What is the refund policy?"
python src/evals.py

## Output
You will see an answer along with citations like:
policy_1.txt#chunk0
