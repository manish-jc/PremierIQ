from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Embedding model loaded successfully!")

    def embed_text(self, text: str):
        return self.model.encode(text)


if __name__ == "__main__":

    service = EmbeddingService()

    sample_text = "Mohamed Salah is Liverpool's right winger."

    embedding = service.embed_text(sample_text)

    print(f"Embedding dimension: {len(embedding)}")
    print(embedding[:10])