from load_data import load_data

import pandas as pd
import numpy as np


def seven_day_window(df):
    # Select relevant columns
    df = df[['#Cases', '#Deaths', '#Recovered']]
    # Resample to sum over all values submitted in a day
    df = df.resample('D').sum()
    # Compute rolling sum over a 7-day window
    df = df.rolling(window=7).sum()
    # Shift the dateindex by one day
    df.index = df.index.shift(1, freq='D')
    return df


if __name__ == "__main__":

    df = load_data()
    weekly_window = seven_day_window(df)
    print(weekly_window)

