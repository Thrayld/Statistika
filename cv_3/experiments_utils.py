from numpy import mean, var
from scipy.stats import norm, t
from math import sqrt
import numpy as np


np.random.seed(0)


def get_general_interval(data, alpha, quantile_function, variance_approx_function):
    data_size = len(data)
    sample_mean = mean(data)
    variance_approx = variance_approx_function(data)

    # For non-symmetric distributions
    upper_quantile = quantile_function(1-alpha/2)
    lower_quantile = quantile_function(alpha/2)

    # sample_mean - u_q * var_appx / sqrt(n) <= mu <= sample_mean - l_q * var_appx / sqrt(n)
    lower_bound = sample_mean - upper_quantile * sqrt(variance_approx) / sqrt(data_size)
    upper_bound = sample_mean - lower_quantile * sqrt(variance_approx) / sqrt(data_size)

    return lower_bound, upper_bound


def get_first_interval(data, alpha):
    quantile_function = lambda a: norm.ppf(a)
    variance_approx_function = lambda d: mean(d) * (1 - mean(d))
    return get_general_interval(data, alpha, quantile_function, variance_approx_function)


def get_second_interval(data, alpha):
    quantile_function = lambda a: t.ppf(a, df=len(data)-1)
    variance_approx_function = lambda d: var(d, ddof=1)
    return get_general_interval(data, alpha, quantile_function, variance_approx_function)


def get_sample(p, size):
    return (np.random.rand(size) < p).astype('int')


def compute_intervals(n, p, size, alpha, interval_generators):
    intervals = [[] for _ in range(len(interval_generators))]
    for interval_num in range(n):
        sample = get_sample(p, size)
        for idx, int_gen in enumerate(interval_generators):
            interval = int_gen(sample, alpha)
            intervals[idx].append(interval)
    return intervals


INTERVAL_GENERATORS = [get_first_interval, get_second_interval]
