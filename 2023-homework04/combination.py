import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a: np.array, b: np.array, axis=0):
    a = a.squeeze()
    b = b.squeeze()

    # check if a and b are numpy arrays
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise TypeError("a and b must be numpy arrays")
    
    # check if axis is an integer
    if not isinstance(axis, int):
        raise TypeError("axis must be an integer")
    
    # check if axis is smaller than the number of dimensions of a and b
    if axis >= len(a.shape) or axis >= len(b.shape):
        raise ValueError("axis must be smaller than the number of dimensions of a and b")
    
    # combine the arrays along the given axis
    return np.concatenate((a, b), axis=axis)


if __name__ == "__main__":
    # use this for your own testing!

    pass
