from fastapi import APIRouter

from app.api.utils import dataframe_to_records
from app.analytics.top_scorers import TopScorers
from app.analytics.top_assists import TopAssists
from app.analytics.goalkeeper_rankings import GoalkeeperRankings
from app.analytics.club_rankings import ClubRankings

router = APIRouter(
    prefix="/rankings",
    tags=["Rankings"]
)

top_scorers = TopScorers()
top_assists = TopAssists()
goalkeepers = GoalkeeperRankings()
club_rankings = ClubRankings()


# ---------------------------------------
# Top Scorers
# ---------------------------------------

@router.get("/top-scorers")
def get_top_scorers(
    season: int | None = None,
    limit: int = 10
):

    results = top_scorers.get_top_scorers(
        season=season,
        limit=limit
    )

    return dataframe_to_records(results)


# ---------------------------------------
# Top Assists
# ---------------------------------------

@router.get("/top-assists")
def get_top_assists(
    season: int | None = None,
    limit: int = 10
):

    results = top_assists.get_top_assists(
        season=season,
        limit=limit
    )

    return dataframe_to_records(results)


# ---------------------------------------
# Goalkeeper Rankings
# ---------------------------------------

@router.get("/goalkeepers")
def get_goalkeepers(
    season: int | None = None,
    limit: int = 10
):

    results = goalkeepers.get_top_goalkeepers(
        season=season,
        limit=limit
    )

    return dataframe_to_records(results)


# ---------------------------------------
# Club Rankings
# ---------------------------------------

@router.get("/clubs")
def get_club_rankings(
    season: int | None = None,
    limit: int = 10
):

    results = club_rankings.get_club_rankings(
        season=season,
        limit=limit
    )

    return dataframe_to_records(results)