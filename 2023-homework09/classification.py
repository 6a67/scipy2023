from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def classify(data):
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.3, random_state=0
    )

    results = []
    for k in range(1, 50):
        for weights in ["uniform", "distance"]:
            for algorithm in ["ball_tree", "kd_tree", "brute"]:
                clf = KNeighborsClassifier(
                    n_neighbors=k, weights=weights, algorithm=algorithm
                )
                clf.fit(X_train, y_train)
                score = clf.score(X_test, y_test)
                result = {
                    "k": k,
                    "weights": weights,
                    "algorithm": algorithm,
                    "score": score,
                }
                print(result)
                results.append(result)

    best_result = max(results, key=lambda x: x["score"])
    print(f"Best score: {best_result['score']:.2f}")
    print(f"Best k: {best_result['k']}")
    print(f"Best weights: {best_result['weights']}")
    print(f"Best algorithm: {best_result['algorithm']}")

    return clf


if __name__ == "__main__":
    data = datasets.load_digits()
    classifier = classify(data)
