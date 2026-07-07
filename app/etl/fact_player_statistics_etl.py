from pathlib import Path

import pandas as pd


class FactPlayerStatisticsETL:

    def __init__(self):

        self.profile_path = Path(
            "warehouse/processed/player_profiles.csv"
        )

        self.statistics_path = Path(
            "warehouse/processed/player_statistics.csv"
        )

        self.output_path = Path(
            "warehouse/processed/fact_player_statistics.csv"
        )

    # ---------------------------------------
    # Extract
    # ---------------------------------------

    def extract(self):

        print("Loading player profiles...")

        profiles = pd.read_csv(
            self.profile_path,
            low_memory=False
        )

        print("Loading player statistics...")

        statistics = pd.read_csv(
            self.statistics_path,
            low_memory=False
        )

        return profiles, statistics
    

    # ---------------------------------------
    # Prepare Profiles
    # ---------------------------------------

    def prepare_profiles(self, profiles):

        profiles = profiles.copy()

        profiles["join_name"] = (

            profiles["name"]

            .fillna("")

            .astype(str)

            .str.strip()

            .str.lower()

        )

        # Keep only latest season for duplicate
        # player-season combinations

        profiles = (

            profiles

            .sort_values(
                "season",
                ascending=False
            )

            .drop_duplicates(
                subset=[
                    "join_name",
                    "season"
                ]
            )

        )

        profiles = profiles.rename(

            columns={

                "club": "profile_club",

                "position": "profile_position"

            }

        )

        return profiles

    # ---------------------------------------
    # Prepare Statistics
    # ---------------------------------------

    def prepare_statistics(self, statistics):

        statistics = statistics.copy()

        statistics["join_name"] = (

            statistics["player"]

            .fillna("")

            .astype(str)

            .str.strip()

            .str.lower()

        )

        return statistics
    
    # ---------------------------------------
    # Transform
    # ---------------------------------------

    def transform(
        self,
        profiles,
        statistics
    ):

        print("\nBuilding Fact Table...")

        fact = statistics.merge(

            profiles[
                [
                    "player_id",
                    "join_name",
                    "season",
                    "profile_club",
                    "profile_position"
                ]
            ],

            on=[
                "join_name",
                "season"
            ],

            how="left"

        )

        # ---------------------------------------
        # Build Match Status
        # ---------------------------------------

        fact["match_status"] = fact["player_id"].apply(

            lambda value:
                "Matched"
                if pd.notna(value)
                else "Unmatched"

        )

        # ---------------------------------------
        # Final Club & Position
        # ---------------------------------------

        fact["club"] = (
              fact["profile_club"]
              .fillna(fact["club"])
              )
        fact["position"] = (
            fact["profile_position"]
            )

        # ---------------------------------------
        # Remove Temporary Columns
        # ---------------------------------------

        fact.drop(

            columns=[

                "join_name",
                "profile_club",
                "profile_position"

            ],

            inplace=True

        )

        # ---------------------------------------
        # Reorder Columns
        # ---------------------------------------

        metadata_columns = [

            "player_id",
            "player",
            "season",
            "club",
            "position",
            "match_status"

        ]

        statistic_columns = [

            column

            for column in fact.columns

            if column not in metadata_columns

        ]

        fact = fact[
            metadata_columns + statistic_columns
        ]

        print(f"\nRows : {len(fact)}")
        print(f"Columns : {len(fact.columns)}")

        return fact

    # ---------------------------------------
    # Validate
    # ---------------------------------------

    def validate(self, fact):

        print("\n" + "=" * 50)
        print("FACT PLAYER STATISTICS REPORT")
        print("=" * 50)

        print(f"Rows               : {len(fact)}")
        print(f"Columns            : {len(fact.columns)}")

        print(
            f"Matched Players    : "
            f"{fact['match_status'].eq('Matched').sum()}"
        )

        print(
            f"Unmatched Players  : "
            f"{fact['match_status'].eq('Unmatched').sum()}"
        )

        print(
            f"Duplicate Rows     : "
            f"{fact.duplicated().sum()}"
        )

        print(
            f"Missing Player IDs : "
            f"{fact['player_id'].isna().sum()}"
        )

        print("=" * 50)

    # ---------------------------------------
    # Load
    # ---------------------------------------

    def load(self, fact):

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        fact.to_csv(
            self.output_path,
            index=False
        )

        print(f"\nSaved to {self.output_path}")

    # ---------------------------------------
    # Run
    # ---------------------------------------

    def run(self):

        print("=" * 60)
        print("FACT PLAYER STATISTICS ETL")
        print("=" * 60)

        profiles, statistics = self.extract()

        profiles = self.prepare_profiles(profiles)

        statistics = self.prepare_statistics(statistics)

        fact = self.transform(
            profiles,
            statistics
        )

        self.validate(fact)

        self.load(fact)

        print("\nFACT PLAYER STATISTICS ETL Completed Successfully.")