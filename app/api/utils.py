import math
import numpy as np


def serialize(data):

    if isinstance(data, dict):

        return {
            key: serialize(value)
            for key, value in data.items()
        }

    elif isinstance(data, list):

        return [
            serialize(item)
            for item in data
        ]

    elif isinstance(data, np.integer):

        return int(data)

    elif isinstance(data, np.floating):

        if math.isnan(data):
            return None

        return float(data)

    elif isinstance(data, np.bool_):

        return bool(data)

    return data

def dataframe_to_records(dataframe):

    records = (
        dataframe.astype(object)
        .where(dataframe.notna(), None)
        .to_dict(orient="records")
    )

    return serialize(records)