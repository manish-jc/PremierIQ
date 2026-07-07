from pathlib import Path
import pandas as pd

stats_path = Path("warehouse/raw/player_statistics")

csv_files = sorted(stats_path.glob("*.csv"))

print("=" * 60)
print("PLAYER STATISTICS DATASET")
print("=" * 60)

print(f"\nTotal CSV Files : {len(csv_files)}\n")

for csv_file in csv_files:

    print("-" * 60)

    print(f"File : {csv_file.name}")

    df = pd.read_csv(csv_file)

    print(f"Rows : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    print("Column Names:")

    print(df.columns.tolist())

    print("\nFirst 3 Rows:\n")

    print(df.head(3))

    print("\n")