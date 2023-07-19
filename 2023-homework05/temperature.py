import matplotlib.pyplot as plt
import numpy as np


def main():
    df = np.load("data/full_temperature.npy", allow_pickle=True)
    plot_temperature(df)
    plt.tight_layout()
    plt.show()


def plot_temperature(data):
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # First subplot: Monthly temperatures for selected years
    years = [1990, 2005, 2020]
    months = np.arange(1, 13)
    labels = ["1990", "2005", "2020"]

    for i, year in enumerate(years):
        temperatures = data[year - 1990]  # Adjust index for the year
        ax1.plot(months, temperatures, label=labels[i])

    ax1.set_title("Average temperature of selected years")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Temperature in C")
    ax1.legend()

    # Second subplot: Average temperatures and yearly variation for each year
    mean_temperatures = np.mean(data, axis=1)
    min_temperatures = np.min(data, axis=1)
    max_temperatures = np.max(data, axis=1)
    years = np.arange(1990, 2022)

    ax2.plot(years, mean_temperatures, label="Mean temperature")
    ax2.fill_between(years, min_temperatures, max_temperatures, alpha=0.3)
    ax2.annotate(
        "Mean temperature",
        xy=(2000, mean_temperatures[10]),
        xytext=(2000 + 3, mean_temperatures[10] + 3),
        arrowprops=dict(facecolor="black", arrowstyle="-|>"),
    )
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Temperature in C")
    ax2.set_title("Average temperatures and yearly variation over the years 1990-2021")

    # Super-title
    fig.suptitle("Temperature data for Muenster/Osnabrueck (1990-2021)", fontsize=16)

    return fig, ax1, ax2


if __name__ == "__main__":
    main()
