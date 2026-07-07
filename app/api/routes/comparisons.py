from fastapi import APIRouter, HTTPException

from app.api.utils import serialize, dataframe_to_records

from app.analytics.player_comparison import PlayerComparison
from app.analytics.club_comparison import ClubComparison
from app.analytics.season_comparison import SeasonComparison

router = APIRouter(
    prefix="/comparisons",
    tags=["Comparisons"]
)

player_comparison = PlayerComparison()
club_comparison = ClubComparison()
season_comparison = SeasonComparison()


# ---------------------------------------
# Player Comparison
# ---------------------------------------

@router.get("/player")
def compare_players(
    player1: str,
    player2: str,
    season: int | None = None
):

    comparison = player_comparison.compare_players(
        player1,
        player2,
        season
    )

    if comparison is None:
        raise HTTPException(
            status_code=404,
            detail="Player not found."
        )

    return dataframe_to_records(comparison)


# ---------------------------------------
# Club Comparison
# ---------------------------------------

@router.get("/club")
def compare_clubs(
    club1: str,
    club2: str,
    season: int | None = None
):

    comparison = club_comparison.compare_clubs(
        club1,
        club2,
        season
    )

    if comparison is None:
        raise HTTPException(
            status_code=404,
            detail="Club not found."
        )

    return dataframe_to_records(comparison)


# ---------------------------------------
# Season Comparison
# ---------------------------------------

@router.get("/season")
def compare_seasons(
    season1: int,
    season2: int
):

    comparison, first, second = season_comparison.compare(
        season1,
        season2
    )

    comparison = dataframe_to_records(comparison)

    return serialize({

        "comparison": comparison,

        "season1": first,

        "season2": second

    })