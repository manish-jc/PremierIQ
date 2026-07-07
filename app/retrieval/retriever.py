from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class FootballRetriever:

    def __init__(self):

        print("Loading embedding model...")

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Loading FAISS index...")

        self.vector_db = FAISS.load_local(
            "vector_store",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        print("Retriever Ready!\n")

    def search(self, query):

        results = self.vector_db.similarity_search(query, k=5)

        return results


if __name__ == "__main__":

    retriever = FootballRetriever()

    question = input("Ask a football question: ")

    results = retriever.search(question)

    print("\nTop Results\n")

    for i, doc in enumerate(results, start=1):

        print("=" * 60)
        print(f"Result {i}")
        print("=" * 60)

        print(doc.page_content)

        print("\nMetadata:")

        print(doc.metadata)

        print()