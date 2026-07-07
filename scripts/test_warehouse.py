from app.services.warehouse import DataWarehouse


warehouse = DataWarehouse()

print()

print("Fact Table")

print(
    warehouse.get_fact_player_statistics().shape
)

print()

print("Players")

print(
    warehouse.get_dim_players().shape
)

print()

print("Clubs")

print(
    warehouse.get_dim_clubs().shape
)

print()

print("Seasons")

print(
    warehouse.get_dim_seasons().shape
)