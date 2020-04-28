from model.Buy_Order import BuyOrder
from simple_trading_algorithm.PlotManager import *


class Optimiser:
    CURRENT_POSITION = 0
    CURRENT_BALANCE = 2000
    LEVEL_INTERVAL = 10
    ORDER_SIZE = 20
    NUM_OF_BUY_LEVELS = 10

    def __init__(self):
        self.data_manager = DataManager()
        self.buy_orders: list = []
        self.sell_orders: list = []
        self.plot_manager: PlotManager = PlotManager(self.data_manager)
        self.figure = self.plot_manager.fig

        self.init_buy_orders()

    def run_algorithm_step(self, index):
        current_position = index

        return

    def init_buy_orders(self):
        [start_timestamp, start_price] = self.data_manager.get_starting_point()
        for i in range(1, Optimiser.NUM_OF_BUY_LEVELS + 1):
            buy_order = BuyOrder(start_price - i * Optimiser.LEVEL_INTERVAL, Optimiser.ORDER_SIZE, start_timestamp)
            self.buy_orders.append(buy_order)

        for order in self.buy_orders:
            print(str(order))
