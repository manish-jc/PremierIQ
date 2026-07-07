from pathlib import Path

import pandas as pd


class DataWarehouse:

    def __init__(self):

        self.base_path = Path(
            "warehouse/processed"
        )

        print("Loading Data Warehouse...")

        self.fact_player_statistics = pd.read_csv(
            self.base_path / "fact_player_statistics.csv",
            low_memory=False
        )

        self.dim_players = pd.read_csv(
            self.base_path / "dim_players.csv",
            low_memory=False
        )

        self.dim_clubs = pd.read_csv(
            self.base_path / "dim_clubs.csv",
            low_memory=False
        )

        self.dim_seasons = pd.read_csv(
            self.base_path / "dim_seasons.csv",
            low_memory=False
        )

        print("Warehouse Loaded Successfully.")

    # ---------------------------------------
    # Getters
    # ---------------------------------------

    def get_fact_player_statistics(self):

        return self.fact_player_statistics.copy()

    def get_dim_players(self):

        return self.dim_players.copy()

    def get_dim_clubs(self):

        return self.dim_clubs.copy()

    def get_dim_seasons(self):

        return self.dim_seasons.copy()