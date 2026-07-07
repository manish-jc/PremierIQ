from app.services.warehouse import DataWarehouse
import pandas as pd


class TopAssists:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Get Top Assists
    # ---------------------------------------

    def get_top_assists(
        self,
        season=None,
        club=None,
        limit=10
    ):

        dataframe = self.df.copy()

        # Season Filter
        if season is not None:

            dataframe = dataframe[
                dataframe["season"] == season
            ]

        # Club Filter
        if club is not None:

            dataframe = dataframe[
                dataframe["club"]
                .fillna("")
                .str.lower()
                ==
                club.lower()
            ]

        dataframe["assists"] = pd.to_numeric(
            dataframe["assists"],
            errors="coerce"
        ).fillna(0)

        dataframe = dataframe.sort_values(
            by="assists",
            ascending=False
        )

        dataframe = dataframe.head(limit)

        dataframe = dataframe.reset_index(drop=True)

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
                "assists"
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

            print(f"TOP {limit} PREMIER LEAGUE ASSIST PROVIDERS")

        else:

            print(f"TOP {limit} ASSISTS - {season}")

        print("=" * 60)

        print(

            self.get_top_assists(
                season=season,
                club=club,
                limit=limit
            )

        )