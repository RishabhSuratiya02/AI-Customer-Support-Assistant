from langchain_chroma import Chroma
from backend.config import CHROMA_DB_DIR
from backend.rag.embeddings import get_embedding_model


_vector_store = None

def get_vector_store():
    global _vector_store

    if _vector_store is None:
        embedding_model = get_embedding_model()

        _vector_store = Chroma(
            collection_name="techstore_knowledge_base",
            embedding_function= embedding_model,
            persist_directory=str(CHROMA_DB_DIR)

        )

    return _vector_store


def delete_existing_documents(filename: str):
    vector_store  = get_vector_store()
    vector_store.delete(
        where={"filename": filename}
    )


def add_documents(documents):
    if not documents:
        raise ValueError("No Document provided.")

    filename = documents[0].metadata.get("filename")

    if not filename:
        raise ValueError("Document filename is missing.")

    delete_existing_documents(filename)


    vector_store = get_vector_store()
    vector_store.add_documents(documents=documents)

    return len(documents)


