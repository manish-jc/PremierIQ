from app.analytics.top_assists import TopAssists


analytics = TopAssists()

analytics.display()

analytics.display(
    season=2022
)

analytics.display(
    club="Arsenal FC",
    limit=5
)