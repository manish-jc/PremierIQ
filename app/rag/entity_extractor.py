from app.services.warehouse import DataWarehouse


class EntityExtractor:

    def __init__(self):

        warehouse = DataWarehouse()

        self.players = warehouse.get_dim_players()
        self.clubs = warehouse.get_dim_clubs()

        # ---------------------------------------
        # Club Aliases
        # ---------------------------------------

        self.club_aliases = {

            "arsenal": "Arsenal FC",
            "aston villa": "Aston Villa",
            "bournemouth": "AFC Bournemouth",
            "brentford": "Brentford FC",
            "brighton": "Brighton & Hove Albion",
            "brighton and hove albion": "Brighton & Hove Albion",
            "burnley": "Burnley FC",
            "chelsea": "Chelsea FC",
            "crystal palace": "Crystal Palace",
            "everton": "Everton FC",
            "fulham": "Fulham FC",
            "ipswich": "Ipswich Town",
            "leicester": "Leicester City",
            "liverpool": "Liverpool FC",
            "man city": "Manchester City",
            "manchester city": "Manchester City",
            "city": "Manchester City",
            "man united": "Manchester United",
            "manchester united": "Manchester United",
            "united": "Manchester United",
            "newcastle": "Newcastle United",
            "newcastle united": "Newcastle United",
            "forest": "Nottingham Forest",
            "nottingham": "Nottingham Forest",
            "southampton": "Southampton FC",
            "spurs": "Tottenham Hotspur",
            "tottenham": "Tottenham Hotspur",
            "tottenham hotspur": "Tottenham Hotspur",
            "west ham": "West Ham United",
            "west ham united": "West Ham United",
            "wolves": "Wolverhampton Wanderers",
            "wolverhampton": "Wolverhampton Wanderers"

        }

    # ---------------------------------------
    # Find Players
    # ---------------------------------------

    def find_players(self, question):

        question = question.lower().strip()

        full_name_matches = []
        surname_matches = []

        for player in self.players["player_name"]:

            if not isinstance(player, str):
                continue

            full_name = player.lower().strip()

            # Exact full-name match (highest priority)
            if full_name in question:

                full_name_matches.append(player)

                continue

            # Surname match
            surname = full_name.split()[-1]

            if len(surname) >= 4 and surname in question:

                surname_matches.append(player)

        # Prefer exact full-name matches
        if full_name_matches:

            return list(dict.fromkeys(full_name_matches))

        return list(dict.fromkeys(surname_matches))

    # ---------------------------------------
    # Find Clubs
    # ---------------------------------------

    def find_clubs(self, question):

        question = question.lower()

        matches = []

        for club in self.clubs["club_name"]:

            if not isinstance(club, str):
                continue

            if club.lower() in question:
                matches.append(club)

        for alias, club in self.club_aliases.items():

            if alias in question:
                matches.append(club)

        return list(dict.fromkeys(matches))

    # ---------------------------------------
    # Find Season
    # ---------------------------------------

    def find_season(self, question):

        words = question.split()

        for word in words:

            if word.isdigit():

                year = int(word)

                if 1992 <= year <= 2030:

                    return year

        return None