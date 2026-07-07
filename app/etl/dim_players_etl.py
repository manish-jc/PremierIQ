from pathlib import Path

import pandas as pd


class DimPlayersETL:

    def __init__(self):

        self.input_path = Path(
            "warehouse/processed/player_profiles.csv"
        )

        self.output_path = Path(
            "warehouse/processed/dim_players.csv"
        )

    # ------------------------------------
    # Extract
    # ------------------------------------

    def extract(self):

        print("Reading player profiles...")

        return pd.read_csv(
            self.input_path,
            low_memory=False
        )
    
    # ------------------------------------
    # Transform
    # ------------------------------------

    def transform(self, dataframe):

        print("Building player dimension...")

        # Keep latest season for each player
        dataframe = dataframe.sort_values(
            by="season",
            ascending=False
        )

        dataframe = dataframe.drop_duplicates(
            subset=["player_id"],
            keep="first"
        )

        # Select dimension columns
        dataframe = dataframe[
            [
                "player_id",
                "name",
                "nationality",
                "position",
                "preferred_foot",
                "date_of_birth",
                "birth_year",
                "height_cm",
                "height_category",
                "market_value_eur",
                "market_value_million"
            ]
        ]

        # Rename columns
        dataframe = dataframe.rename(
            columns={
                "name": "player_name"
            }
        )

        # Clean player names
        dataframe["player_name"] = (
            dataframe["player_name"]
            .astype(str)
            .str.strip()
        )

        dataframe = dataframe.sort_values(
            by="player_name"
        )

        dataframe = dataframe.reset_index(
            drop=True
        )

        print(f"Unique Players : {len(dataframe)}")

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

        print(f"\nSaved to {self.output_path}")

    # ------------------------------------
    # Run
    # ------------------------------------

    def run(self):

        print("=" * 60)
        print("DIM PLAYERS ETL")
        print("=" * 60)

        dataframe = self.extract()

        dataframe = self.transform(dataframe)

        print("\nValidation")
        print("-" * 40)

        print(f"Rows                 : {len(dataframe)}")
        print(f"Columns              : {len(dataframe.columns)}")
        print(
            f"Duplicate Player IDs : "
            f"{dataframe['player_id'].duplicated().sum()}"
        )
        print(
            f"Missing Player IDs   : "
            f"{dataframe['player_id'].isna().sum()}"
        )
        print(
            f"Missing Names        : "
            f"{dataframe['player_name'].isna().sum()}"
        )

        self.load(dataframe)

        print("\nDIM PLAYERS ETL Completed Successfully.")