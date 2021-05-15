from src.utils.runge_kutta import ode45
from src.utils.plot import (
    build_plot,
    show_plot,
)
from src.utils.metadata import print_metadata

if __name__ == '__main__':
    calculated_data = ode45()
    print_metadata()
    build_plot(calculated_data, title='4-5 order Runge-Kutta')
    show_plot()
