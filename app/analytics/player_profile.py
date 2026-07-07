from app.services.warehouse import DataWarehouse
import pandas as pd


class PlayerProfile:

    def __init__(self):

        warehouse = DataWarehouse()

        self.players = warehouse.get_dim_players()

        self.statistics = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Find Player
    # ---------------------------------------

    def find_player(
        self,
        player_name
    ):

        dataframe = self.players.copy()

        dataframe = dataframe[

            dataframe["player_name"]
            .str.lower()
            ==
            player_name.lower()

        ]

        return dataframe

    # ---------------------------------------
    # Get Statistics
    # ---------------------------------------

    def get_statistics(
        self,
        player_name,
        season=None
    ):

        dataframe = self.statistics.copy()

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
    # Player Profile
    # ---------------------------------------

    def get_player_profile(
        self,
        player_name,
        season=None
    ):

        player = self.find_player(
            player_name
        )

        statistics = self.get_statistics(
            player_name,
            season
        )

        if player.empty:

            print("Player not found.")

            return None

        if statistics.empty:

            print("Statistics not found.")

            return None

        player = player.iloc[0]

        numeric_columns = [

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

        for column in numeric_columns:

            statistics[column] = pd.to_numeric(

                statistics[column],

                errors="coerce"

            ).fillna(0)

        totals = statistics[numeric_columns].sum()


        # ---------------------------------------
        # Career Summary
        # ---------------------------------------

        clubs = sorted(

            statistics["club"]
            .dropna()
            .unique()
            .tolist()

        )

        seasons_played = int(

            statistics["season"].nunique()

        )

        latest_season = statistics["season"].max()

        latest_club = (

            statistics[
                statistics["season"] == latest_season
            ]["club"]

            .dropna()

            .iloc[0]

            if not statistics[
                statistics["season"] == latest_season
            ]["club"].dropna().empty

            else None

        )

        # ---------------------------------------
        # Best Goal Scoring Season
        # ---------------------------------------

        goals_by_season = (

            statistics.groupby("season")["goals"]

            .sum()

            .reset_index()

        )

        best_scoring_season = None

        best_season_goals = 0

        if not goals_by_season.empty:

            best_row = goals_by_season.loc[

                goals_by_season["goals"].idxmax()

            ]

            best_scoring_season = int(
                best_row["season"]
            )

            best_season_goals = int(
                best_row["goals"]
            )

        # ---------------------------------------
        # Advanced Metrics
        # ---------------------------------------

        appearances = int(
            totals["appearances"]
        )

        goals = int(
            totals["goals"]
        )

        assists = int(
            totals["assists"]
        )

        minutes = int(
            totals["minutes_played"]
        )

        advanced_metrics = {

            "goals_per_game":

                round(
                    goals / appearances,
                    2
                )

                if appearances else 0,

            "assists_per_game":

                round(
                    assists / appearances,
                    2
                )

                if appearances else 0,

            "minutes_per_goal":

                round(
                    minutes / goals,
                    2
                )

                if goals else 0

        }

        # ---------------------------------------
        # Player Profile
        # ---------------------------------------

        profile = {

            "player_information": {

                "player_id":
                    player["player_id"],

                "name":
                    player["player_name"],

                "position":
                    player["position"],

                "nationality":
                    player["nationality"],

                "preferred_foot":
                    player["preferred_foot"],

                "date_of_birth":
                    player["date_of_birth"],

                "birth_year":
                    player["birth_year"],

                "height_cm":
                    player["height_cm"],

                "height_category":
                    player["height_category"],

                "market_value_eur":
                    player["market_value_eur"],

                "market_value_million":
                    player["market_value_million"]

            },

            "career_summary": {

                "profile_type":

                    "Career"

                    if season is None

                    else "Season",

                "season":

                    season

                    if season is not None

                    else None,

                "clubs":

                    clubs,

                "latest_club":

                    latest_club,

                "seasons_played":

                    seasons_played,

                "best_scoring_season":

                    best_scoring_season,

                "best_season_goals":

                    best_season_goals

            },

            "statistics": {

                column: int(totals[column])

                for column in numeric_columns

            },

            "advanced_metrics":

                advanced_metrics

        }

        return profile
    
    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        player_name,
        season=None
    ):

        profile = self.get_player_profile(
            player_name,
            season
        )

        if profile is None:

            return

        print()

        print("=" * 70)

        print(profile["player_information"]["name"].upper())

        print("=" * 70)

        # ---------------------------------------
        # Player Information
        # ---------------------------------------

        print("\nPLAYER INFORMATION")
        print("-" * 70)

        for key, value in profile["player_information"].items():

            print(f"{key.replace('_', ' ').title():25}: {value}")

        # ---------------------------------------
        # Career Summary
        # ---------------------------------------

        print("\nCAREER SUMMARY")
        print("-" * 70)

        for key, value in profile["career_summary"].items():

            print(f"{key.replace('_', ' ').title():25}: {value}")

        # ---------------------------------------
        # Statistics
        # ---------------------------------------

        print("\nSTATISTICS")
        print("-" * 70)

        for key, value in profile["statistics"].items():

            print(f"{key.replace('_', ' ').title():25}: {value}")

        # ---------------------------------------
        # Advanced Metrics
        # ---------------------------------------

        print("\nADVANCED METRICS")
        print("-" * 70)

        for key, value in profile["advanced_metrics"].items():

            print(f"{key.replace('_', ' ').title():25}: {value}")

        print("\n" + "=" * 70)