from app.analytics.player_search import PlayerSearch

search = PlayerSearch()

# ---------------------------------------
# Search by Name
# ---------------------------------------

print("\nSEARCH BY NAME\n")

search.display(
    name="Harry"
)

# ---------------------------------------
# Search by Club
# ---------------------------------------

print("\nSEARCH BY CLUB\n")

search.display(
    club="Liverpool FC"
)

# ---------------------------------------
# Search by Position
# ---------------------------------------

print("\nSEARCH BY POSITION\n")

search.display(
    position="Goalkeeper"
)

# ---------------------------------------
# Search by Nationality
# ---------------------------------------

print("\nSEARCH BY NATIONALITY\n")

search.display(
    nationality="England"
)

# ---------------------------------------
# Combined Search
# ---------------------------------------

print("\nCOMBINED SEARCH\n")

search.display(

    club="Manchester City",

    position="Goalkeeper"

)