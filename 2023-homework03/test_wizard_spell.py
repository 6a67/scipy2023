import types

try:
    import wizard_spell as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'wizard_spell.py'!"


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


def test_imports(filename="wizard_spell", allowed_imports={"random"}):
    """ Checks if any non-allowed imports have been done. """
    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import any modules except random!"


def test_wizard_spell():
    """ Checks WizardSpell class functionality. """
    a = testfile.WizardSpell()
    b = testfile.WizardSpell(spell_type=None)

    charm = testfile.WizardSpell(spell_type="Charm")

    assert hasattr(charm, "spell_type"), "'WizardSpell' object does not have a 'spell_type' attribute!"
    assert charm.spell_type == "Charm", "'WizardSpell' object does not have the specified spell_type!"
    assert hasattr(charm, "power"), "'WizardSpell' object does not have a 'power' attribute!"
    assert 1 <= charm.power <= 100, "'WizardSpell' object does not have a power value within the specified range!"

    assert str(a) == f"<WizardSpell of type {a.spell_type} with power {a.power}>", "'WizardSpell' object does not have the specified string representation!"
    assert str(charm) == f"<WizardSpell of type Charm with power {charm.power}>",  "'WizardSpell' object does not have the specified string representation!"

    transfiguration = testfile.WizardSpell(spell_type="Transfiguration")
    potion = testfile.WizardSpell(spell_type="Potion")

    assert isinstance(a + b, testfile.WizardSpell), "Combination operation does not return 'WizardSpell' object!"
    assert (a + a).spell_type == a.spell_type, "Combination rules are not followed in detail!"

    child_spell = a + b
    assert 1 <= child_spell.power <= 100, "'WizardSpell' object does not have a power value within the specified range when combined!"

    try:
        a + 7
    except TypeError as e:
        assert "spell" in str(e), "You have to mention the word 'spell' at least once in the TypeError message!"

    try:
        7 + a
    except TypeError as e:
        assert "spell" in str(e), "You have to mention the word 'spell' at least once in the TypeError message!"


if __name__ == "__main__":
    test_imports()
    test_wizard_spell()
    print("All tests passed!")
