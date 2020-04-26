from simple_trading_algorithm.plot_utils import *



index_1 = 20
index_2 = 200

figure = get_figure()
add_starting_point_triangle_to_figure(fig=figure)

init_order_levels_for_figure(fig=figure, delta=25, num_of_layers=5)
figure.show()