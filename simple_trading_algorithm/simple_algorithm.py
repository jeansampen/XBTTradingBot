from simple_trading_algorithm.plot_utils import *


class Optimiser:
    def __init__(self):
        self.buy_orders: list = []
        self.sell_orders: list = []
        self.plot_manager: PlotManager = PlotManager()
        self.figure = self.plot_manager.fig

    def run_algorithm_step(self, index):
        self.plot_manager.add_order_levels_to_figure(delta=10, num_of_layers=10)

