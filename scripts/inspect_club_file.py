from pathlib import Path
import pandas as pd

season_path = Path("warehouse/raw/squad_profiles/DATA_CSV/Season_2024")

# Get the first CSV file automatically
csv_file = sorted(season_path.glob("*.csv"))[0]

print(f"Reading: {csv_file.name}\n")

df = pd.read_csv(csv_file)

print("=" * 60)
print("First 5 Rows")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("Columns")
print("=" * 60)
print(df.columns.tolist())

print("\n" + "=" * 60)
print("Shape")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("Data Types")
print("=" * 60)
print(df.dtypes)