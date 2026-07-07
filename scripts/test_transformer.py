from app.services.football_api import FootballAPI
from app.services.data_transformer import DataTransformer

api = FootballAPI()

players = api.get_players()

player = players["response"][0]

clean_player = DataTransformer.transform_player(player)

if clean_player:
    print(clean_player)
else:
    print("Player skipped (No statistics available)")

print(clean_player)