import types

try:
    import repeat as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'repeat.py'!"


def test_imports(filename="repeat", allowed_imports=set()):
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


def test_custom_repeater():

    assert hasattr(
        testfile, "custom_repeater"), "Your repeat.py script must have a `custom_repeater`-function"
    
    assert testfile.custom_repeater("abc", [1, 2, 3]) == "abbccc"
    assert testfile.custom_repeater("hello", [1, 2]) == "heelllo"
    assert testfile.custom_repeater("xyz", [0, 3]) == "yyy"
    assert testfile.custom_repeater("osnabrueck", [1, 2, 3, 4]) == "ossnnnaaaabrruuueeeeckk"