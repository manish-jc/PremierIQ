from app.analytics.player_profile import PlayerProfile


analytics = PlayerProfile()

print("\nCAREER PROFILE")
analytics.display(
    "Harry Kane"
)

print("\nSEASON PROFILE")
analytics.display(
    "Harry Kane",
    season=2022
)