from pathlib import Path

import pandas as pd


class DimClubsETL:

    def __init__(self):

        self.input_path = Path(
            "warehouse/processed/player_profiles.csv"
        )

        self.output_path = Path(
            "warehouse/processed/dim_clubs.csv"
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

        print("\nBuilding Club Dimension...")

        clubs = dataframe[["club"]].copy()

        # Remove missing clubs
        clubs = clubs.dropna()

        # Clean whitespace
        clubs["club"] = (
            clubs["club"]
            .astype(str)
            .str.strip()
        )

        # Remove blank names
        clubs = clubs[
            clubs["club"] != ""
        ]

        # Remove duplicates
        clubs = clubs.drop_duplicates()

        # Sort alphabetically
        clubs = clubs.sort_values(
            by="club"
        )

        clubs = clubs.reset_index(
            drop=True
        )

        # Generate surrogate key
        clubs.insert(
            0,
            "club_id",
            range(1, len(clubs) + 1)
        )

        # Rename column
        clubs.rename(
            columns={
                "club": "club_name"
            },
            inplace=True
        )

        print(f"Unique Clubs : {len(clubs)}")

        return clubs
    
    # ---------------------------------------
    # Validate
    # ---------------------------------------

    def validate(self, dataframe):

        print("\n" + "=" * 50)
        print("DIM CLUBS REPORT")
        print("=" * 50)

        print(f"Rows               : {len(dataframe)}")
        print(f"Columns            : {len(dataframe.columns)}")

        print(
            f"Duplicate Clubs    : "
            f"{dataframe['club_name'].duplicated().sum()}"
        )

        print(
            f"Missing Club Names : "
            f"{dataframe['club_name'].isna().sum()}"
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

        print(f"\nSaved to {self.output_path}")

    # ---------------------------------------
    # Run
    # ---------------------------------------

    def run(self):

        print("=" * 60)
        print("DIM CLUBS ETL")
        print("=" * 60)

        dataframe = self.extract()

        dataframe = self.transform(dataframe)

        self.validate(dataframe)

        self.load(dataframe)

        print("\nDIM CLUBS ETL Completed Successfully.")