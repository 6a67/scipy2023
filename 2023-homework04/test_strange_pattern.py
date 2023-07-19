from hashlib import sha1

import numpy as np
import types

try:
    import strange_pattern as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is suppoesed to be 'strange_pattern.py'!"

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


def test_imports(filename="strange_pattern", allowed_imports={"numpy"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(
        filename)) <= allowed_imports, "You are not allowed to import any modules except NumPy!"


def test_strange_pattern():
    result = testfile.strange_pattern((10, 10))

    assert type(
        result) is np.ndarray, "Your function does not return a NumPy array!"
    assert result.dtype is np.dtype(
        "bool"), "Your function does not return a boolean array!"
    assert sha1(result).hexdigest(
    ) == '7e69ac17197f17ebccf456b6dfbbe95fe938b7d9', "Your function does not produce the correct pattern!"

    result = testfile.strange_pattern((2, 2))

    assert sha1(result).hexdigest(
    ) == "3c585604e87f855973731fea83e21fab9392d2fc", "Your function does not produce the correct pattern in an edge case!"

    result = testfile.strange_pattern((0, 0))

    assert result.shape == (
        0, 0), "Your function does not produce the correct pattern in an edge case!"