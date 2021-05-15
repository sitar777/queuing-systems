from typing import List, NoReturn

from matplotlib.figure import Figure
import matplotlib.pyplot as plot

from src.config import (
    STEPS,
    CHANNELS,
)


def build_plot(
    proba_matrix: List[List[float]],
    x_label: str = 't',
    y_label: str = 'p',
    title: str = 'Sample Plot',
        ) -> Figure:
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


def render_plot() -> NoReturn:
    plot.grid(True)
    plot.legend()
    plot.show()
