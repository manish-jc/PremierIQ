from app.etl.dim_seasons_etl import DimSeasonsETL

if __name__ == "__main__":

    etl = DimSeasonsETL()

    etl.run()