from backend.rag.document_loader import process_file
from backend.rag.vector_store import add_documents, get_vector_store

file_path = "data/documents/return_refund_policy.pdf"

documents = process_file(file_path)

print("Documents loaded:", len(documents))

added_count = add_documents(documents)
print("Documents added:",added_count)

vector_store = get_vector_store()

record_count = vector_store._collection.count()

print("Total records in ChromaDB:", record_count)

vector_store = get_vector_store()
results = vector_store.similarity_search(
    query="What is the return and refund policy?",
    k=3
)

print("\n Retrieved Documents")

for index, document in enumerate(results, start=1):
    print(f"\nResult {index}:")
    print(document.page_content[:500])
    print("Metadata:", document.metadata)
