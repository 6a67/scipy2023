from pandas.api.types import CategoricalDtype

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def to_categorical(series):
    # Replace the unknown values with NaN
    series = series.replace("unbekannt", np.nan)

    # Define the categories
    categories = ["A00-A04", "A05-A14", "A15-A34", "A35-A59", "A60-A79", "A80+"]

    # Define the data type
    cat_type = CategoricalDtype(categories=categories, ordered=True)

    # Convert the series to categorical
    cat_series = series.astype(cat_type)

    return cat_series


if __name__ == "__main__":

    df = pd.read_csv("data/RKI_COVID.csv", usecols=["AgeGroup"])
    ser = to_categorical(df["AgeGroup"])
    print(ser)
