from backend.rag.document_loader import process_file
from backend.rag.text_splitter import split_documents

# load pdf step 1

file_path =  "data/documents/return_refund_policy.pdf"

documents = process_file(file_path)

print("Documents loaded:", len(documents))

#split document step 2

chunks = split_documents(documents)
print("Total chunks generated:", len(chunks))

# display chunks  step 3

for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}:")
    print("Content:", chunk.page_content[:300])
    print("Characters:", len(chunk.page_content))
    print("Page:", chunk.metadata.get("page_number"))
    print("Filename:", chunk.metadata.get("filename"))