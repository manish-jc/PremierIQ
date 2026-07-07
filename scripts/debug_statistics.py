import pandas as pd

df = pd.read_csv("warehouse/processed/player_statistics.csv")

# Find duplicate player-season combinations
duplicates = df[df.duplicated(subset=["season", "player"], keep=False)]

print(f"Duplicate player-season rows: {len(duplicates)}")

# Show a few examples
for player in duplicates["player"].unique()[:5]:

    print("\n" + "=" * 60)
    print(player)
    print("=" * 60)

    print(
        duplicates[
            duplicates["player"] == player
        ][
            ["season", "player", "club", "nationality"]
        ].head(10)
    )