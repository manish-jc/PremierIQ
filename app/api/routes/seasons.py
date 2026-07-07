from fastapi import APIRouter

from app.api.utils import serialize
from app.analytics.season_summary import SeasonSummary

router = APIRouter(
    prefix="/seasons",
    tags=["Seasons"]
)

season_summary = SeasonSummary()


@router.get("/{season}")
def get_season_summary(
    season: int
):

    summary = season_summary.get_season_summary(
        season
    )

    return serialize(summary)