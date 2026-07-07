import pandas as pd

profiles = pd.read_csv(
    "warehouse/processed/player_profiles.csv",
    low_memory=False
)

stats = pd.read_csv(
    "warehouse/processed/player_statistics.csv",
    low_memory=False
)

profiles["join_name"] = (
    profiles["name"]
    .astype(str)
    .str.strip()
    .str.lower()
)

stats["join_name"] = (
    stats["player"]
    .astype(str)
    .str.strip()
    .str.lower()
)

merged = stats.merge(
    profiles[
        [
            "player_id",
            "join_name",
            "season",
            "club",
            "position"
        ]
    ],
    on=["join_name", "season"],
    how="left"
)

print("=" * 50)
print("JOIN REPORT")
print("=" * 50)

print(f"Statistics rows : {len(stats)}")
print(f"Matched rows    : {merged['player_id'].notna().sum()}")
print(f"Unmatched rows  : {merged['player_id'].isna().sum()}")

print("\nMatch Percentage:")
print(
    round(
        merged["player_id"].notna().mean() * 100,
        2
    ),
    "%"
)