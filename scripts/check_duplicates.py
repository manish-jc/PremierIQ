from pathlib import Path
import pandas as pd

stats_path = Path("warehouse/raw/player_statistics")

for csv_file in sorted(stats_path.glob("*.csv")):

    df = pd.read_csv(csv_file)

    duplicates = df.duplicated(
        subset=["Initial Year", "Player"],
        keep=False
    ).sum()

    if duplicates > 0:
        print(f"{csv_file.name} -> {duplicates} duplicate rows")
