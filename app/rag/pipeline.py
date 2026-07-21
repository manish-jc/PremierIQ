from app.retrieval.retriever import FootballRetriever
from app.utils.gemini_client import GeminiClient

from app.rag.router import QuestionRouter
from app.rag.entity_extractor import EntityExtractor
from app.rag.context_builder import ContextBuilder


class RAGPipeline:

    def __init__(self):

        print("Loading PremierIQ Pipeline...")

        self.retriever = FootballRetriever()
        self.gemini = GeminiClient()

        self.router = QuestionRouter()
        self.extractor = EntityExtractor()
        self.context_builder = ContextBuilder()

        print("Pipeline Loaded Successfully.\n")

    # ---------------------------------------
    # Build Prompt
    # ---------------------------------------

    def build_prompt(
        self,
        context,
        question
    ):

        return f"""
You are PremierIQ, an AI assistant specializing in the English Premier League.

Answer ONLY using the provided context.

If the context is insufficient, reply:
"I couldn't find enough information in my knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

    # ---------------------------------------
    # Ask
    # ---------------------------------------

    def ask(
        self,
        question
    ):

        print("=" * 80)
        print("QUESTION :", question)
        print("=" * 80)

        # ---------------------------------------------------
        # Step 1 : Route
        # ---------------------------------------------------

        route_info = self.router.route(question)

        print("\nROUTER OUTPUT")
        print(route_info)

        # ---------------------------------------------------
        # Step 2 : Analytics Context
        # ---------------------------------------------------

        context = self.context_builder.build(

            route_info,

            self.extractor,

            question

        )

        print("\nANALYTICS CONTEXT")
        print(context)

        # ---------------------------------------------------
        # Analytics Answer
        # ---------------------------------------------------

        if context is not None:

            print("\nUsing Analytics Context")

            prompt = self.build_prompt(

                context,

                question

            )

            answer = self.gemini.generate(prompt)

            print("\nGemini Answer Generated")

            return answer

        # ---------------------------------------------------
        # RAG Fallback
        # ---------------------------------------------------

        print("\nNo Analytics Context Found")
        print("Switching to RAG Retrieval...\n")

        docs = self.retriever.search(question)

        print(f"Documents Retrieved : {len(docs)}")

        for i, doc in enumerate(docs):

            print("\n" + "-" * 80)
            print(f"Document {i+1}")
            print("-" * 80)

            print(doc.page_content[:500])

        context = "\n\n".join(

            doc.page_content

            for doc in docs

        )

        print("\nFINAL CONTEXT SENT TO GEMINI")
        print(context[:1000])

        prompt = self.build_prompt(

            context,

            question

        )

        answer = self.gemini.generate(prompt)

        print("\nGemini Answer Generated")

        return answer


if __name__ == "__main__":

    pipeline = RAGPipeline()

    while True:

        question = input("\nQuestion : ")

        answer = pipeline.ask(question)

        print("\n")
        print("=" * 80)
        print(answer)
        print("=" * 80)