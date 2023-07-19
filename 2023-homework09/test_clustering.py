import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

try:
    import clustering as testfile
except ModuleNotFoundError:
    assert False, 'The module clustering is not found!'

def test_generate_data():
    n_samples = 800
    n_centers = 7
    std = 0.6

    assert hasattr(testfile, "generate_data"), "Your module needs a function 'generate_data'"
    X, true_labels, true_centers = testfile.generate_data(n_samples, n_centers, std)

    assert isinstance(X, np.ndarray), 'X should be a numpy array.'
    assert isinstance(true_labels, np.ndarray), 'true_labels should be a numpy array.'
    assert isinstance(true_centers, np.ndarray), 'true_centers should be a numpy array.'

def test_cluster():
    n_samples = 800
    n_centers = 7
    std = 0.6
    n_clusters = 7

    X, true_labels, true_centers = testfile.generate_data(n_samples, n_centers, std)

    assert hasattr(testfile, "cluster"), "Your module needs a function 'cluster'"
    kmeans, labels, centroids = testfile.cluster(X, n_clusters)

    assert isinstance(kmeans, KMeans), 'kmeans should be a KMeans object.'
    assert isinstance(labels, np.ndarray), 'labels should be a numpy array.'
    assert isinstance(centroids, np.ndarray), 'centroids should be a numpy array.'

if __name__ == "__main__":
    test_generate_data()
    test_cluster()
    print('pass')
