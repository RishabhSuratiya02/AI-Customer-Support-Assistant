from backend.rag.retriever import retrieve_documents

query = "what is the refund policy time?"

results = retrieve_documents(query, k=2)

print("retrieve_documents:", len(results))

for index, document in enumerate(results, start=1):
    print(f"\nResult {index}:")
    print("Content:", document.page_content[:500])
    print("Page:", document.metadata.get("page_number"))
    print("Filename:", document.metadata.get("filename"))