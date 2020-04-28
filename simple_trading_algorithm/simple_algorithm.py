from simple_trading_algorithm.plot_utils import *


def init_figure():
    figure = get_figure()
    add_starting_point_triangle_to_figure(fig=figure)
    add_order_levels_to_figure(fig=figure, delta=10, num_of_layers=10)
    return figure


def run_algorithm_step(figure, index):
    return

