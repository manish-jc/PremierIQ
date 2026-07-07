from app.analytics.club_profile import ClubProfile

analytics = ClubProfile()

print("\nCAREER PROFILE")
analytics.display(
    "Liverpool FC"
)

print("\nSEASON PROFILE")
analytics.display(
    "Liverpool FC",
    season=2022
)