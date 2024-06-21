# generate synthetic test scores
import numpy as np

def standard(n, shape, scale):
    # this defines a gamma-type distribution with a heavy left-skew.
    # approx. 1/3 
    scores = 100-np.random.gamma(shape, scale, n)
    return scores * (scores > 0)  # no negative scores


# bimodal
def bimodal(n,p,mod_1,mod_2,sd_1,sd_2):
    # n: number of data points to generate
    # p: proportion of n to put into first mode
    # mod_1,2: center of modes 1 and 2
    # sd_1,2: sd of modes 1 and 2
    test = np.append(
        np.random.normal(mod_1, sd_1, int(n * p)), 
        np.random.normal(mod_2, sd_2, int(n * (1-p))))
    mask = test < 100
    test = mask * (test - 100) + 100  # can't score above 100
    return test * (test > 0)  # no negative scores

# trimodal
def trimodal(n,p_1,p_2,mod_1,mod_2,mod_3,sd_1,sd_2,sd_3):
    test = np.append(
        np.random.normal(mod_1, sd_1, int(n*p_1)),
        np.random.normal(mod_2, sd_2, int(n*p_2))
    )
    test = np.append(
        test,
        np.random.normal(mod_3, sd_3, int(n*(1-p_1-p_2)))
    )
    mask = test < 100
    test = mask * (test - 100) + 100
    return test * (test > 0)

# unimodal
def unimodal(n,mean,sd):
    # n: number of data points to generate
    test = np.random.normal(mean, sd, n)
    mask = test < 100
    test = mask * (test - 100) + 100  # can't score above 100
    return test * (test > 0)  # no negative scores

# uniform
def uniform(n):
    return np.random.uniform(50,100,n)

