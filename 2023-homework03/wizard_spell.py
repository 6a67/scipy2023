import random

class WizardSpell:
    spell_types: str = ""
    power: int = 0

# Remove the passes from the methods below and add your code in order to fulfil the assignment.
    def __init__(self, spell_type=None, possible_spell_types=("Charm", "Transfiguration", "Potion"), power=None):
        self.spell_type = random.choice(possible_spell_types) if spell_type is None else spell_type
        self.power = random.randint(1, 100) if power is None else power

    def __str__(self):
        return f"<WizardSpell of type {self.spell_type} with power {self.power}>"

    def __add__(self, other):
        # Check if other is of type WizardSpell
        if not isinstance(other, WizardSpell):
            raise TypeError(f"Cannot add WizardSpell and {type(other)}. sad spell[ing] :(")

        # Dictionary of the different spells given in the table in the task
        combinations = {
            ("Charm", "Transfiguration"): ("Enchantment", "Illusion", "Conjuration"),
            ("Charm", "Potion"): ("Alchemy",),
            ("Potion", "Transfiguration"): ("Metamorphosis",)
        }

        # Select the spell type from the dictionary given the current and the given spell type
        selected_spell = combinations.get(tuple(sorted((self.spell_type, other.spell_type))), None)
        if selected_spell is None:
            return WizardSpell(spell_type=random.choice([self.spell_type, other.spell_type]))

        return WizardSpell(spell_type=random.choice(selected_spell))

    def __radd__(self, other):
        return self.__add__(other)


# Example usage of the WizardSpell class. You can leave this alone, or add new code to test how stuff works.
if __name__ == "__main__":
    spell1 = WizardSpell(spell_type="Charm")
    spell2 = WizardSpell(spell_type="Transfiguration")
    print(spell1)  # WizardSpell of type Charm with power ... 
    print(spell2)  # WizardSpell of type Transfiguration with power ... 
    spell3 = spell1 + spell2
    print(spell3)  # WizardSpell of type ... 
