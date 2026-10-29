from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import faiss
import numpy as np

# Knowledge base — the domain-specific content this app answers questions about
documents = [
    "Python is a high-level programming language known for its readability and versatility.",
    "Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
    "FAISS is a library developed by Meta for efficient similarity search and clustering of dense vectors.",
    "Retrieval Augmented Generation combines information retrieval with text generation to produce accurate answers.",
    "Sentence embeddings are numerical representations of text that capture semantic meaning.",
    "Deep learning uses neural networks with multiple layers to model complex patterns in data.",
]

# Load embedding model and build the search index
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embed_model.encode(documents)
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

# Load the generation model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
gen_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
def answer_question(query, k=3):
    """
    Core application function: given a user question, retrieve relevant
    context and generate an answer. This is the main entry point of the MVP.
    """
    # Retrieve relevant documents
    query_embedding = embed_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    retrieved_docs = [documents[idx] for idx in indices[0]]
    context = " ".join(retrieved_docs)

    # Generate answer using retrieved context
    prompt = f"Answer the question based on the context below.\n\nContext: {context}\n\nQuestion: {query}\n\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = gen_model.generate(**inputs, max_length=100)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer, retrieved_docs

if __name__ == "__main__":
    # Simple manual test when running this file directly
    query = "What is FAISS used for?"
    answer, sources = answer_question(query)
    print(f"Question: {query}")
    print(f"Answer: {answer}")