from app.analytics.season_summary import SeasonSummary
import pandas as pd


class SeasonComparison:

    def __init__(self):

        self.summary = SeasonSummary()

    # ---------------------------------------
    # Compare Seasons
    # ---------------------------------------

    def compare(
        self,
        season1,
        season2
    ):

        first = self.summary.get_season_summary(
            season1
        )

        second = self.summary.get_season_summary(
            season2
        )

        comparison = [

            {

                "Statistic": "Goals",

                str(season1):
                    first["overview"]["goals"],

                str(season2):
                    second["overview"]["goals"]

            },

            {

                "Statistic": "Assists",

                str(season1):
                    first["overview"]["assists"],

                str(season2):
                    second["overview"]["assists"]

            },

            {

                "Statistic": "Players",

                str(season1):
                    first["overview"]["players"],

                str(season2):
                    second["overview"]["players"]

            },

            {

                "Statistic": "Clubs",

                str(season1):
                    first["overview"]["clubs"],

                str(season2):
                    second["overview"]["clubs"]

            },

            {

                "Statistic": "Appearances",

                str(season1):
                    first["overview"]["appearances"],

                str(season2):
                    second["overview"]["appearances"]

            }

        ]

        return (

            pd.DataFrame(comparison),

            first,

            second

        )
    

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        season1,
        season2
    ):

        dataframe, first, second = self.compare(

            season1,

            season2

        )

        print()

        print("=" * 70)

        print(f"{season1} vs {season2}")

        print("=" * 70)

        print(dataframe)

        print()

        print("AWARDS")

        print("-" * 70)

        print(

            f"Golden Boot ({season1}) : "

            f"{first['awards']['golden_boot']['player']} "

            f"({first['awards']['golden_boot']['goals']})"

        )

        print(

            f"Golden Boot ({season2}) : "

            f"{second['awards']['golden_boot']['player']} "

            f"({second['awards']['golden_boot']['goals']})"

        )

        print()

        print(

            f"Playmaker ({season1}) : "

            f"{first['awards']['playmaker']['player']} "

            f"({first['awards']['playmaker']['assists']})"

        )

        print(

            f"Playmaker ({season2}) : "

            f"{second['awards']['playmaker']['player']} "

            f"({second['awards']['playmaker']['assists']})"

        )

        print()

        print(

            f"Best Club ({season1}) : "

            f"{first['awards']['best_club']['club']}"

        )

        print(

            f"Best Club ({season2}) : "

            f"{second['awards']['best_club']['club']}"

        )

        print()

        print("=" * 70)