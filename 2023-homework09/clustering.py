import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def generate_data(n_samples, n_centers, std):
    X, y_true, centers = make_blobs(
        n_samples=n_samples,
        centers=n_centers,
        cluster_std=std,
        random_state=0,
        return_centers=True,
    )
    return X, y_true, centers


def cluster(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, n_init="auto")
    kmeans.fit(X)
    y_pred = kmeans.predict(X)
    centroids = kmeans.cluster_centers_
    return kmeans, y_pred, centroids


def analyze_results(X, true_labels, true_centers, labels, centroids):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Plot ground truth clusters
    ax1.scatter(X[:, 0], X[:, 1], c=true_labels, cmap="viridis")
    ax1.scatter(
        true_centers[:, 0],
        true_centers[:, 1],
        marker="x",
        s=50,
        color="black",
        linewidth=4,
        alpha=1,
    )
    ax1.set_title("Ground truth clusters")

    # Plot predicted clusters
    ax2.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
    ax2.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="x",
        s=50,
        color="black",
        linewidth=4,
        alpha=1,
    )
    ax2.set_title("Predicted clusters")

    plt.show()


if __name__ == "__main__":
    n_samples = 800
    n_centers = 7
    std = 0.6
    n_clusters = 7

    X, true_labels, true_centers = generate_data(n_samples, n_centers, std)

    kmeans, labels, centroids = cluster(X, n_clusters)

    analyze_results(X, true_labels, true_centers, labels, centroids)
