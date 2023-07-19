from spellbook import Spellbook
from wizard_spell import WizardSpell

def main():
    simulate_spellbook()

def simulate_spellbook():
    my_spellbook = Spellbook()

    print("Creating a Spellbook my_spellbook ...")
    print(my_spellbook)

    print("\nAdding 3 Wizard Spells to my_spellbook ...")
    my_spellbook.add_spell(WizardSpell(spell_type="Charm"))
    my_spellbook.add_spell(WizardSpell(spell_type="Transfiguration"))
    my_spellbook.add_spell(WizardSpell(spell_type="Potions"))
    print(my_spellbook)

    print("\nCombining spells in my_spellbook ...")
    my_spellbook.combine()
    print(my_spellbook)

    print("\nThe most powerful spell in the spellbook is:", my_spellbook.most_powerful_spell())

if __name__ == "__main__":
    main()

