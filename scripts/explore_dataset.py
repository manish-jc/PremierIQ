from pathlib import Path

base_path = Path("warehouse/raw/squad_profiles/DATA_CSV")

print("=" * 60)
print("PremierIQ Dataset Explorer")
print("=" * 60)

season_folders = sorted(base_path.iterdir())

print(f"\nTotal Seasons: {len(season_folders)}")

for season in season_folders[:3]:

    print(f"\n{season.name}")

    files = list(season.glob("*.csv"))

    print(f"Files: {len(files)}")

    for file in files[:5]:
        print("   ", file.name)