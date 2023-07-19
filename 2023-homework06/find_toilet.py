import numpy as np
import pandas as pd


def find_closest_toilet(lat, lon):
    """ Returns Series with properties of suitable public toilet nearest to given coordinates. """
    
    # Load data
    df = pd.read_csv("data/australian_toilets.csv")

    # Filter only toilets with drinkable water and baby care facilities
    df = df[(df["DrinkingWater"]) & (df["BabyChange"])]

    # Convert coordinates to radians, point1
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)

    # Calculate offsets to point2
    dlat = df["Latitude"].apply(lambda x: np.radians(x) - lat_rad)
    dlon = df["Longitude"].apply(lambda x: np.radians(x) - lon_rad)
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat_rad) * np.cos(np.radians(df["Latitude"])) * np.sin(dlon / 2) ** 2
    )
    c = 2 * np.arcsin(np.sqrt(a))
    distance = 6371 * c  # Radius of the Earth is 6371 km

    # Find the index of the closest toilet
    closest_index = distance.idxmin()

    # Extract the relevant information for the closest toilet
    closest_toilet = df.loc[closest_index, ["FacilityID", "Name", "Longitude", "Latitude"]]
    closest_toilet["distance"] = distance[closest_index]

    # rename columns of series
    closest_toilet.rename(
        index={
            "Name": "name",
            "Longitude": "longitude",
            "Latitude": "latitude",
        },
        inplace=True,
    )


    return closest_toilet

if __name__ == "__main__":

    # use this for your own testing!

    lat, lon = -26.834666, 129.139510
    result = find_closest_toilet(lat, lon)

    print(result)

