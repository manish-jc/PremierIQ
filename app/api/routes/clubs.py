from fastapi import APIRouter

from app.api.utils import serialize

from app.services.warehouse import DataWarehouse
from app.analytics.club_profile import ClubProfile

router = APIRouter(
    prefix="/clubs",
    tags=["Clubs"]
)

warehouse = DataWarehouse()

club_profile = ClubProfile()


@router.get("/")
def get_clubs():

    clubs = warehouse.get_dim_clubs()

    records = (
        clubs.astype(object)
        .where(clubs.notna(), None)
        .to_dict(orient="records")
    )

    return records


@router.get("/profile/{club_name}")
def get_club_profile(
    club_name: str,
    season: int | None = None
):

    profile = club_profile.get_club_profile(
        club_name,
        season
    )

    return serialize(profile)