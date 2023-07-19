import pandas as pd

df = pd.read_csv("data/dnd_monsters.csv")
# Count the frequencies.
freqs_dataframe = df.groupby(["type", "align"])["name"].count().unstack(fill_value=0)

# Filter to only include the top 10 categories in 'type' and 'align' by frequency.
top_types = freqs_dataframe.sum(axis=1).nlargest(10).index
top_aligns = freqs_dataframe.sum(axis=0).nlargest(10).index
freqs_dataframe = freqs_dataframe.loc[top_types, top_aligns]

# Convert to numpy array and list of names for plotting.
freq_values = freqs_dataframe.values
freq_names_type = list(freqs_dataframe.index)
freq_names_align = list(freqs_dataframe.columns)
