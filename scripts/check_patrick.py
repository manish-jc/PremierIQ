from app.services.warehouse import DataWarehouse

warehouse = DataWarehouse()

print("Players")
print(warehouse.get_dim_players().columns.tolist())

print()

print("Clubs")
print(warehouse.get_dim_clubs().columns.tolist())

print()

print(warehouse.get_dim_clubs().head())