def validate_player_profiles(df):

    print("\n==============================")
    print("PLAYER PROFILE DATASET REPORT")
    print("==============================")

    print(f"Rows               : {len(df)}")
    print(f"Columns            : {len(df.columns)}")
    print(f"Duplicate Rows     : {df.duplicated().sum()}")
    print(f"Missing Names      : {df['name'].isna().sum()}")
    print(f"Missing IDs        : {df['player_id'].isna().sum()}")
    print(f"Missing Clubs      : {df['club'].isna().sum()}")
    print(f"Missing Seasons    : {df['season'].isna().sum()}")

    print("==============================\n")


def validate_player_statistics(df):

    print("\n==============================")
    print("PLAYER STATISTICS REPORT")
    print("==============================")

    print(f"Rows               : {len(df)}")
    print(f"Columns            : {len(df.columns)}")
    print(f"Duplicate Rows     : {df.duplicated().sum()}")
    print(f"Missing Players    : {df['player'].isna().sum()}")
    print(f"Missing Seasons    : {df['season'].isna().sum()}")

    print("==============================\n")