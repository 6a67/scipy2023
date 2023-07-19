import pandas as pd
import numpy as np


def aggregate_european_countries():
    # Read the countries.csv file into a DataFrame
    df = pd.read_csv("data/countries.csv")

    # Filter the DataFrame to include only European countries
    european_countries = df[df["Subcontinent"].str.contains("Europe")]

    # Group by in EU
    european_countries_grouped = european_countries.groupby("In EU")

    # Find max net migration with given country in EU and not in EU
    european_countries_agg = european_countries_grouped.agg(
        {
            "Net migration": [
                "max",
                lambda x: european_countries.loc[x.idxmax(), "Country"],
            ],
            "Pop. Density": [
                "min",
                lambda x: european_countries.loc[x.idxmin(), "Country"],
            ],
        }
    )

    # Rename columns
    european_countries_agg.columns = [
        "max net migration",
        "max net migration country",
        "min pop density",
        "min pop density country",
    ]
    european_countries_agg.index = [
        "False",
        "True",
    ]  # Convert index to string for 'in eu' column

    # Reset index and convert it to a column
    # european_countries_agg.reset_index(inplace=True)

    # Rename 'In EU' column to 'in eu'
    # european_countries_agg.rename(columns={"In EU": "in eu"}, inplace=True)

    # Return the result
    return european_countries_agg


if __name__ == "__main__":
    # use this for your own testing!

    agg_df = aggregate_european_countries()
    print(agg_df)
