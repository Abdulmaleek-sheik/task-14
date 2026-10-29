# MVP Application — Testing & Metrics Documentation

## Overview
This document summarizes the testing results and performance metrics for the AI-powered Q&A application built using Retrieval Augmented Generation (RAG).

## Architecture
- **Retrieval:** Sentence Transformers (`all-MiniLM-L6-v2`) + FAISS for semantic search over a small knowledge base
- **Generation:** Google FLAN-T5-base for answer generation based on retrieved context

## Test Results

| Test # | Question | Result | Score |
|--------|----------|--------|-------|
| 1 | What is FAISS used for? | PASS | 100% |
| 2 | What is Python known for? | FAIL | <50% |
| 3 | What is deep learning? | PASS | 100% |

**Overall Accuracy: 2/3 tests passed (67%)**

## Methodology
Each test question is paired with a set of expected keywords that a correct answer should contain. Since the application uses a generative language model (not exact-match retrieval), answers are evaluated by checking what percentage of expected keywords appear in the generated response. A test passes if at least 50% of expected keywords are present.

## Analysis
The application performs reliably on direct, fact-based questions (e.g., FAISS and deep learning definitions), where the knowledge base contains clear, matching content. The one failing test (Python's characteristics) likely reflects a limitation of the lightweight FLAN-T5-base model, which can occasionally generate incomplete or partial answers on certain phrasings.

## Conclusion
This MVP demonstrates a working end-to-end AI application: data retrieval, context-grounded generation, and automated accuracy testing — with a documented 67% pass rate on the initial test suite, providing a baseline for future improvement.