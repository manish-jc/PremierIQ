from app.services.football_api import FootballAPI


class PlayerETL:

    def __init__(self):

        self.api = FootballAPI()

    def extract_all_players(self):

        print("\nFetching Premier League teams...\n")

        teams = self.api.get_teams()

        all_players = []

        for team in teams["response"]:

            team_id = team["team"]["id"]
            team_name = team["team"]["name"]

            print(f"Fetching squad: {team_name}")

            squad = self.api.get_team_squad(team_id)

            players = squad["response"][0]["players"]

            for player in players:

                player["team_name"] = team_name

                all_players.append(player)

        return all_players