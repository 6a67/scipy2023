import types

try:

    import sea_animal as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'sea_animal.py'!"


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


def test_imports(filename="sea_animal", allowed_imports={"random"}):
    """ Checks if any non-allowed imports have been done. """

    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import any modules except random!"

def test_sea_animal():
    from sea_animal import Animal
    a = testfile.SeaAnimal()

    # check inheritance
    assert isinstance(a, Animal), "SeaAnimal has to inherit from the class Animal"

    # check attributes of class
    assert hasattr(a, "has_flippers"), "SeaAnimal has to have attribute has_flippers"
    assert a.has_flippers == True, "SeaAnimal has to have attribute has_flippers"

    assert a.swim() == "shuh shuh", "SeaAnimal has to have attribute swimm"