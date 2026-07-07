from fastapi import APIRouter

from app.api.utils import serialize

from app.analytics.football_awards import FootballAwards

router = APIRouter(
    prefix="/awards",
    tags=["Awards"]
)

football_awards = FootballAwards()


@router.get("/")
def get_awards(
    season: int | None = None
):

    awards = football_awards.get_awards(
        season=season
    )

    return serialize(awards)