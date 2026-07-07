from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.analytics.player_search import PlayerSearch
from app.services.warehouse import DataWarehouse
from app.analytics.player_profile import PlayerProfile
from app.api.utils import serialize, dataframe_to_records

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)

warehouse = DataWarehouse()
player_search = PlayerSearch()
player_profile = PlayerProfile()

@router.get("/")
def get_players():

    players = warehouse.get_dim_players()

    # Convert NaN -> None
    records = (
        players.astype(object)
        .where(players.notna(), None)
        .to_dict(orient="records")
    )

    return jsonable_encoder(records)


@router.get("/search")
def search_players(

    name: str | None = None,
    club: str | None = None,
    position: str | None = None,
    nationality: str | None = None

):

    results = player_search.search(

        name=name,
        club=club,
        position=position,
        nationality=nationality

    )

    return dataframe_to_records(results)