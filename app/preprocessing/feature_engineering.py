import pandas as pd
import numpy as np


def create_birth_year(df):

    df["birth_year"] = df["date_of_birth"].dt.year

    return df


def create_age_group(df):

    conditions = [
        df["age"] < 21,
        df["age"].between(21, 24),
        df["age"].between(25, 30),
        df["age"].between(31, 35),
        df["age"] > 35
    ]

    labels = [
        "Youth",
        "Young",
        "Prime",
        "Experienced",
        "Veteran"
    ]

    df["age_group"] = np.select(
        conditions,
        labels,
        default="Unknown"
    )

    return df


def create_height_category(df):

    conditions = [
        df["height_cm"] < 170,
        df["height_cm"].between(170, 180),
        df["height_cm"].between(181, 190),
        df["height_cm"] > 190
    ]

    labels = [
        "Short",
        "Average",
        "Tall",
        "Very Tall"
    ]

    df["height_category"] = np.select(
        conditions,
        labels,
        default="Unknown"
    )

    return df


def create_market_value_million(df):

    df["market_value_million"] = (
        df["market_value_eur"] / 1_000_000
    )

    return df