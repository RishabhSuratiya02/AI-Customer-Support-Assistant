from backend.rag.embeddings import get_embedding_model

embeddings = get_embedding_model()

vector = embeddings.embed_query("where is my order?")
print("embedding generated sucessfully")
print("Vector dimention:", len(vector))