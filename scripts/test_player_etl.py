from app.etl.player_etl import PlayerETL

etl = PlayerETL()

players = etl.extract_all_players()

print("\n")

print("Total Players:", len(players))

print()

print(players[0])