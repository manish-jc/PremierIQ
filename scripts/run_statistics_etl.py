from app.etl.statistics_etl import PlayerStatisticsETL

if __name__ == "__main__":

    etl = PlayerStatisticsETL()

    etl.run()