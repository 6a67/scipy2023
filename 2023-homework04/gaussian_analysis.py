import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    # check if loc, scale, lower_bound, upper_bound are integers or floats
    if not isinstance(loc, (int, float)) or not isinstance(scale, (int, float)) or not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):    
        raise TypeError("loc, scale, lower_bound, upper_bound must be integers or floats")

    # check if lower_bound is smaller than upper_bound
    if lower_bound >= upper_bound:
        raise ValueError("lower_bound must be smaller than upper_bound")
    
    # draw 100 samples from a normal distribution with loc and scale
    samples = np.random.normal(loc, scale, 100)
    # filter out samples that are outside the bounds
    samples = samples[(samples >= lower_bound) & (samples <= upper_bound)]
    # calculate mean and standard deviation
    mean = np.mean(samples)
    std = np.std(samples)
    
    return (mean, std)


if __name__ == "__main__":
    # use this for your own testing!

    pass
