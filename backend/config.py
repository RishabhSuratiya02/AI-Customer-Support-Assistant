import os

from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent[1]

load_dotenv(BASE_DIR/ ".env")

groq_api_key = os.getenv("GROQ_API_KEY")

LLM_MODEL = "openai/gpt-oss-20b"
temperature = 0
max_tokens_output = 800

embedding_model = "sentence-transformers/all-MiniLM-L6-v2"

chunk_size = 1000
chunk_overlap = 200

retrieval_k = 4

DOCUMENTS_DIR = BASE_DIR / "data" / "documents"
CHROMA_DB_DIR = BASE_DIR / "data" / "chroma_db"

def validate_config() -> None:
    """Check required configuration before processing a PDF."""
    if not groq_api_key or not groq_api_key.strip():
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to your .env file."
        )


DOCUMENTS_DIR.mkdir(parents=True, exits_ok = True)
CHROMA_DB_DIR.mkdir(parents=True, exits_ok = True)

