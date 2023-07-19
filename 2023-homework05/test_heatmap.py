from helpers import imports_of_your_file

import pandas as pd
import numpy as np
import matplotlib
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from data import freq_values, freq_names_type, freq_names_align

try:

    import heatmap as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'heatmap.py'!"

def test_make_heatmap(filename="heatmap", allowed_imports={"numpy", "pandas", "matplotlib.pyplot", "heatmap"}):
    """ Checks whether returned heatmap has the correct attributes. """
    try:
        fig, ax = testfile.make_heatmap()

        # general checks
        assert isinstance(fig, Figure), "The first returned variable should be a Figure!"
        assert isinstance(ax, Axes), "The second second variable should be an Axes object!"

        # data checks
        assert len(ax.images) == 1, "You should plot exactly one image (that of the heatmap)!"
        assert ax.images[0].get_array().shape == freq_values.shape, "The heatmap should be quadratic!"
        assert ax.images[0].cmap.name == "inferno", "The heatmap should use the colormap 'inferno'!"
        assert np.allclose(ax.images[0].get_array(), freq_values), "The heatmap data does not match the expected data!"

        # annotation and labeling
        assert ax.get_title() == "Creature Type Frequencies per Alignment", "The title is not correct!"
        assert ax.xaxis.label.get_text() == "Alignment", "The x-axis is not labeled correctly!"
        assert ax.yaxis.label.get_text() == "Creature Type", "The y-axis is not labeled correctly!"
        assert np.all(sorted([label.get_text() for label in ax.get_xticklabels()]) == sorted(freq_names_align)), "The x-ticks seem to be incorrect!"
        assert np.all(sorted([label.get_text() for label in ax.get_yticklabels()]) == sorted(freq_names_type)), "The y-ticks seem to be incorrect!"
        assert fig.colorbar is not None, "There should be a colorbar!"

        # imports check
        try:
            assert set(imports_of_your_file(filename, testfile)) <= allowed_imports
        except AssertionError:
            print(f"Imports found in the file: {set(imports_of_your_file(filename, testfile))}")
            print(f"Allowed imports: {allowed_imports}")
            raise AssertionError("You are importing modules that are not allowed.")

        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_make_heatmap()


