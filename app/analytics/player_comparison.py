from app.services.warehouse import DataWarehouse
import pandas as pd


class PlayerComparison:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Find Player
    # ---------------------------------------

    def get_player(
        self,
        player_name,
        season=None
    ):

        dataframe = self.df.copy()

        dataframe = dataframe[
            dataframe["player"]
            .str.lower()
            ==
            player_name.lower()
        ]

        if season is not None:

            dataframe = dataframe[
                dataframe["season"] == season
            ]

        return dataframe
    

    # ---------------------------------------
    # Compare Players
    # ---------------------------------------

    def compare_players(
        self,
        player1,
        player2,
        season=None
    ):

        first = self.get_player(
            player1,
            season
        )

        second = self.get_player(
            player2,
            season
        )

        if first.empty:

            print(f"{player1} not found.")

            return

        if second.empty:

            print(f"{player2} not found.")

            return

        first = first.iloc[0]

        second = second.iloc[0]

        # ---------------------------------------
        # Statistics to Compare
        # ---------------------------------------

        statistics = [

            "goals",
            "assists",
            "appearances",
            "minutes_played",
            "shots",
            "shots_on_target",
            "passes",
            "touches",
            "tackles",
            "interceptions",
            "yellow_cards",
            "red_cards"

        ]

        comparison = []

        for stat in statistics:

            comparison.append({

                "Statistic": stat.replace("_", " ").title(),

                player1: first.get(stat, 0),

                player2: second.get(stat, 0)

            })

        comparison = pd.DataFrame(comparison)

        return comparison
    

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        player1,
        player2,
        season=None
    ):

        print()

        print("=" * 70)

        if season is None:

            print(f"{player1} vs {player2}")

        else:

            print(f"{player1} vs {player2} ({season})")

        print("=" * 70)

        comparison = self.compare_players(
            player1,
            player2,
            season
        )

        if comparison is not None:

            print(comparison)