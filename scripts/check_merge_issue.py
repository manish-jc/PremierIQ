import pandas as pd

df = pd.read_csv(
    "warehouse/processed/player_statistics.csv",
    low_memory=False
)

counts = (
    df.groupby(["season", "player"])
      .size()
      .reset_index(name="count")
)

print("Player-season combinations with more than one row:\n")

print(
    counts[counts["count"] > 1]
        .sort_values("count", ascending=False)
        .head(20)
)