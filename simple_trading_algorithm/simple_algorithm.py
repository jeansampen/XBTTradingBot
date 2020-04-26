from simple_trading_algorithm.plot_utils import *


def init_figure():
    figure = get_figure()
    add_starting_point_triangle_to_figure(fig=figure)
    return figure
