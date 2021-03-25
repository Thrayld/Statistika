import matplotlib.pyplot as plt

from experiments_utils import compute_intervals, INTERVAL_GENERATORS


ALPHAS = [0.05, 0.01, 0.001]
SIZES = [10, 100, 1000]

N = 10
P = 0.33

# Constants for plotting
COLORS = ['red', 'blue']
EPSILON = 0.15


def plot_intervals(ax, intervals):
    for type_, intervals_of_type in enumerate(intervals):
        for num, interval in enumerate(intervals_of_type):
            ax.axhline(
                y=num - EPSILON*type_,
                xmin=interval[0],
                xmax=interval[1],
                color=COLORS[type_]
            )


def set_ax(ax, p, alpha, size):
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xlim([-0.1, 1.1])
    ax.set_title(f'α = {alpha}, n = {size}')
    ax.axvline(x=p)


def populate_ax(ax, p, alpha, size, intervals):
    set_ax(ax, p, alpha, size)
    plot_intervals(ax, intervals)


fig, axes = plt.subplots(len(ALPHAS), len(SIZES), figsize=(10, 10))
for idx_alpha, alpha in enumerate(ALPHAS):
    for idx_size, size in enumerate(SIZES):
        intervals = compute_intervals(N, P, size, alpha, INTERVAL_GENERATORS)
        ax = axes[idx_alpha][idx_size]
        populate_ax(ax, P, alpha, size, intervals)
fig.suptitle('Intervaly spolehlivosti pro různé hodnoty α a n', fontsize=20)
plt.show()


