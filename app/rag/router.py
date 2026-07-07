import re


class QuestionRouter:

    def __init__(self):
        pass

    # ---------------------------------------
    # Route Question
    # ---------------------------------------

    def route(self, question):

        question = question.lower()

        # =====================================
        # Comparison
        # =====================================

        if "compare" in question:

            return {
                "route": "comparison"
            }

        # =====================================
        # Rankings
        # =====================================

        if any(keyword in question for keyword in [
            "top scorer",
            "top scorers",
            "most goals"
        ]):

            return {
                "route": "rankings",
                "type": "top_scorers"
            }

        if any(keyword in question for keyword in [
            "top assist",
            "top assists",
            "most assists"
        ]):

            return {
                "route": "rankings",
                "type": "top_assists"
            }

        if any(keyword in question for keyword in [
            "goalkeeper",
            "goalkeepers",
            "best goalkeeper",
            "best goalkeepers"
        ]):

            return {
                "route": "rankings",
                "type": "goalkeepers"
            }

        if any(keyword in question for keyword in [
            "club ranking",
            "best club",
            "best clubs",
            "top clubs"
        ]):

            return {
                "route": "rankings",
                "type": "clubs"
            }

        # =====================================
        # Awards
        # =====================================

        if "golden boot" in question:

            return {
                "route": "awards",
                "type": "golden_boot"
            }

        if "playmaker" in question:

            return {
                "route": "awards",
                "type": "playmaker"
            }

        if "award" in question or "awards" in question:

            return {
                "route": "awards",
                "type": "all"
            }

        # =====================================
        # Season Summary
        # =====================================

        if (
            "season" in question
            or re.search(r"\b20\d{2}\b", question)
        ):

            return {
                "route": "season"
            }

        # =====================================
        # Player / Club Profile
        # =====================================

        if any(keyword in question for keyword in [
            "who is",
            "tell me about",
            "profile"
        ]):

            return {
                "route": "profile"
            }

        # =====================================
        # Default
        # =====================================

        return {
            "route": "knowledge"
        }