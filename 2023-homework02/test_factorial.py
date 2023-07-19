import types

try:
    import factorial as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'factorial.py'!"


def test_imports(filename="factorial", allowed_imports=set()):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import other modules in this exercise!"


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

def test_factorial():
    assert hasattr(
        testfile, "factorial"), "Your factorial.py script must have a method called factorial"
    
    assert testfile.factorial(0) == 1
    assert testfile.factorial(1) == 1
    assert testfile.factorial(5) == 120
    assert testfile.factorial(10) == 3628800

