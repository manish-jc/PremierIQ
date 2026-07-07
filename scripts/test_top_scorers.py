from app.analytics.top_scorers import TopScorers


analytics = TopScorers()

analytics.display()

analytics.display(season=2022)

analytics.display(
    club="Arsenal FC",
    limit=5
)