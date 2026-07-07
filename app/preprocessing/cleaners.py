import ast
import pandas as pd
import numpy as np


def clean_height(height):

    if pd.isna(height):
        return np.nan

    height = str(height)

    height = height.replace("m", "")
    height = height.replace(",", ".")

    try:
        return int(float(height) * 100)
    except:
        return np.nan


def clean_nationality(value):

    if pd.isna(value):
        return ""

    try:
        countries = ast.literal_eval(value)

        if isinstance(countries, list):
            return "; ".join(countries)

        return str(countries)

    except:
        return str(value)


def clean_date(value):

    if pd.isna(value):
        return pd.NaT

    return pd.to_datetime(
        value,
        errors="coerce"
    )


def clean_market_value(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace("€", "")
    value = value.replace(",", ".")

    try:

        if value.endswith("m"):
            return int(float(value[:-1]) * 1_000_000)

        if value.endswith("k"):
            return int(float(value[:-1]) * 1_000)

        return np.nan

    except:
        return np.nan
    

import re


def clean_numeric(value):

    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace(",", "")
    value = value.strip()

    try:
        return float(value)
    except:
        return np.nan


def clean_player_name(name):

    if pd.isna(name):
        return ""

    name = str(name)

    # Remove weird symbols
    name = re.sub(r"[@*#]", "", name)

    # Remove multiple spaces
    name = re.sub(r"\s+", " ", name)

    return name.strip()


def clean_club_name(club):

    if pd.isna(club):
        return np.nan

    club = str(club).strip()

    if club == "-":
        return np.nan

    return club