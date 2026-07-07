from app.services.warehouse import DataWarehouse
import pandas as pd


class ClubProfile:

    def __init__(self):

        warehouse = DataWarehouse()

        self.clubs = warehouse.get_dim_clubs()

        self.fact = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Find Club
    # ---------------------------------------

    def find_club(
        self,
        club_name
    ):

        dataframe = self.clubs.copy()

        dataframe = dataframe[

            dataframe["club_name"]
            .str.lower()
            ==
            club_name.lower()

        ]

        return dataframe

    # ---------------------------------------
    # Get Club Statistics
    # ---------------------------------------

    def get_club_statistics(
        self,
        club_name,
        season=None
    ):

        dataframe = self.fact.copy()

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
    # Top Scorer
    # ---------------------------------------

    def get_top_scorer(
        self,
        statistics
    ):

        if statistics.empty:

            return None

        dataframe = statistics.copy()

        dataframe["goals"] = pd.to_numeric(

            dataframe["goals"],

            errors="coerce"

        ).fillna(0)

        scorer = (

            dataframe.groupby("player", as_index=False)["goals"]

            .sum()

            .sort_values(

                by="goals",

                ascending=False

            )

            .iloc[0]

        )

        return {

            "player": scorer["player"],

            "goals": int(scorer["goals"])

        }

    # ---------------------------------------
    # Top Assist Provider
    # ---------------------------------------

    def get_top_assist_provider(
        self,
        statistics
    ):

        if statistics.empty:

            return None

        dataframe = statistics.copy()

        dataframe["assists"] = pd.to_numeric(

            dataframe["assists"],

            errors="coerce"

        ).fillna(0)

        assist = (

            dataframe.groupby("player", as_index=False)["assists"]

            .sum()

            .sort_values(

                by="assists",

                ascending=False

            )

            .iloc[0]

        )

        return {

            "player": assist["player"],

            "assists": int(assist["assists"])

        }

    # ---------------------------------------
    # Best Scoring Season
    # ---------------------------------------

    def get_best_scoring_season(
        self,
        statistics
    ):

        if statistics.empty:

            return None

        dataframe = statistics.copy()

        dataframe["goals"] = pd.to_numeric(

            dataframe["goals"],

            errors="coerce"

        ).fillna(0)

        season = (

            dataframe.groupby("season", as_index=False)["goals"]

            .sum()

            .sort_values(

                by="goals",

                ascending=False

            )

            .iloc[0]

        )

        return {

            "season": int(season["season"]),

            "goals": int(season["goals"])

        }
    

    # ---------------------------------------
    # Club Profile
    # ---------------------------------------

    def get_club_profile(
        self,
        club_name,
        season=None
    ):

        club = self.find_club(
            club_name
        )

        if club.empty:

            print("Club not found.")

            return None

        statistics = self.get_club_statistics(
            club_name,
            season
        )

        if statistics.empty:

            print("No statistics found.")

            return None

        # ---------------------------------------
        # Numeric Columns
        # ---------------------------------------

        numeric_columns = [

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

        for column in numeric_columns:

            statistics[column] = pd.to_numeric(

                statistics[column],

                errors="coerce"

            ).fillna(0)

        totals = statistics[numeric_columns].sum()

        # ---------------------------------------
        # Basic Information
        # ---------------------------------------

        club = club.iloc[0]

        seasons_played = int(

            statistics["season"].nunique()

        )

        players_represented = int(

            statistics["player"].nunique()

        )

        average_goals = round(

            totals["goals"] / seasons_played,

            2

        ) if seasons_played else 0

        # ---------------------------------------
        # Helper Methods
        # ---------------------------------------

        top_scorer = self.get_top_scorer(
            statistics
        )

        top_assist = self.get_top_assist_provider(
            statistics
        )

        best_season = self.get_best_scoring_season(
            statistics
        )

        # ---------------------------------------
        # Build Profile
        # ---------------------------------------

        profile = {

            "club_information": {

                "club_id":

                    int(club["club_id"]),

                "club_name":

                    club["club_name"],

                "profile_type":

                    "Career"

                    if season is None

                    else "Season"

            },

            "career_summary": {

                "season":

                    season,

                "seasons_played":

                    seasons_played,

                "players_represented":

                    players_represented,

                "average_goals_per_season":

                    average_goals

            },

            "statistics": {

                column: int(totals[column])

                for column in numeric_columns

            },

            "top_players": {

                "top_scorer":

                    top_scorer,

                "top_assist_provider":

                    top_assist

            },

            "season_summary": {

                "best_scoring_season":

                    best_season

            }

        }

        return profile
    

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        club_name,
        season=None
    ):

        profile = self.get_club_profile(
            club_name,
            season
        )

        if profile is None:

            return

        print()

        print("=" * 70)

        print(
            profile["club_information"]["club_name"].upper()
        )

        print("=" * 70)

        # ---------------------------------------
        # Club Information
        # ---------------------------------------

        print("\nCLUB INFORMATION")
        print("-" * 70)

        for key, value in profile["club_information"].items():

            print(

                f"{key.replace('_', ' ').title():30}: {value}"

            )

        # ---------------------------------------
        # Career Summary
        # ---------------------------------------

        print("\nCAREER SUMMARY")
        print("-" * 70)

        for key, value in profile["career_summary"].items():

            print(

                f"{key.replace('_', ' ').title():30}: {value}"

            )

        # ---------------------------------------
        # Statistics
        # ---------------------------------------

        print("\nSTATISTICS")
        print("-" * 70)

        for key, value in profile["statistics"].items():

            print(

                f"{key.replace('_', ' ').title():30}: {value}"

            )

        # ---------------------------------------
        # Top Players
        # ---------------------------------------

        print("\nTOP PLAYERS")
        print("-" * 70)

        print(

            f"{'Top Scorer':30}: "
            f"{profile['top_players']['top_scorer']['player']} "
            f"({profile['top_players']['top_scorer']['goals']} goals)"

        )

        print(

            f"{'Top Assist Provider':30}: "
            f"{profile['top_players']['top_assist_provider']['player']} "
            f"({profile['top_players']['top_assist_provider']['assists']} assists)"

        )

        # ---------------------------------------
        # Season Summary
        # ---------------------------------------

        print("\nSEASON SUMMARY")
        print("-" * 70)

        best = profile["season_summary"]["best_scoring_season"]

        print(

            f"{'Best Scoring Season':30}: "
            f"{best['season']} "

            f"({best['goals']} goals)"

        )

        print()

        print("=" * 70)