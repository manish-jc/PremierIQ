from pathlib import Path
import pandas as pd

from app.preprocessing.transformers import transform_player_statistics
from app.preprocessing.validators import validate_player_statistics


class PlayerStatisticsETL:

    def __init__(self):

        self.raw_path = Path(
            "warehouse/raw/player_statistics"
        )

        self.output_path = Path(
            "warehouse/processed/player_statistics.csv"
        )

    # ------------------------------------
    # Extract CSV Files
    # ------------------------------------

    def extract_files(self):

        csv_files = sorted(
            self.raw_path.glob("*.csv")
        )

        print(f"\nFound {len(csv_files)} statistic files.\n")

        return csv_files

    # ------------------------------------
    # Clean Individual Statistic File
    # ------------------------------------

    def clean_stat_file(self, csv_file):

        print(f"Reading {csv_file.name}")

        df = pd.read_csv(csv_file)

        statistic = (
            csv_file.stem
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

        df.rename(

            columns={

                "Initial Year": "season",

                "Player": "player",

                "Club": "club",

                "Nationality": "nationality",

                "Stat": statistic

            },

            inplace=True

        )

        df.drop(

            columns=["Rank"],

            errors="ignore",

            inplace=True

        )

        # ----------------------------------------
        # Remove Exact Duplicate Rows
        # ----------------------------------------

        df = df.drop_duplicates()

        # ----------------------------------------
        # Collapse repeated player records
        # ----------------------------------------

        df = (

            df

            .groupby(

                [

                    "season",

                    "player",

                    "club",

                    "nationality"

                ],

                as_index=False

            )

            .first()

        )

        return df, statistic
    

    # ------------------------------------
    # Build Master Statistics Table
    # ------------------------------------

    def build_master_table(self, csv_files):

        master = {}

        for csv_file in csv_files:

            df, statistic = self.clean_stat_file(csv_file)

            print(
                f"Processing {statistic} "
                f"({len(df)} rows)"
            )

            for _, row in df.iterrows():

                season = row["season"]
                player = row["player"]
                club = row["club"]
                nationality = row["nationality"]

                # Handle missing club names
                if pd.isna(club) or club == "-":
                    club = ""

                # Handle missing nationality
                if pd.isna(nationality):
                    nationality = ""

                key = (
                    season,
                    player,
                    club,
                    nationality
                )

                # Create player record if not present
                if key not in master:

                    master[key] = {

                        "season": season,
                        "player": player,
                        "club": club,
                        "nationality": nationality

                    }

                # Add current statistic
                value = row.get(statistic)

                master[key][statistic] = value

        print("\nFinished building master table.")

        dataframe = pd.DataFrame(
            master.values()
        )

        return dataframe
    

    # ------------------------------------
    # Transform
    # ------------------------------------

    def transform(self):

        csv_files = self.extract_files()

        dataframe = self.build_master_table(
            csv_files
        )

        print("\nCleaning statistics dataset...")

        dataframe = transform_player_statistics(
            dataframe
        )

        return dataframe

    # ------------------------------------
    # Load
    # ------------------------------------

    def load(self, dataframe):

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        dataframe.to_csv(
            self.output_path,
            index=False
        )

        print(
            f"\nSaved to {self.output_path}"
        )

    # ------------------------------------
    # Run ETL
    # ------------------------------------

    def run(self):

        print("=" * 60)
        print("PLAYER STATISTICS ETL")
        print("=" * 60)

        dataframe = self.transform()

        print("\nETL Summary")
        print("-" * 40)
        print(f"Rows    : {len(dataframe)}")
        print(f"Columns : {len(dataframe.columns)}")

        validate_player_statistics(
            dataframe
        )

        self.load(
            dataframe
        )

        print("\nETL Completed Successfully.")