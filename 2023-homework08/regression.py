import seaborn as sns
import statsmodels.formula.api as smf
from plotnine import *


def simple_regression(data):
    fit = smf.ols("tip ~ total_bill", data=data).fit()
    return fit


def plot_regression(data, fit):
    plot = (
        ggplot(data, aes(x="total_bill", y="tip"))
        + geom_point()
        + geom_abline(intercept=fit.params[0], slope=fit.params[1], color="red")
    )
    return plot


if __name__ == "__main__":
    data = sns.load_dataset("tips")
    fit = simple_regression(data)
    print(fit.summary())

    plot = plot_regression(data, fit)
    print(plot)

    """
    A higher total bill is associated with a higher tip.
    """
