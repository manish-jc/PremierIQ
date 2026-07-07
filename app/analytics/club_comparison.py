from app.services.warehouse import DataWarehouse
import pandas as pd


class ClubComparison:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Get Club
    # ---------------------------------------

    def get_club(
        self,
        club_name,
        season=None
    ):

        dataframe = self.df.copy()

        dataframe = dataframe[

            dataframe["club"]
            .str.lower()

            ==

            club_name.lower()

        ]

        if season is not None:

            dataframe = dataframe[

                dataframe["season"] == season

            ]

        return dataframe
    

    # ---------------------------------------
    # Compare Clubs
    # ---------------------------------------

    def compare_clubs(
        self,
        club1,
        club2,
        season=None
    ):

        first = self.get_club(
            club1,
            season
        )

        second = self.get_club(
            club2,
            season
        )

        if first.empty:

            print(f"{club1} not found.")

            return None

        if second.empty:

            print(f"{club2} not found.")

            return None

        statistics = [

            "goals",
            "assists",
            "appearances",
            "minutes_played",
            "shots",
            "shots_on_target",
            "passes",
            "touches",
            "yellow_cards",
            "red_cards"

        ]

        for stat in statistics:

            first[stat] = pd.to_numeric(

                first[stat],

                errors="coerce"

            ).fillna(0)

            second[stat] = pd.to_numeric(

                second[stat],

                errors="coerce"

            ).fillna(0)

        first_totals = first[statistics].sum()

        second_totals = second[statistics].sum()

        comparison = []

        for stat in statistics:

            comparison.append({

                "Statistic": stat.replace("_", " ").title(),

                club1: int(first_totals[stat]),

                club2: int(second_totals[stat])

            })

        return pd.DataFrame(comparison)
    

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        club1,
        club2,
        season=None
    ):

        print()

        print("=" * 70)

        if season is None:

            print(f"{club1} vs {club2}")

        else:

            print(f"{club1} vs {club2} ({season})")

        print("=" * 70)

        comparison = self.compare_clubs(

            club1,

            club2,

            season

        )

        if comparison is not None:

            print(comparison)