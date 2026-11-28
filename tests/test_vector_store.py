# from backend.rag.document_loader import process_file
# from backend.rag.vector_store import add_documents, get_vector_store

# file_path = "data/documents/return_refund_policy.pdf"

# documents = process_file(file_path)

# print("Documents loaded:", len(documents))

# added_count = add_documents(documents)
# print("Documents added:",added_count)

# vector_store = get_vector_store()

# record_count = vector_store._collection.count()

# print("Total records in ChromaDB:", record_count)

# vector_store = get_vector_store()
# results = vector_store.similarity_search(
#     query="What is the return and refund policy?",
#     k=3
# )

# print("\n Retrieved Documents")

# for index, document in enumerate(results, start=1):
#     print(f"\nResult {index}:")
#     print(document.page_content[:500])
#     print("Metadata:", document.metadata)



from backend.rag.document_loader import process_file
from backend.rag.text_splitter import split_documents
from backend.rag.vector_store import add_documents, get_vector_store

file_path = "data/documents/return_refund_policy.pdf"

# Step 1: Load PDF
documents = process_file(file_path)
print("Documents loaded:", len(documents))

# Step 2: Split documents into chunks
chunks = split_documents(documents)
print("Chunks generated:", len(chunks))

# Step 3: Store chunks in ChromaDB
added_count = add_documents(chunks)
print("Chunks added:", added_count)

# Step 4: Check total records
vector_store = get_vector_store()
print("Total records in ChromaDB:", vector_store._collection.count())

# Step 5: Test similarity search
results = vector_store.similarity_search(
    query="What is the refund processing time?",
    k=3
)

print("\nRetrieved Results:", len(results))

for index, result in enumerate(results, start=1):
    print(f"\nResult {index}:")
    print("Content:", result.page_content[:300])
    print("Page:", result.metadata.get("page_number"))
    print("Filename:", result.metadata.get("filename"))

