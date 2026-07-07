import pandas as pd

FILE = "warehouse/raw/player_statistics/Red Cards.csv"
PLAYER = "Wilfried Zaha"

df = pd.read_csv(FILE)

player_df = df[df["Player"] == PLAYER]

print("=" * 80)
print(player_df)
print("=" * 80)

print("\nDuplicate Groups:\n")

print(
    player_df.groupby(
        [
            "Initial Year",
            "Player",
            "Club",
            "Nationality",
            "Stat"
        ]
    ).size()
)