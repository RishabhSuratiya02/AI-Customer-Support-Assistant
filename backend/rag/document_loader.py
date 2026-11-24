from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, CSVLoader

def validate_file(file_path: str | Path) -> Path:
    path = path(file_path).expanduser().resolve()

    if not path.is_file():
        raise FileNotFoundError(f"File not found:{path}")

    if path.suffix.lower() not in [".pdf", ".csv"]:
        raise ValueError("Only PDF and CSV file are supported")

    return path


def load_pdf(path: Path)-> list[Document]:
    try: 
        loader = PyPDFLoader(str(path))
        pages = loader.load()
    except Exception as exc:
        raise ValueError(
            "Could not read the pdf. it may be corrupted or password-protected."
        ) from exc
    return pages

def load_csv(path: Path)-> list[Document]:
    try:
        loader = CSVLoader(str(path))
        documents = loader.load()

    except Exception as exc:
        raise ValueError(
            "could not read the csv. it me be corrupted or password-protechted."

        )   from exc 
    return documents


def filter_documents(documents: list[Document], filename: str)-> list[Document]:
    readable_documents = []

    for document in documents:
        if not document.page_content.strip():
            continue

        document.metadata["filename"] = filename
        page_index = document.metadata.get("page")
        if isinstance(page_index, int):
            document.metadata["page_number"] = page_index +1

        readable_documents.append(document)

    if not readable_documents:
        
        raise ValueError("No readable content found in the file.")

    return readable_documents

def process_file(file_path: str | Path) -> list[Document]:
    path = validate_file(file_path)

    if path.suffix.lower() ==".pdf":
        documents = load_pdf(path)

    elif path.suffix.lower() == ".csv":
        documents = load_csv(path)

    return filter_documents(documents, path.name)    