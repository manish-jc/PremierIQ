from app.services.warehouse import DataWarehouse
import pandas as pd


class ClubRankings:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Club Rankings
    # ---------------------------------------

    def get_club_rankings(
        self,
        season=None,
        limit=10
    ):

        dataframe = self.df.copy()

        # ---------------------------------------
        # Remove unmatched players
        # ---------------------------------------

        dataframe = dataframe[
            dataframe["player_id"].notna()
        ]

        # ---------------------------------------
        # Season Filter
        # ---------------------------------------

        if season is not None:

            dataframe = dataframe[
                dataframe["season"] == season
            ]

        # ---------------------------------------
        # Convert statistics to numeric
        # ---------------------------------------

        statistics = [

            "goals",
            "assists",
            "shots",
            "passes",
            "yellow_cards",
            "red_cards"

        ]

        for stat in statistics:

            dataframe[stat] = pd.to_numeric(

                dataframe[stat],

                errors="coerce"

            ).fillna(0)

        # ---------------------------------------
        # Group by Club
        # ---------------------------------------

        clubs = dataframe.groupby(
            "club"
        ).agg({

            "goals": "sum",

            "assists": "sum",

            "shots": "sum",

            "passes": "sum",

            "yellow_cards": "sum",

            "red_cards": "sum"

        }).reset_index()

        # ---------------------------------------
        # Club Score
        # ---------------------------------------

        clubs["club_score"] = (

            clubs["goals"]

            +

            clubs["assists"]

            +

            clubs["shots"] / 10

            +

            clubs["passes"] / 100

            -

            clubs["yellow_cards"]

            -

            clubs["red_cards"] * 3

        )

        # ---------------------------------------
        # Ranking
        # ---------------------------------------

        clubs = clubs.sort_values(

            by="club_score",

            ascending=False

        )

        clubs = clubs.head(limit)

        clubs = clubs.reset_index(
            drop=True
        )

        clubs.insert(

            0,

            "rank",

            range(
                1,
                len(clubs) + 1
            )

        )

        return clubs

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
                f"TOP {limit} PREMIER LEAGUE CLUBS"
            )

        else:

            print(
                f"TOP {limit} CLUBS - {season}"
            )

        print("=" * 70)

        print(

            self.get_club_rankings(
                season=season,
                limit=limit
            )

        )
        