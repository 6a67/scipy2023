import statsmodels as sm
import seaborn as sns
import numpy as np
import plotnine

try:
    import regression as testfile

except ModuleNotFoundError:

    assert False, 'The name of your file is supposed to be "regression.py"!'


def test_simple_regression():

    data = sns.load_dataset("tips")

    assert hasattr(testfile, "simple_regression"), "Your module needs a function 'simple_regression'"

    result_fit = testfile.simple_regression(data)

    assert isinstance(result_fit, sm.regression.linear_model.RegressionResultsWrapper), 'Your function needs to return a RegressionResultsWrapper object.'

    assert np.allclose(result_fit.params, [0.920270, 0.105025], rtol=1e-2), "Your fitted parameters do not match the expected parameters."


def test_plot():
    assert hasattr(testfile, "plot_regression"), "Your module needs a function 'plot_regression'"
    
    data = sns.load_dataset("tips")
    result_fit = testfile.simple_regression(data)

    plot = testfile.plot_regression(data, result_fit)

    assert isinstance(plot, plotnine.ggplot), 'Your function needs to return a ggplot object.'

    assert plot.labels.x=="total_bill", "Your plots x variable should be 'total_bill' "
    assert plot.labels.y=="tip", "Your plots y variable should be 'tip' "


if __name__ == "__main__":

    test_simple_regression()
    test_plot()
    print('pass')