from statistics import mean
from experiments_utils import compute_intervals, INTERVAL_GENERATORS

ALPHAS = [0.05, 0.01, 0.001]
SIZES = [10, 100, 1000]

N = 10000
P = 0.33


def evaluate_interval(interval, p):
    length = interval[1] - interval[0]
    does_contain_p = int(interval[0] <= p <= interval[1])
    return length, does_contain_p


def evaluate_all_intervals(intervals, p):
    evaluation = []
    for intervals_of_type in intervals:
        type_eval = [evaluate_interval(interval, p) for interval in intervals_of_type]
        avg_length = mean(e[0] for e in type_eval)
        hit_rate = mean(e[1] for e in type_eval)
        evaluation.append((avg_length, hit_rate))
    return evaluation


def print_results(alpha, size, evaluation):
    print(f'##### alpha = {alpha}, n = {size} #####')
    for type_, results in enumerate(evaluation):
        print(f'Type {type_}: Average length: {results[0]:.3f}; Miss rate: {1-results[1]:.4f}')
    print()


for idx_alpha, alpha in enumerate(ALPHAS):
    for idx_size, size in enumerate(SIZES):
        intervals = compute_intervals(N, P, size, alpha, INTERVAL_GENERATORS)
        evaluation = evaluate_all_intervals(intervals, P)
        print_results(alpha, size, evaluation)
