import pandas as pd
import numpy as np


def most_common(df):
    # Group the data by Type 1 and Type 2, count the occurrences of each combination, and find the most common one
    common_combination = df.groupby(['Type 1', 'Type 2']).size().idxmax()

    # Filter the data for Pokémon with the most common type combination
    common_pokemon = df[(df['Type 1'] == common_combination[0]) & (df['Type 2'] == common_combination[1])]

    # Find the Pokémon with the highest attack value among the common type combination
    pokemon_with_highest_attack = common_pokemon.loc[common_pokemon['Attack'].idxmax(), 'Name']

    return pokemon_with_highest_attack

if __name__ == "__main__":

    # use this for your own testing!

    df = pd.read_csv('data/pokemon_no_duplicates.csv', index_col=0)
    name = most_common(df)
    print(name)
