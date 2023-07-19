import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_densityplot(iris):
    sns.set(style="ticks")
    sns.set_style("darkgrid")

    g = sns.jointplot(
        data=iris,
        x="sepalWidth",
        y="petalWidth",
        hue="species",
        kind="kde",
        marginal_kws=dict(shade=True),
    )

    g.set_axis_labels("sepalWidth", "petalWidth")

    return g


if __name__ == "__main__":
    iris = pd.read_csv("data/iris.csv", index_col=0)
    fig = make_densityplot(iris)
    plt.show()
