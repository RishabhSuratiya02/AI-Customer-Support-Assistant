from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.config import chunk_size, chunk_overlap

def split_documents(documents):
    if not documents:
        raise ValueError("No Documents provided for spilitting.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        length_function = len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)

    return chunks