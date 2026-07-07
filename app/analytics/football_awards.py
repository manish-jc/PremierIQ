from app.analytics.top_scorers import TopScorers
from app.analytics.top_assists import TopAssists
from app.analytics.goalkeeper_rankings import GoalkeeperRankings
from app.analytics.club_rankings import ClubRankings


class FootballAwards:

    def __init__(self):

        self.scorers = TopScorers()

        self.assists = TopAssists()

        self.goalkeepers = GoalkeeperRankings()

        self.clubs = ClubRankings()

    # ---------------------------------------
    # Golden Boot
    # ---------------------------------------

    def get_golden_boot(
        self,
        season=None
    ):

        winner = self.scorers.get_top_scorers(
            season=season,
            limit=1
        ).iloc[0]

        return {

            "player": winner["player"],

            "club": winner["club"],

            "goals": int(winner["goals"])

        }

    # ---------------------------------------
    # Playmaker Award
    # ---------------------------------------

    def get_playmaker(
        self,
        season=None
    ):

        winner = self.assists.get_top_assists(
            season=season,
            limit=1
        ).iloc[0]

        return {

            "player": winner["player"],

            "club": winner["club"],

            "assists": int(winner["assists"])

        }

    # ---------------------------------------
    # Golden Glove
    # ---------------------------------------

    def get_golden_glove(
        self,
        season=None
    ):

        winner = self.goalkeepers.get_top_goalkeepers(
            season=season,
            limit=1
        ).iloc[0]

        return {

            "player": winner["player"],

            "club": winner["club"],

            "clean_sheets": int(winner["clean_sheets"])

        }

    # ---------------------------------------
    # Best Club
    # ---------------------------------------

    def get_best_club(
        self,
        season=None
    ):

        winner = self.clubs.get_club_rankings(
            season=season,
            limit=1
        ).iloc[0]

        return {

            "club": winner["club"],

            "score": round(

                winner["club_score"],

                2

            )

        }
    

    # ---------------------------------------
    # All Awards
    # ---------------------------------------

    def get_awards(
        self,
        season=None
    ):

        awards = {

            "golden_boot":

                self.get_golden_boot(
                    season
                ),

            "playmaker":

                self.get_playmaker(
                    season
                ),

            "golden_glove":

                self.get_golden_glove(
                    season
                ),

            "best_club":

                self.get_best_club(
                    season
                )

        }

        return awards

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        season=None
    ):

        awards = self.get_awards(
            season
        )

        print()

        print("=" * 70)

        if season is None:

            print("PREMIER LEAGUE ALL-TIME AWARDS")

        else:

            print(f"PREMIER LEAGUE AWARDS ({season})")

        print("=" * 70)

        print()

        print("GOLDEN BOOT")
        print("-" * 70)

        print(
            f"Winner : {awards['golden_boot']['player']}"
        )

        print(
            f"Club   : {awards['golden_boot']['club']}"
        )

        print(
            f"Goals  : {awards['golden_boot']['goals']}"
        )

        print()

        print("PLAYMAKER AWARD")
        print("-" * 70)

        print(
            f"Winner  : {awards['playmaker']['player']}"
        )

        print(
            f"Club    : {awards['playmaker']['club']}"
        )

        print(
            f"Assists : {awards['playmaker']['assists']}"
        )

        print()

        print("GOLDEN GLOVE")
        print("-" * 70)

        print(
            f"Winner         : {awards['golden_glove']['player']}"
        )

        print(
            f"Club           : {awards['golden_glove']['club']}"
        )

        print(
            f"Clean Sheets   : {awards['golden_glove']['clean_sheets']}"
        )

        print()

        print("BEST CLUB")
        print("-" * 70)

        print(
            f"Club  : {awards['best_club']['club']}"
        )

        print(
            f"Score : {awards['best_club']['score']}"
        )

        print()

        print("=" * 70)