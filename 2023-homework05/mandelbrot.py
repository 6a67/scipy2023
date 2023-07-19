import matplotlib.pyplot as plt
import numpy as np

from helpers import mandelbrot


def main():
    visualize_mandelbrot()
    plt.tight_layout()
    plt.show()


def visualize_mandelbrot():
    """Visualizes the Mandelbrot Set in a rectangle spanning from (-1.5, 1.0) in the top left corner to (0.5, -1.0) in the bottom right corner."""

    fig, ax = plt.subplots()

    # Create the Mandelbrot boolean array using mandelbrot from helpers.py
    x, y, dx, dy = -1.5, 1.0, 2.0, -2.0
    mandel = mandelbrot(x, y, dx, dy)

    # Plot the Mandelbrot data with the colormap turbo
    ax.imshow(mandel, cmap="turbo")  # extent=(x, x + dx, y - dy, y)   :,(

    # Create an annotation that points out the Seahorse Valley
    # ax.annotate(
    #     "Seahorse Valley",
    #     xy=(-0.75, 2.1),
    #     xytext=(-1.2, 2.5),
    #     arrowprops=dict(facecolor="yellow"),
    #     color="yellow",
    # )

    ax.annotate(
        "Seahorse Valley",
        xy=(147, 170),
        xytext=(90, 230),
        arrowprops=dict(facecolor="yellow"),
        color="yellow",
    )

    # Turn off the unneeded axis of the plot
    ax.axis("off")

    return fig, ax


if __name__ == "__main__":
    main()
