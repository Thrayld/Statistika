import numpy as np

size = 100
true_lambda_ = 0.7

np.random.seed(0)
sample = np.random.exponential(1 / true_lambda_, size)

mle = 1 / sample.mean()

print(f'mle: {mle:0.3f}')
