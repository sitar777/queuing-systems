from src.utils.runge_kutta import ode45
from src.utils.plot import (
    build_plot,
    show_plot,
)

if __name__ == '__main__':
    calculated_data = ode45()
    build_plot(calculated_data, title='4-5 order Runge-Kutta')
    show_plot()
