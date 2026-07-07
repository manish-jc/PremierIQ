from app.analytics.player_profile import PlayerProfile
from app.analytics.club_profile import ClubProfile
from app.analytics.top_scorers import TopScorers
from app.analytics.top_assists import TopAssists
from app.analytics.goalkeeper_rankings import GoalkeeperRankings
from app.analytics.club_rankings import ClubRankings
from app.analytics.player_comparison import PlayerComparison
from app.analytics.club_comparison import ClubComparison
from app.analytics.season_summary import SeasonSummary
from app.analytics.football_awards import FootballAwards


class ContextBuilder:

    def __init__(self):

        self.player_profile = PlayerProfile()
        self.club_profile = ClubProfile()

        self.top_scorers = TopScorers()
        self.top_assists = TopAssists()
        self.goalkeepers = GoalkeeperRankings()
        self.club_rankings = ClubRankings()

        self.player_comparison = PlayerComparison()
        self.club_comparison = ClubComparison()

        self.season_summary = SeasonSummary()
        self.awards = FootballAwards()

    # ---------------------------------------
    # Build Context
    # ---------------------------------------

    def build(
        self,
        route_info,
        extractor,
        question
    ):

        route = route_info["route"]

        season = extractor.find_season(question)

        # =====================================
        # PROFILE
        # =====================================

        if route == "profile":

            players = extractor.find_players(question)

            if len(players) == 1:

                return self.player_profile.get_player_profile(
                    players[0],
                    season
                )

            clubs = extractor.find_clubs(question)

            if len(clubs) == 1:

                return self.club_profile.get_club_profile(
                    clubs[0],
                    season
                )

            return None

        # =====================================
        # RANKINGS
        # =====================================

        elif route == "rankings":

            ranking_type = route_info["type"]

            if ranking_type == "top_scorers":

                return self.top_scorers.get_top_scorers(
                    season=season
                )

            elif ranking_type == "top_assists":

                return self.top_assists.get_top_assists(
                    season=season
                )

            elif ranking_type == "goalkeepers":

                return self.goalkeepers.get_top_goalkeepers(
                    season=season
                )

            elif ranking_type == "clubs":

                return self.club_rankings.get_club_rankings(
                    season=season
                )

        # =====================================
        # AWARDS
        # =====================================

        elif route == "awards":

            return self.awards.get_awards(
                season
            )

        # =====================================
        # SEASON
        # =====================================

        elif route == "season":

            if season is not None:

                return self.season_summary.get_season_summary(
                    season
                )

        # =====================================
        # COMPARISON
        # =====================================

        elif route == "comparison":

            players = extractor.find_players(question)

            if len(players) == 2:

                return self.player_comparison.compare_players(
                    players[0],
                    players[1],
                    season
                )

            clubs = extractor.find_clubs(question)

            if len(clubs) == 2:

                return self.club_comparison.compare_clubs(
                    clubs[0],
                    clubs[1],
                    season
                )

        # =====================================
        # KNOWLEDGE
        # =====================================

        return None