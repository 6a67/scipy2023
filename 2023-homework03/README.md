[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/JIUWcR0c)
# Homework 03

The deadline of this homework is on **Tuesday, 9th of May, 23:59:00 UTC+2**.

Since we had some problems with getting autograding to work with only passing 2/3 pytests starting this week you will have to pass all the pytests. 
To compensate, we aim to give out either fewer or comparatively easier exercises.

## Overview

The purpose of this homework is to mainly test more advanced programming concepts in Python. The tasks will be centered on Object-Oriented Programming (OOP).

For this homework, make sure to submit:
- wizard_spell.py
- spellbook.py
- simulate.py 

In `simulate.py` your two classes from `wizard_spell.py` and `spellbook.py` are imported and some print statements are run to check if everything works.

Therefore, you should leave it alone for now and work in the other two non-test files. 

Then, for testing you can come back and run it, or even add or remove lines to check if what you have been working on works as intended.

Since `simulate.py` isn't checked in the `pytest`, you can add or remove code as you wish and should still be able to pass the `pytest`, as long as your two classes are implemented correctly.


## Cloning the repository

via command line

```bash
git clone <url>
```

or via Github Desktop application

```
File > Clone a Repository
```

In order to complete this assignment, you need to implement the following functions:

### 1. Class `WizardSpell`

In `wizard_spell.py`, define a class `WizardSpell` that represents a spell in the magical world of Harry Potter.

`WizardSpell` should have two instance attributes: `spell_type` of type `str` and `power` of type `int`.

Furthermore, `WizardSpell` should overwrite four *dunder* methods:

- the constructor `__init__`
- the string representation `__str__`
- the left addition function `__add__`
- the right addition function `__radd__`

We will use `__init__` to initialize the `spell_type` and `power` attributes, `__str__` to make sure that the spell has a sensible representation when printed, and `__add__` and `__radd__` to implement the combination operation for two `WizardSpell` objects, which yields a new `WizardSpell` object.

### \_\_init\_\_

This function initializes the `spell_type` and `power` of the `WizardSpell`. It should have three keyword arguments:

- Keyword argument `spell_type` should have a default value of `None`.
- Keyword argument `possible_spell_type` should have as default value a tuple of the three basic spell types: `Charm`, `Transfiguration`, and `Potion`.
- Keyword argument `power` should have a default value of `None`.

If the keyword argument `spell_type` has the value `None`, the instance attribute `spell_type` should be selected randomly among `possible_spell_types`. Otherwise, the instance attribute `spell_type` should have the same value as the keyword argument `spell_type`.

`Hint`: You can implement a random selection by calling the function `random.choice()` on an iterable. The random module is already imported for your convenience. You can learn more about random [here][def].

If the keyword argument `power` has the value `None`, the instance attribute `power` should be assigned a random integer between `1` and `100`. Otherwise, the instance attribute `power` should have the same value as the keyword argument `power`.

### \_\_str\_\_

Use the `__str__` method to generate a representation following these examples:

- `<WizardSpell of type Charm>`
- `<WizardSpell of type Transfiguration>`
- `<WizardSpell of type Potion>`

The text should be dependent on the instance attributes `spell_type` and `power`. This is also the text that will be printed when calling print on a `WizardSpell` instance.

### \_\_add\_\_

The `__add__` method will be used to define the behavior when adding two `WizardSpel` objects with the `+` operator. This operator is supposed to implement a combination operation, representing the blending of two magical spells. This will generate a child object of class `WizardSpell`.

The `spell_type` of the child object is determined by chance as well as by the following combination rules:

| Parent 1         | Parent 2         | Resulting Child Spell Type               |
|------------------|------------------|------------------------------------------|
| Charm            | Charm            | Charm                                    |
| Charm            | Transfiguration  | Enchantment, Illusion, or Conjuration (randomly chosen) |
| Charm            | Potion           | Alchemy                                  |
| Transfiguration  | Transfiguration  | Transfiguration                          |
| Transfiguration  | Potion           | Metamorphosis                            |
| Potion           | Potion           | Potion                                   |

For combinations not listed in the table, the resulting child spell type is randomly chosen from the parent spell types. The order of the parents given should not matter.

You will see that we have already added a dictionary with 3 different parent combinations and their correct child spell type.
To get out the correct child type from the dictionary, you can use Python's `.get()` method by giving it the two parent types as a key.

The provided dictionary can be enough to solve the task, if you do some work in your code. You will have to sort both parent spell types alphabetically so that for both examples `1: (Charm, Potion)` and `2: (Potion, Charm)` the correct dictionairy entry will be found. This can be done with the help of Python's `sorted()` method.

Additionally, you will have to return one of the parent types if no corresponding entry is found in the dictionary, for example in the case of `(Charm, Charm)`.

This can be done with a simple *if condition* checking whether a child option has been returned by the `.get()` method.

Alternatively, you could also expand the dictionary to include all the possible combinations.

To recap what has to be implemented in the `__add__` method:

- If one of the objects is not of type `WizardSpell`, a `TypeError` is raised.
- If the two objects are the same `spell_type`, the child will be the same `spell_type`.
- If the two objects are of spell types `Charm` and `Transfiguration`, the child `spell_type` will be chosen randomly among `Enchantment`, `Illusion`, and `Conjuration`.
- If the two objects are of spell types `Charm` and `Potion`, the child `spell_type` will be `Alchemy`.
- If the two objects are of spell types `Transfiguration` and `Potion`, the child `spell_type` will be `Metamorphosis`.
- If the two objects are of different spell types and no combination rule is defined, the child `spell_type` will be chosen randomly among the parent `spell_types`.

Try to make the `TypeError` informative. At the very least, be sure to mention the word spell (this will be tested for).

### \_\_radd\_\_

The `__radd__` method is only called when the object to the left of the operator `+` is a non-`WizardSpell`, for which the combination operation is undefined. Therefore, you can simply raise a `TypeError` when the method is called. Try to make the `TypeError` informative. At the very least, be sure to mention the word spell (this will be tested for).

### 2. Class `Spellbook`

In `spellbook.py`, define a class `Spellbook` that is filled with wizard spells.

`Spellbook` should have a single instance attribute `spells` which is of type list.

Furthermore, it will have six methods:
- `__init__`
- `__len__`
- `__str__`
- `add_spell`
- `combine`
- `most_powerful_spell`

The constructor `__init__` initializes the instance attribute `spells` with an empty list. `__len__` returns the current length of that list, which is equal to the number of spells currently in the spellbook.

### \_\_str\_\_

Use the `__str__` method to generate a representation following these examples:

- `<Spellbook with 0 spells and 0 types>`
- `<Spellbook with 5 spells and 3 types>`
- `<Spellbook with 8 spells and 4 types>`

Next to the number of spells, you will also need to calculate the number of **unique spell types** currently in the spellbook.

`Hint`: Unique values can easily be counted using sets.

### add_spell

The method `add_spell` should have one keyword argument `new_spell` with default value `None`. If this keyword argument has the value `None`, a new `WizardSpell` object should be appended to the instance attribute spells list with a random power. Otherwise, the value of `new_spell` is appended to spells.

### combine

The method `combine` randomly selects two objects from the spells list and applies the combination operation to them with the `+` operator. The result is added to the spellbook using the `add_spell` method. If there are not at least two objects in the spells list, nothing happens.

### most_powerful_spell
The method `most_powerful_spell` iterates through the spells list and returns the `WizardSpell` object with the highest power attribute.

If you have implemented both `WizardSpell` and `Spellbook` correctly, `simulate.py` should now execute fully without errors. You can then try running `pytest`, which tests the functionality of both classes a bit more extensively.

If the `pytest` passes both on your local system and online, then you have passed this homework. Good luck!

## Submitting this homework

- Make sure that you test your code before submitting it. You can run the tests either by using Testing in Visual Studio Code or by running `pytest` command.

- After your code passes the tests, push your code by running the following commands or via Github Desktop Application:

```bash
git add .
```

```bash
git commit -m "Commit message"
```

```bash
git push
```

- Congratulations! If you have verified that your commit has passed the online autograde, then you have successfully completed your homework and you will see a green tick on your repo.

## Submitting the weekly feedback

- We appreciate your feedback on the content we've shared over the past week – it helps us improve and continue to provide engaging and relevant material.
- Follow [this link](https://docs.google.com/forms/d/e/1FAIpQLSeGOBvRQpU1bxiWUlIbsMnBgVHsEx0EsvLAEkb2PIspapzJHA/viewform) to fill in the feedback form.


[def]: https://docs.python.org/3/library/random.html
