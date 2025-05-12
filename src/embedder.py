
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

def embed_chunks(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts)
    return embeddings

