from app.retrieval.retriever import FootballRetriever
from app.utils.gemini_client import GeminiClient

from app.rag.router import QuestionRouter
from app.rag.entity_extractor import EntityExtractor
from app.rag.context_builder import ContextBuilder


class RAGPipeline:

    def __init__(self):

        self.retriever = FootballRetriever()
        self.gemini = GeminiClient()

        self.router = QuestionRouter()
        self.extractor = EntityExtractor()
        self.context_builder = ContextBuilder()

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

Your job is to answer football questions using ONLY the provided context.

Guidelines:

- Write naturally, like a football analyst.
- Never mention Python, JSON, dictionaries or DataFrames.
- Explain statistics instead of listing raw values.
- If ranking information is provided, present it as a numbered ranking.
- If comparison information is provided, compare both teams or players naturally.
- If season information is provided, summarize the season.
- Keep answers concise but informative.
- If the context is insufficient, reply:
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

        # -----------------------------
        # Route Question
        # -----------------------------

        route_info = self.router.route(question)

        # -----------------------------
        # Build Analytics Context
        # -----------------------------

        context = self.context_builder.build(

            route_info,

            self.extractor,

            question

        )

        # -----------------------------
        # Analytics Response
        # -----------------------------

        if context is not None:

            prompt = self.build_prompt(

                context,

                question

            )

            return self.gemini.generate(prompt)

        # -----------------------------
        # RAG Fallback
        # -----------------------------

        docs = self.retriever.search(question)

        context = "\n\n".join(

            doc.page_content

            for doc in docs

        )

        prompt = self.build_prompt(

            context,

            question

        )

        return self.gemini.generate(prompt)


# ---------------------------------------
# Test
# ---------------------------------------

if __name__ == "__main__":

    pipeline = RAGPipeline()

    while True:

        question = input("\nQuestion : ")

        answer = pipeline.ask(question)

        print()

        print("=" * 80)

        print(answer)