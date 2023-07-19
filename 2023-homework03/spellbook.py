import random
from wizard_spell import WizardSpell

class Spellbook:
    spells: list = []

# Remove the passes from the methods below and add your code in order to fulfil the assignment.
    def __init__(self):
        self.spells = []

    def __len__(self):
        return len(self.spells)

    def __str__(self):
        unique_spell_types = len(set([spell.spell_type for spell in self.spells]))
        return f"<Spellbook with {len(self)} spells and {unique_spell_types} types>"

    def add_spell(self, new_spell=None):
        if not isinstance(new_spell, WizardSpell):
            raise TypeError(f"Cannot add {type(new_spell)} to Spellbook")
        
        if new_spell is None:
            new_spell = WizardSpell()
        
        self.spells.append(new_spell)

    def combine(self):
        if len(self) < 2:
            return
        
        spell1 = random.choice(self.spells)
        spell2 = random.choice(self.spells)

        new_spell = spell1 + spell2

        self.add_spell(new_spell)

    def most_powerful_spell(self):
        if len(self) == 0:
            return None

        return max(self.spells, key=lambda spell: spell.power)

# Example usage of the Spellbook class. You can leave this alone, or add new code to test how stuff works.
if __name__ == "__main__":
    spellbook = Spellbook()
    spellbook.add_spell(WizardSpell(spell_type="Charm"))
    spellbook.add_spell(WizardSpell(spell_type="Transfiguration"))
    spellbook.add_spell(WizardSpell(spell_type="Potions"))

    print(spellbook)  # Spellbook with {current number of spells} and 3 types, each spell with a random power between 1 and 100.

    spellbook.combine()
    print(spellbook)  # Spellbook with {current number of spells + 1} and more types (depending on the combination), each spell with a random power between 1 and 100.

    most_powerful = spellbook.most_powerful_spell()
    print("The most powerful spell in the spellbook is:", most_powerful) # Prints the spell with the highest power value in the spellbook.
