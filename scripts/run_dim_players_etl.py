from app.etl.dim_players_etl import DimPlayersETL

if __name__ == "__main__":

    etl = DimPlayersETL()

    etl.run()