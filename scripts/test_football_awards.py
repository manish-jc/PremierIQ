from app.analytics.football_awards import FootballAwards

awards = FootballAwards()

print("\nALL-TIME AWARDS")
awards.display()

print("\n2022 AWARDS")
awards.display(
    season=2022
)