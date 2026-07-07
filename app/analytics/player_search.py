from app.services.warehouse import DataWarehouse


class PlayerSearch:

    def __init__(self):

        warehouse = DataWarehouse()

        self.df = warehouse.get_fact_player_statistics()

    # ---------------------------------------
    # Search Players
    # ---------------------------------------

    def search(
        self,
        name=None,
        club=None,
        position=None,
        nationality=None
    ):

        dataframe = self.df.copy()

        # -----------------------------
        # Name
        # -----------------------------

        if name:

            dataframe = dataframe[

                dataframe["player"]

                .str.contains(

                    name,

                    case=False,

                    na=False

                )

            ]

        # -----------------------------
        # Club
        # -----------------------------

        if club:

            dataframe = dataframe[

                dataframe["club"]

                .str.lower()

                ==

                club.lower()

            ]

        # -----------------------------
        # Position
        # -----------------------------

        if position:

            dataframe = dataframe[

                dataframe["position"]

                .str.lower()

                ==

                position.lower()

            ]

        # -----------------------------
        # Nationality
        # -----------------------------

        if nationality:

            dataframe = dataframe[

                dataframe["nationality"]

                .str.lower()

                ==

                nationality.lower()

            ]

        # ---------------------------------------
        # Remove duplicates
        # ---------------------------------------

        dataframe = dataframe.drop_duplicates(

            subset=[

                "player",

                "club",

                "season"

            ]

        )

        dataframe = dataframe.sort_values(

            by=[

                "player",

                "season"

            ]

        )

        return dataframe[
            [

                "player",

                "club",

                "season",

                "position",

                "nationality"

            ]

        ].reset_index(drop=True)
    

    # ---------------------------------------
    # Display
    # ---------------------------------------

    def display(
        self,
        name=None,
        club=None,
        position=None,
        nationality=None
    ):

        results = self.search(

            name=name,

            club=club,

            position=position,

            nationality=nationality

        )

        print()

        print("=" * 70)

        print("PLAYER SEARCH RESULTS")

        print("=" * 70)

        print(f"Total Players Found : {len(results)}")

        print()

        if results.empty:

            print("No players found.")

            return

        print(results)