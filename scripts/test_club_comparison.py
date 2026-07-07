from app.analytics.club_comparison import ClubComparison

comparison = ClubComparison()

comparison.display(

    "Liverpool FC",

    "Manchester City"

)

print()

comparison.display(

    "Liverpool FC",

    "Manchester City",

    season=2022

)