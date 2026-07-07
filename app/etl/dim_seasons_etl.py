from pathlib import Path

import pandas as pd


class DimSeasonsETL:

    def __init__(self):

        self.input_path = Path(
            "warehouse/processed/player_profiles.csv"
        )

        self.output_path = Path(
            "warehouse/processed/dim_seasons.csv"
        )

    # ---------------------------------------
    # Extract
    # ---------------------------------------

    def extract(self):

        print("Reading player profiles...")

        return pd.read_csv(
            self.input_path,
            low_memory=False
        )

    # ---------------------------------------
    # Transform
    # ---------------------------------------

    def transform(self, dataframe):

        print("\nBuilding Season Dimension...")

        seasons = dataframe[
            ["season"]
        ].copy()

        seasons = seasons.dropna()

        seasons = seasons.drop_duplicates()

        seasons = seasons.sort_values(
            by="season"
        )

        seasons = seasons.reset_index(
            drop=True
        )

        seasons.insert(

            0,

            "season_id",

            range(
                1,
                len(seasons) + 1
            )

        )

        seasons["season_name"] = (

            seasons["season"]

            .astype(int)

            .astype(str)

            +

            "/"

            +

            (

                seasons["season"]

                .astype(int)

                + 1

            )

            .astype(str)

            .str[-2:]

        )

        print(
            f"Unique Seasons : {len(seasons)}"
        )

        return seasons

    # ---------------------------------------
    # Validate
    # ---------------------------------------

    def validate(self, dataframe):

        print("\n" + "=" * 50)
        print("DIM SEASONS REPORT")
        print("=" * 50)

        print(f"Rows               : {len(dataframe)}")
        print(f"Columns            : {len(dataframe.columns)}")

        print(
            f"Duplicate Seasons  : "
            f"{dataframe['season'].duplicated().sum()}"
        )

        print(
            f"Missing Seasons    : "
            f"{dataframe['season'].isna().sum()}"
        )

        print("=" * 50)

    # ---------------------------------------
    # Load
    # ---------------------------------------

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

    # ---------------------------------------
    # Run
    # ---------------------------------------

    def run(self):

        print("=" * 60)
        print("DIM SEASONS ETL")
        print("=" * 60)

        dataframe = self.extract()

        dataframe = self.transform(
            dataframe
        )

        self.validate(
            dataframe
        )

        self.load(
            dataframe
        )

        print(
            "\nDIM SEASONS ETL Completed Successfully."
        )