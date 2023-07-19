import matplotlib.pyplot as plt
import numpy as np
from data import freq_values, freq_names_type, freq_names_align


def main():
    fig, ax = make_heatmap()
    plt.tight_layout()
    plt.show()


def make_heatmap():
    """Plots heatmap of D&D creature type frequencies per alignment."""

    # Create a figure and Axes object
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the frequency data using imshow
    im = ax.imshow(
        freq_values.T, cmap="inferno"
    )  # Transpose freq_values to swap the axes

    # Set the necessary labels and title for the Axes object
    ax.set_xticks(np.arange(len(freq_names_align)))  # Use freq_names_align for x-axis
    ax.set_yticks(np.arange(len(freq_names_type)))  # Use freq_names_type for y-axis
    ax.set_xticklabels(
        freq_names_align, rotation=90
    )  # Use freq_names_align for x-axis labels and rotate them by 90 degrees
    ax.set_yticklabels(freq_names_type)  # Use freq_names_type for y-axis labels
    ax.set_xlabel("Alignment")  # Swap the x-axis label to 'Alignment'
    ax.set_ylabel("Creature Type")  # Swap the y-axis label to 'Creature Type'
    ax.set_title("Creature Type Frequencies per Alignment")

    # Create a colorbar on the right side of the plot
    cbar = ax.figure.colorbar(im, ax=ax, aspect=30, pad=0.02)
    cbar.set_label("Frequency")

    # Adjust the position of ticks and labels
    ax.xaxis.tick_bottom()

    return fig, ax


if __name__ == "__main__":
    main()
