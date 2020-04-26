from simple_trading_algorithm.plot_utils import *



index_1 = 20
index_2 = 200

figure = get_figure()
add_buy_triangle_to_figure_for_index(figure, index_1)
add_sell_triangle_to_figure_for_index(figure, index_2)

add_sell_line_to_figure(figure, 7600)
add_buy_line_to_figure(figure, 7500)


figure.show()