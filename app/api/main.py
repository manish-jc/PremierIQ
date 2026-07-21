from fastapi import FastAPI
from app.api.routes import chat
from app.api.routes.players import router as players_router
from app.api.routes.clubs import router as clubs_router
from app.api.routes.rankings import router as rankings_router
from app.api.routes.comparisons import router as comparisons_router
from app.api.routes.seasons import router as seasons_router
from app.api.routes.awards import router as awards_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

    title="PremierIQ API",

    description="""
PremierIQ is a Premier League Analytics and AI platform.

## Features

- Player Analytics
- Club Analytics
- Rankings
- Season Summaries
- Football Awards
- Comparisons
- AI Chat (Coming Soon)
""",

    version="1.0.0"

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------------
# Routers
# ---------------------------------------

app.include_router(players_router)

app.include_router(clubs_router)

app.include_router(rankings_router)

app.include_router(comparisons_router)

app.include_router(seasons_router)

app.include_router(awards_router)

app.include_router(chat.router)


@app.get("/")

def home():

    return {

        "application": "PremierIQ",

        "version": "1.0.0",

        "status": "Running"

    }


@app.get("/", tags=["Home"])
def home():

    return {

        "application": "PremierIQ",

        "version": "1.0.0",

        "status": "Running"

    }