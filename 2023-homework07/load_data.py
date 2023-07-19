import pandas as pd
import numpy as np


def load_data():
    # Load the two datasets
    covid_df = pd.read_csv('data/RKI_COVID.csv', parse_dates=['ReportingDate'])
    counties_df = pd.read_csv('data/RKI_Counties.csv')

    # Rename the RS column to IdCounty
    counties_df = counties_df.rename(columns={'RS': 'IdCounty'})

    # Perform left outer join on the two datasets
    merged_df = pd.merge(covid_df, counties_df, on='IdCounty', how='left')

    # Set the index to ReportingDate, sort the index and drop AgeGroup2 column
    merged_df = merged_df.set_index('ReportingDate').sort_index().drop(columns=['AgeGroup2'])

    merged_df = merged_df.loc[:, ['AgeGroup', 'Sex', '#Cases', '#Deaths', 'IdCounty', '#Recovered', 'county']]

    return merged_df


if __name__ == "__main__":

    df = load_data()
    print(df)
