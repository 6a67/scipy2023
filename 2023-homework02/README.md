[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/iMOiJVnY)
# Homework 02

The deadline of this homework is on **Tuesday, 2nd of May, 23:59:00 UTC+2**.

## Overview

The purpose of this homework is mainly to test the basic python skills such as Data types, methods, loops, etc.

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

### 1. Calculate the factorial of a non-negative integer

Your task for this exercise is to implement the function `factorial` in the `factorial.py` file.

The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n` and is denoted as `n!`.

### 2. Create a custom repeater

Your task for this exercise is to implement the function `repeat` in the `repeat.py` file.

Create a function that repeats each character in a given string `s` according to a provided `pattern`. The output must be a string containing the characters of `s` repeated according to the `pattern`.

| Input                         | Output                                     |
| :---------------------------  | :----------------------------------------- |
| `("abc", [1, 2, 3])`          | `abbccc`                                   |
| `("hello", [1, 2])`           | `heelllo`                                  | 
| `("osnabrueck", [1, 2, 3, 4])`| `ossnnnaaaabrruuueeeeckk`                    |


### 3. Create a `SeaAnimal` class

At the end of this weeks lecture you learned about classes. 

Write a class `SeaAnimal` according to the class `LandAnimal` (see in the file `sea_animal.py` as well as in the notebook "classes" of the lecture). The class should:
- inherit from the class `Animal`;
- have an `__init__` method with the attribute `has_flippers` that should be `True`;
- have a `swim()` method that returns a string `shuh shuh` (http://writtensound.com/index.php?term=swimming).

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
