[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/mgoGuM1z)
# Homework 4 - Basic NumPy

The deadline of this homework is on **Tuesday, 16th of May, 23:59:00 UTC+2**.

In this homework you should implement three different functions in their respective files.


### 1 Strange Pattern

You come across this strange pattern.

| x     |       |       | x     |       |       | x     |       |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|       |       | **x** |       |       | **x** |       |       |
|       | **x** |       |       | **x** |       |       | **x** |
| **x** |       |       | **x** |       |       | **x** |       |
|       |       | **x** |       |       | **x** |       |       |
|       | **x** |       |       | **x** |       |       | **x** |

Mesmerized, you decide you must write a function to generate arbitrary sizes of it. (_Write a function `strange_pattern` that takes a shape tuple `(n, m)` as input and generates a boolean (True for x's and False for blank spaces) 2D NumPy array of the given shape with this pattern_)

**Hint:** Perhaps this strange symbol might help? `::`

### 2 Gaussian analysis

Write a function `gaussian_analysis` which takes four parameters `loc`, `scale`, `lower_bound` and `upper_bound` and returns a tuple of two values (`mean`, `std`).
First of all the function should make sure that `loc`, `scale`, `lower_bound` and `upper_bound` are integers or floats and that `lower_bound` is smaller than `upper_bound` and should return meaningful error messages if those are not the case.
In the function 100 samples of a gaussian distribution should be drawn in respect to the given `loc` and `scale` parameters. Check out the Numpy documentation to find out which function you could use here.
Next, the values below the `lower_bound` and above the `upper_bound` should be filtered out. Afterwards you should calculate the `mean` and the `std`(standard deviation) of the array and return them in a tuple.



### 3. Combination of arrays

Write a function `combination` that takes in two numpy arrays and an optional parameter `axis` which should be 0 by default.
Remove unnecessary dimensions of the input arrays, check whether they can be combined along the given axis and return the combined array.
If the combination is not possible, raise a meaningful error message.

Good luck!
