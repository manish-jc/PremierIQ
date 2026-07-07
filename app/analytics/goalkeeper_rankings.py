from app.services.warehouse import DataWarehouse
import pandas as pd


class GoalkeeperRankings:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()


    # ---------------------------------------
    # Top Goalkeepers
    # ---------------------------------------

    def get_top_goalkeepers(
        self,
        season=None,
        limit=10
    ):

        dataframe = self.df.copy()

        # ----------------------------
        # Goalkeepers only
        # ----------------------------

        dataframe = dataframe[
            dataframe["position"] == "Goalkeeper"
        ]

        # ----------------------------
        # Season Filter
        # ----------------------------

        if season is not None:

            dataframe = dataframe[
                dataframe["season"] == season
            ]

        statistics = [

            "clean_sheets",
            "saves",
            "penalties_saved",
            "goals_conceded",
            "high_claims",
            "punches",
            "sweeper_clearances"

        ]

        for stat in statistics:

            dataframe[stat] = pd.to_numeric(
                dataframe[stat],
                errors="coerce"
            ).fillna(0)


        dataframe["goalkeeper_score"] = (

            dataframe["clean_sheets"]

            +

            dataframe["saves"] / 10

            +

            dataframe["penalties_saved"] * 3

            +

            dataframe["high_claims"] / 10

            +

            dataframe["punches"] / 20

            +

            dataframe["sweeper_clearances"] / 10

            -

            dataframe["goals_conceded"] / 10

        )

        dataframe = dataframe.sort_values(

            by="goalkeeper_score",

            ascending=False

        )

        dataframe = dataframe.head(limit)

        dataframe = dataframe.reset_index(drop=True)

        dataframe.insert(

            0,

            "rank",

            range(
                1,
                len(dataframe) + 1
            )

        )

        return dataframe[
            [

                "rank",

                "player",

                "club",

                "season",

                "clean_sheets",

                "saves",

                "goals_conceded",

                "goalkeeper_score"

            ]

        ]
    

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        season=None,
        limit=10
    ):

        print()

        print("=" * 70)

        if season is None:

            print(
                f"TOP {limit} PREMIER LEAGUE GOALKEEPERS"
            )

        else:

            print(
                f"TOP {limit} GOALKEEPERS - {season}"
            )

        print("=" * 70)

        print(

            self.get_top_goalkeepers(
                season=season,
                limit=limit
            )

        )