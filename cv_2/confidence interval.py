from scipy.stats import norm
from math import sqrt

from data import observation_count, estimate

alpha = 0.05
quantile = norm.ppf(1 - alpha / 2)

interval_half_length = quantile / sqrt(observation_count) * sqrt(estimate * (1 - estimate))

lower_bound = estimate - interval_half_length
upper_bound = estimate + interval_half_length

print(f'Estimate: {estimate:.2f}')
print(f'Confidence interval: [{lower_bound:.2f}, {upper_bound:.2f}]')
