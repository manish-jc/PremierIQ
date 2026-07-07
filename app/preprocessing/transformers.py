from app.preprocessing.cleaners import *
from app.preprocessing.feature_engineering import *


def transform_player_profiles(df):

    df = df.copy()

    df.rename(
        columns={
            "id": "player_id",
            "foot": "preferred_foot",
            "joinedon": "joined_on",
            "dateofbirth": "date_of_birth",
            "signedfrom": "signed_from",
            "marketvalue": "market_value"
        },
        inplace=True
    )

    df["height_cm"] = df["height"].apply(clean_height)

    df["nationality"] = df["nationality"].apply(
        clean_nationality
    )

    df["joined_on"] = df["joined_on"].apply(clean_date)

    df["date_of_birth"] = df["date_of_birth"].apply(clean_date)

    df["market_value_eur"] = df["market_value"].apply(
        clean_market_value
    )

    # -------------------------------
    # Feature Engineering
    # -------------------------------

    df = create_birth_year(df)

    df = create_age_group(df)

    df = create_height_category(df)

    df = create_market_value_million(df)

    # -------------------------------
    # Drop old columns
    # -------------------------------

    df.drop(
        columns=[
            "height",
            "market_value",
            "joined",
            "currentclub"
        ],
        errors="ignore",
        inplace=True
    )

    # -------------------------------
    # Remove duplicate rows
    # -------------------------------

    df.drop_duplicates(inplace=True)

    # -------------------------------
    # Reorder Columns
    # -------------------------------

    final_columns = [

        "player_id",

        "name",

        "season",

        "club",

        "position",

        "preferred_foot",

        "nationality",

        "age",

        "age_group",

        "birth_year",

        "date_of_birth",

        "height_cm",

        "height_category",

        "market_value_eur",

        "market_value_million",

        "signed_from",

        "joined_on",

        "contract",

        "status"
    ]

    existing_columns = [
        column
        for column in final_columns
        if column in df.columns
    ]

    df = df[existing_columns]

    return df

def transform_player_statistics(df):

    df = df.copy()

    df["player"] = df["player"].apply(
        clean_player_name
    )

    df["club"] = df["club"].apply(
        clean_club_name
    )

    stat_columns = [

        column

        for column in df.columns

        if column not in [

            "season",

            "player",

            "club",

            "nationality"

        ]

    ]

    for column in stat_columns:

        df[column] = df[column].apply(
            clean_numeric
        )

    return df