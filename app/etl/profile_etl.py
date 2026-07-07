from pathlib import Path

import pandas as pd

from app.preprocessing.transformers import transform_player_profiles
from app.preprocessing.validators import validate_player_profiles


class PlayerProfileETL:

    def __init__(self):

        self.raw_path = Path(
            "warehouse/raw/squad_profiles/DATA_CSV"
        )

        self.output_path = Path(
            "warehouse/processed/player_profiles.csv"
        )

    # ------------------------------------
    # Extract
    # ------------------------------------

    def extract(self):

        all_dataframes = []

        season_folders = sorted(self.raw_path.iterdir())

        for season_folder in season_folders:

            season = season_folder.name.replace("Season_", "")

            for csv_file in season_folder.glob("*.csv"):

                df = pd.read_csv(csv_file)

                club = csv_file.stem.rsplit("_", 2)[0]
                club = club.replace("_", " ")

                df["season"] = int(season)
                df["club"] = club

                all_dataframes.append(df)

        return all_dataframes

    # ------------------------------------
    # Transform
    # ------------------------------------

    def transform(self, dataframes):

        df = pd.concat(
            dataframes,
            ignore_index=True
        )

        df.columns = [
            column.lower().strip()
            for column in df.columns
        ]

        df = transform_player_profiles(df)

        return df

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

        print(f"\nSaved to {self.output_path}")

    # ------------------------------------
    # Run
    # ------------------------------------

    def run(self):

        print("Extracting player profiles...")

        dataframes = self.extract()

        print(f"Read {len(dataframes)} club files.")

        dataframe = self.transform(dataframes)

        print(f"Total Players: {len(dataframe)}")

        validate_player_profiles(dataframe)

        self.load(dataframe)