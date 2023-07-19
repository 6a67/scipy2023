from helpers import imports_of_your_file
import numpy as np

import matplotlib

try:

    import temperature as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'temperature.py'!"

y_1990 = [ 5.01,  7.08,  7.56,  8.17, 14.32, 15.43, 16.82, 18.59, 11.87, 11.86,  5.37,  3.11]
y_2005 = [ 4.12,  1.24,  5.98, 10.59, 13.1 , 16.66, 18.2 , 16.14, 15.87, 12.68,  5.83,  3.11]
y_2020 = [ 5.22,  6.67,  6.7 , 11.35, 12.8 , 18.11, 17.3 , 20.75, 14.87, 11.31,  7.87,  5.15]
y_mean = [10.4325,      9.23333333, 10.25333333,  9.23083333, 10.355,       9.9625,
  8.0075,      9.83083333, 10.01333333, 10.7475,     10.73833333, 10.11833333,
 10.56166667, 10.365,      10.0925,     10.29333333, 10.91583333, 10.9925,
 10.40666667, 10.27166667,  8.82166667, 10.56833333, 10.11666667,  9.66083333,
 11.40916667, 10.7725,     10.435,      10.7075,     11.41416667, 11.25083333,
 11.50833333, 10.21833333]

def test_plot_temperature(filename="temperature", allowed_imports={"numpy", "matplotlib.pyplot", "helpers"}):
    """ Checks whether plots returned by plot_temperature have the correct attributes. """
    
    df = np.load('data/full_temperature.npy', allow_pickle=True)
    fig, ax1, ax2 = testfile.plot_temperature(df)

    # general checks
    assert isinstance(fig, matplotlib.figure.Figure), "The first returned variable should be a Figure!"
    assert isinstance(ax1, matplotlib.axes.Axes), "The second returned variable should be an Axes object!"
    assert isinstance(ax2, matplotlib.axes.Axes), "The third returned variable should be an Axes object!"

    # upper plot data checks
    assert len(ax1.lines) == 3, "You should plot exactly three lines in the upper plot!"
    assert np.allclose(y_1990, ax1.lines[0].get_data()[1]) or np.allclose(y_1990, ax1.lines[1].get_data()[1]) or np.allclose(y_1990, ax1.lines[2].get_data()[1]),\
    "Neither line of the upper plot contains the correct year 1990 data!"
    assert np.allclose(y_2005, ax1.lines[0].get_data()[1]) or np.allclose(y_2005, ax1.lines[1].get_data()[1]) or np.allclose(y_2005, ax1.lines[2].get_data()[1]),\
    "Neither line of the upper plot contains the correct year 2005 data!"
    assert np.allclose(y_2020, ax1.lines[0].get_data()[1]) or np.allclose(y_2020, ax1.lines[1].get_data()[1]) or np.allclose(y_2020, ax1.lines[2].get_data()[1]),\
    "Neither line of the upper plot contains the correct year 2020 data!"

    # lower plot data checks
    assert len(ax2.lines) == 1, "You should plot only one line in the upper plot!"
    assert np.allclose(y_mean, ax2.lines[0].get_data()[1]),\
    "The line of the lower plot doesn't contain the correct mean values"

    # annotation and labeling 
    assert fig._suptitle.get_text() == "Temperature data for Muenster/Osnabrueck (1990-2021)", "The suptitle is not correct!"
    assert ax2.xaxis.label.get_text() == "Year", "The label of the x-axis of the second plot is supposed to enumerate the years!"
    assert ax2.yaxis.label.get_text() == "Temperature in C", "The label of the y-axis of the second plot is supposed to display the temperature in C!"
    assert ax1.xaxis.label.get_text() == "Month", "The label of the x-axis of the first plot is supposed to enumerate the months!"
    assert ax1.yaxis.label.get_text() == "Temperature in C", "The label of the y-axis of the first plot is supposed to display the temperature in C!"
    assert ax1._axes.yaxis._axes.title.get_text() == "Average temperature of selected years", "The title of the upper plot is not correct!"
    assert ax2._axes.yaxis._axes.title.get_text() == "Average temperatures and yearly variation over the years 1990-2021", "The title of the lower plot is not correct!"
    assert ax1.legend_ is not None, "Your upper plot needs a legend!"    

    # imports check
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are importing modules that are not allowed."

test_plot_temperature()