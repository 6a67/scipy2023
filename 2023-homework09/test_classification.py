from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

try:
    import classification as testfile
except ModuleNotFoundError:
    assert False, 'The module classification is not found!'

def test_classify():
    data = datasets.load_digits()

    assert hasattr(testfile, "classify"), "Your module needs a function 'classify'"

    classifier = testfile.classify(data)

    assert isinstance(classifier, KNeighborsClassifier), 'Your function needs to return a KNeighborsClassifier object.'

    # Test if it achieves at least some minimum score:
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=0.3, random_state=0)
    score = classifier.score(X_test, y_test)
    assert score >= 0.8, "Your classifier performance is below the expected level."

if __name__ == "__main__":
    test_classify()
    print('pass')
