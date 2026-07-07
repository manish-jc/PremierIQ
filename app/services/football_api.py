import os
import requests

from dotenv import load_dotenv

from app.config import (
    BASE_URL,
    CURRENT_SEASON,
    PREMIER_LEAGUE_ID
)

load_dotenv()


class FootballAPI:

    def __init__(self):

        api_key = os.getenv("FOOTBALL_API_KEY")

        if not api_key:
            raise ValueError("FOOTBALL_API_KEY not found in .env")

        self.headers = {
            "x-apisports-key": api_key
        }

    # ----------------------------------------
    # Generic GET Method
    # ----------------------------------------

    def _get(self, endpoint, params=None):

        url = f"{BASE_URL}/{endpoint}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------------
    # Teams
    # ----------------------------------------

    def get_teams(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "teams",
            {
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Team Squad
    # ----------------------------------------

    def get_team_squad(self, team_id):

        return self._get(
            "players/squads",
            {
                "team": team_id
            }
        )

    # ----------------------------------------
    # Search Player
    # ----------------------------------------

    def search_player(
        self,
        player_name,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "players",
            {
                "search": player_name,
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Player Statistics
    # ----------------------------------------

    def get_player_statistics(
        self,
        player_id,
        season=CURRENT_SEASON
    ):

        return self._get(
            "players",
            {
                "id": player_id,
                "season": season
            }
        )

    # ----------------------------------------
    # Fixtures
    # ----------------------------------------

    def get_fixtures(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "fixtures",
            {
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Standings
    # ----------------------------------------

    def get_standings(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "standings",
            {
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Team Statistics
    # ----------------------------------------

    def get_team_statistics(
        self,
        team_id,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "teams/statistics",
            {
                "team": team_id,
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Top Scorers
    # ----------------------------------------

    def get_top_scorers(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "players/topscorers",
            {
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Top Assists
    # ----------------------------------------

    def get_top_assists(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "players/topassists",
            {
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Top Yellow Cards
    # ----------------------------------------

    def get_top_yellow_cards(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "players/topyellowcards",
            {
                "league": league,
                "season": season
            }
        )

    # ----------------------------------------
    # Top Red Cards
    # ----------------------------------------

    def get_top_red_cards(
        self,
        league=PREMIER_LEAGUE_ID,
        season=CURRENT_SEASON
    ):

        return self._get(
            "players/topredcards",
            {
                "league": league,
                "season": season
            }
        )