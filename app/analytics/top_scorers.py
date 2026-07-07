from app.services.warehouse import DataWarehouse
import pandas as pd


class TopScorers:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Get Top Scorers
    # ---------------------------------------

    def get_top_scorers(
        self,
        season=None,
        club=None,
        limit=10
    ):

        dataframe = self.df.copy()

        # ----------------------------
        # Season Filter
        # ----------------------------

        if season is not None:

            dataframe = dataframe[
                dataframe["season"] == season
            ]

        # ----------------------------
        # Club Filter
        # ----------------------------

        if club is not None:

            dataframe = dataframe[
                dataframe["club"]
                .fillna("")
                .str.lower()
                ==
                club.lower()
            ]

        # ----------------------------
        # Goals
        # ----------------------------

        dataframe["goals"] = pd.to_numeric(
            dataframe["goals"],
            errors="coerce"
        ).fillna(0)

        # ----------------------------
        # Sort
        # ----------------------------

        dataframe = dataframe.sort_values(
            by="goals",
            ascending=False
        )

        dataframe = dataframe.head(limit)

        # ----------------------------
        # Ranking
        # ----------------------------

        dataframe = dataframe.reset_index(
            drop=True
        )

        dataframe.insert(
            0,
            "rank",
            range(1, len(dataframe) + 1)
        )

        return dataframe[
            [
                "rank",
                "player",
                "club",
                "season",
                "goals"
            ]
        ]

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        season=None,
        club=None,
        limit=10
    ):

        print()

        print("=" * 60)

        if season is None:

            print(f"TOP {limit} PREMIER LEAGUE SCORERS")

        else:

            print(f"TOP {limit} SCORERS - {season}")

        print("=" * 60)

        print(

            self.get_top_scorers(
                season=season,
                club=club,
                limit=limit
            )

        )