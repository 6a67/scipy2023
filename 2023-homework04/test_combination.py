from hashlib import sha1
import numpy as np
import types

try:
    import combination as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is suppoesed to be 'combination.py'!"

def imports_of_your_file(filename):
    """ Yields all imports in the testfile. """

    for name, val in vars(testfile).items():
        if isinstance(val, types.ModuleType):
            # get direct imports
            yield val.__name__

        else:
            # get from x import y imports
            imprt = getattr(testfile, name)

            if hasattr(imprt, "__module__") and not str(imprt.__module__).startswith("_") and not str(imprt.__module__) == filename:
                yield imprt.__module__


def test_imports(filename="combination", allowed_imports={"numpy"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(
        filename)) <= allowed_imports, "You are not allowed to import any modules except NumPy!"


def test_combination():
    a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    b = np.ones((2,2))

    result = testfile.combination(a,b)

    assert sha1(result).hexdigest(
    ) == '5709b4ea8b49ac48d42ae3e0bd1b3fb0dbb3249b', 'Your function does not return the right result!'

    
