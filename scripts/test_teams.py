from app.services.football_api import FootballAPI

api = FootballAPI()

teams = api.get_teams()

print("Number of Teams:", teams["results"])
print()

for team in teams["response"]:
    print(
        team["team"]["id"],
        "-",
        team["team"]["name"]
    )