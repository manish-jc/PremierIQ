from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter


class FAISSStore:

    def __init__(self):

        print("Loading embedding model...")

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Embedding model loaded!")

    def build_index(self):

        # Load documents
        loader = DocumentLoader()
        documents = loader.load_documents()

        print(f"Loaded {len(documents)} documents")

        # Split documents
        splitter = DocumentSplitter()
        chunks = splitter.split(documents)

        print(f"Created {len(chunks)} chunks")

        # Create FAISS index
        vector_db = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        vector_db.save_local("vector_store")

        print("\nFAISS Index Created Successfully!")


if __name__ == "__main__":

    store = FAISSStore()

    store.build_index()