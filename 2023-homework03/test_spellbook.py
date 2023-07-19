import types

try:
    import spellbook as testfile
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'spellbook.py'!"

from wizard_spell import WizardSpell

def imports_of_your_file(filename):
    """ Yields all imports in the testfile. """
    for name, val in vars(testfile).items():
        if isinstance(val, types.ModuleType):
            # get direct imports
            yield val.__name__

def test_imports(filename="spellbook", allowed_imports={"random", "wizard_spell"}):
    """ Checks if any non-allowed imports have been done. """
    assert set(imports_of_your_file(filename)) <= allowed_imports, "You are not allowed to import any modules except random and wizard_spell!"

def test_spellbook():
    """ Checks Spellbook class functionality. """
    sb = testfile.Spellbook()

    assert hasattr(sb, "spells"), "'Spellbook' object does not have a 'spells' attribute!"
    assert sb.spells == [], "Attribute 'spells' is not initialized as empty list!"

    charm = WizardSpell(spell_type="Charm")
    transfiguration = WizardSpell(spell_type="Transfiguration")
    potion = WizardSpell(spell_type="Potion")

    sb.add_spell(charm)
    sb.add_spell(transfiguration)
    sb.add_spell(potion)

    assert len(sb) == 3, "len() does not return the expected length!"
    assert len(sb) == len(sb.spells), "len() does not return the correct length!"

    assert str(sb) == f"<Spellbook with {len(sb.spells)} spells and {len(set(spell.spell_type for spell in sb.spells))} types>", "'Spellbook' object does not have the specified string representation!"

    sb.combine()
    assert len(sb) == 4, "Combine method did not change length in expected way!"

    assert hasattr(sb, "most_powerful_spell"), "'Spellbook' object does not have the 'most_powerful_spell' method!"
    most_powerful = sb.most_powerful_spell()
    assert isinstance(most_powerful, WizardSpell), "The most_powerful_spell method does not return a WizardSpell object!"

if __name__ == "__main__":
    test_imports()
    test_spellbook()
    print("All tests passed!")

