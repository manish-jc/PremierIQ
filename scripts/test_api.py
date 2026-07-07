from app.services.football_api import FootballAPI

api = FootballAPI()

players = api.get_players(page=1)

for player in players["response"][:5]:

    stats = player["statistics"][0]

    print(
        player["player"]["name"],
        "->",
        stats["games"]["appearences"]
    )