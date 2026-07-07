from app.etl.fact_player_statistics_etl import FactPlayerStatisticsETL

if __name__ == "__main__":

    etl = FactPlayerStatisticsETL()

    etl.run()