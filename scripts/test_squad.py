from app.services.football_api import FootballAPI

api = FootballAPI()

# Manchester City
TEAM_ID = 50

squad = api.get_team_squad(TEAM_ID)

print("Team:", squad["response"][0]["team"]["name"])
print()

for player in squad["response"][0]["players"]:
    print(
        player["id"],
        "-",
        player["name"],
        "-",
        player["position"]
    )