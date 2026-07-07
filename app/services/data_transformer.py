class DataTransformer:

    @staticmethod
    def transform_player(player_data):

        player = player_data["player"]
        stats = player_data["statistics"][0]

        # Skip players with no appearances
        if stats["games"]["appearences"] is None:
            return None

        return {

            "name": player["name"],
            "firstname": player["firstname"],
            "lastname": player["lastname"],
            "age": player["age"],
            "nationality": player["nationality"],
            "height": player["height"],
            "weight": player["weight"],
            "photo": player["photo"],

            "club": stats["team"]["name"],
            "position": stats["games"]["position"],

            "appearances": stats["games"]["appearences"],
            "minutes": stats["games"]["minutes"],
            "rating": stats["games"]["rating"],

            "goals": stats["goals"]["total"],
            "assists": stats["goals"]["assists"],

            "shots": stats["shots"]["total"],
            "shots_on_target": stats["shots"]["on"],

            "passes": stats["passes"]["total"],
            "key_passes": stats["passes"]["key"],
            "pass_accuracy": stats["passes"]["accuracy"],

            "tackles": stats["tackles"]["total"],
            "interceptions": stats["tackles"]["interceptions"]

        }