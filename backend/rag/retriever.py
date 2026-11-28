from backend.rag.vector_store import get_vector_store

def retrieve_documents(query: str, k: int = 4):
    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    if k < 1:
        raise ValueError("K must be atleast 1.")

    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query=query,
        k=k
    )
    return results