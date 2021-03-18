import fplot
import numpy as np
import matplotlib.pyplot as plt

data = [
    (1, '#1f77b4'),
    (2, '#ff7f0e'),
    (1/2, '#2ca02c'),
]

parameters = [{'lambda': p[0], 'color': p[1]} for p in data]


def get_pdf(L):
    return lambda x: L * np.exp(-L * x)


def get_cdf(L):
    return lambda x: 1 - np.exp(-L*x)


def get_median(L):
    return np.log(1 / 2) / (-L)


values = [
    {
        'pdf': get_pdf(p['lambda']),
        'cdf': get_cdf(p['lambda']),
        'median': get_median(p['lambda']),
        'color': p['color']
    }
    for p in parameters
]

lambdas = [p['lambda'] for p in parameters]
colors = [p['color'] for p in parameters]
pdfs = [get_pdf(p['lambda']) for p in parameters]
cdfs = [get_cdf(p['lambda']) for p in parameters]
medians = [get_median(p['lambda']) for p in parameters]


fplot.plot(
    pdfs,
    0, 5,
    show=False,
    # color=colors,
    title='Hustota exponenciálních rozdělení'
)
plt.vlines(medians, ymin=0, ymax=max(lambdas), color=colors, ls='--')
plt.legend([f'λ = {L}' for L in lambdas])
plt.show()

fplot.plot(
    cdfs,
    0, 5,
    show=False,
    # color=colors,
    title='Distribuce exponenciálních rozdělení'
)
plt.vlines(medians, ymin=0, ymax=1, color=colors, ls='--')
plt.legend([f'λ = {L}' for L in lambdas])
plt.show()
