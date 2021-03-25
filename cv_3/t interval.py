from cv_2.data import MOCK_DATA, sample_mean
from experiments_utils import get_second_interval

alpha = 0.05

lower_bound, upper_bound = get_second_interval(MOCK_DATA, alpha)

print(f'Estimate: {sample_mean:.2f}')
print(f'Confidence interval: [{lower_bound:.2f}, {upper_bound:.2f}]')