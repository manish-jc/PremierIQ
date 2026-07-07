from app.services.warehouse import DataWarehouse

from app.analytics.top_scorers import TopScorers
from app.analytics.top_assists import TopAssists
from app.analytics.goalkeeper_rankings import GoalkeeperRankings
from app.analytics.club_rankings import ClubRankings

import pandas as pd


class SeasonSummary:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

        self.scorers = TopScorers()

        self.assists = TopAssists()

        self.goalkeepers = GoalkeeperRankings()

        self.clubs = ClubRankings()


    # ---------------------------------------
    # Season Overview
    # ---------------------------------------

    def get_overview(
        self,
        season
    ):

        dataframe = self.df.copy()

        dataframe = dataframe[
            dataframe["season"] == season
        ]

        numeric_columns = [

            "goals",
            "assists",
            "appearances"

        ]

        for column in numeric_columns:

            dataframe[column] = pd.to_numeric(

                dataframe[column],

                errors="coerce"

            ).fillna(0)

        overview = {

            "season": season,

            "players":

                dataframe["player"].nunique(),

            "clubs":

                dataframe["club"].nunique(),

            "goals":

                int(dataframe["goals"].sum()),

            "assists":

                int(dataframe["assists"].sum()),

            "appearances":

                int(dataframe["appearances"].sum())

        }

        return overview
    

    # ---------------------------------------
    # Season Summary
    # ---------------------------------------

    def get_season_summary(
        self,
        season
    ):

        overview = self.get_overview(
            season
        )

        top_scorer = self.scorers.get_top_scorers(
            season=season,
            limit=1
        ).iloc[0]

        top_assist = self.assists.get_top_assists(
            season=season,
            limit=1
        ).iloc[0]

        best_goalkeeper = self.goalkeepers.get_top_goalkeepers(
            season=season,
            limit=1
        ).iloc[0]

        best_club = self.clubs.get_club_rankings(
            season=season,
            limit=1
        ).iloc[0]

        summary = {

            "overview": overview,

            "awards": {

                "golden_boot": {

                    "player": top_scorer["player"],

                    "goals": int(
                        top_scorer["goals"]
                    )

                },

                "playmaker": {

                    "player": top_assist["player"],

                    "assists": int(
                        top_assist["assists"]
                    )

                },

                "best_goalkeeper": {

                    "player": best_goalkeeper["player"],

                    "score": round(
                        best_goalkeeper["goalkeeper_score"],
                        2
                    )

                },

                "best_club": {

                    "club": best_club["club"],

                    "score": round(
                        best_club["club_score"],
                        2
                    )

                }

            }

        }

        return summary

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        season
    ):

        summary = self.get_season_summary(
            season
        )

        print()

        print("=" * 70)

        print(
            f"PREMIER LEAGUE SEASON SUMMARY ({season})"
        )

        print("=" * 70)

        print("\nOVERVIEW")
        print("-" * 70)

        for key, value in summary["overview"].items():

            print(

                f"{key.replace('_', ' ').title():25}: {value}"

            )

        print("\nAWARDS")
        print("-" * 70)

        print(

            f"{'Golden Boot':25}: "
            f"{summary['awards']['golden_boot']['player']} "
            f"({summary['awards']['golden_boot']['goals']} goals)"

        )

        print(

            f"{'Playmaker':25}: "
            f"{summary['awards']['playmaker']['player']} "
            f"({summary['awards']['playmaker']['assists']} assists)"

        )

        print(

            f"{'Best Goalkeeper':25}: "
            f"{summary['awards']['best_goalkeeper']['player']} "
            f"(Score: {summary['awards']['best_goalkeeper']['score']})"

        )

        print(

            f"{'Best Club':25}: "
            f"{summary['awards']['best_club']['club']} "
            f"(Score: {summary['awards']['best_club']['score']})"

        )

        print()

        print("=" * 70)