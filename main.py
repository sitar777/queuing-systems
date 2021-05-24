from src.utils.runge_kutta import ode45
from src.utils.plot import (
    build_plot,
    render_plot,
)
from src.utils.metadata import print_metadata
from src.utils.equations import probability_derivative

if __name__ == '__main__':
    calculated_data = ode45(probability_derivative)
    print_metadata()
    build_plot(calculated_data, title='M/M/n/m queuing system with channels breakage')
    render_plot()
