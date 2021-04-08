import sympy as sy

from maximum_likelihood import my_likelihood, my_log_likelihood, L
import data

common_args = dict(
    ylabel='',
    xlabel='',
    line_color='blue',
    show=False,
    backend='matplotlib',
)


def draw_mle_and_true_value_and_show(sympy_plot_object):
    backend = sympy_plot_object.backend(sympy_plot_object)
    fig = backend.fig
    ax = backend.ax[0]

    backend.process_series()
    ax.axvline(
        data.true_lambda_,
        color='lime'
    )
    ax.axvline(
        data.mle,
        color='red'
    )

    fig.show()


likelihood_plot = sy.plot(
    my_likelihood, (L, 0.4, 1.2),
    ylim=(0, 7e-56),
    axis_center=(0.37, 0),
    title='Věrohodnostní funkce',
    **common_args
)

draw_mle_and_true_value_and_show(likelihood_plot)

log_likelihood_plot = sy.plot(
    my_log_likelihood, (L, 0.4, 1.2),
    axis_center=(0.37, -135),
    title='Logaritmická věrohodnostní funkce',
    **common_args
)

draw_mle_and_true_value_and_show(log_likelihood_plot)
