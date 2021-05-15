import matplotlib.pyplot as plot

from src.config import (
    STEPS,
    CHANNELS,
)


def build_plot(proba_matrix, x_label="t", y_label="p", title="Sample Plot"):
    fig = plot.figure()
    ax = fig.add_subplot()
    for i in range(CHANNELS):
        x_axis = []
        for x in range(0, STEPS):
            x_axis.append(x * 0.01)
        ax.plot(x_axis, proba_matrix[i], label='State ' + str(i+1))
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return fig


def show_plot():
    plot.grid(True)
    plot.legend()
    plot.show()
