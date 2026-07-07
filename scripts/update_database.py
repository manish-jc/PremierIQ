import pandas as pd

from app.services.football_api import FootballAPI
from app.services.data_transformer import DataTransformer


def update_player_database():

    api = FootballAPI()

    all_players = []

    print("Fetching player data...\n")

    players = api.get_players(page=1)

    for player in players["response"]:

        clean_player = DataTransformer.transform_player(player)

        if clean_player:
            all_players.append(clean_player)

    print(f"Valid Players Found : {len(all_players)}")

    df = pd.DataFrame(all_players)

    df.to_csv(
        "datasets/player_stats.csv",
        index=False
    )

    print("\nplayer_stats.csv created successfully!")


if __name__ == "__main__":

    update_player_database()