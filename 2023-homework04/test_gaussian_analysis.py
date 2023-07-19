from hashlib import sha1

import numpy as np
import types

try:
    import gaussian_analysis as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is suppoesed to be 'gaussian_analysis.py'!"

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


def test_imports(filename="gaussian_analysis", allowed_imports={"numpy"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(
        filename)) <= allowed_imports, "You are not allowed to import any modules except NumPy!"

def test_gaussian_analysis():
    loc =  0
    scale = 3
    lower_bound = 1
    upper_bound = 3

    result = testfile.gaussian_analysis(loc,scale,lower_bound,upper_bound)
    assert type(result) is tuple, 'Your function does not return the right form of result!'
    assert result[0] < upper_bound and result[0] > lower_bound, 'Your function does not return the right result!'
    


    