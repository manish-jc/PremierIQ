from app.rag.entity_extractor import EntityExtractor

extractor = EntityExtractor()

while True:

    question = input("\nQuestion: ")

    print()

    print("Players :", extractor.find_players(question))

    print("Clubs   :", extractor.find_clubs(question))

    print("Season  :", extractor.find_season(question))