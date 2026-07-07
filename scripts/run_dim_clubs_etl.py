from app.etl.dim_clubs_etl import DimClubsETL


if __name__ == "__main__":

    etl = DimClubsETL()

    etl.run()