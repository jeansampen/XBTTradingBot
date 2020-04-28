from Enum.PriceType import PriceType
from model.Buy_Order import BuyOrder
from model.Sell_Order import SellOrder
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

    def init_buy_orders(self):

        [start_timestamp, start_price] = self.data_manager.get_starting_point_for_price_type(PriceType.LOW)
        for i in range(1, Optimiser.NUM_OF_BUY_LEVELS + 1):
            buy_order = BuyOrder(start_price - i * Optimiser.LEVEL_INTERVAL, Optimiser.ORDER_SIZE, start_timestamp)
            self.plot_manager.add_buy_line(buy_order.price)
            self.buy_orders.append(buy_order)

        self.plot_manager.add_starting_point_triangle()
        for order in self.buy_orders:
            print(str(order))

    def run_algorithm_step(self, index):
        if index is not None and 0 < index < self.data_manager.MAX_INDEX:
            self.move_marker(index)
            self.execute_buy_orders(index)
            self.execute_sell_orders(index)

    def move_marker(self, index):
        [current_timestamp, current_low_price] = self.data_manager.get_data_for_index_and_price_type(index,
                                                                                                     PriceType.LOW)
        self.plot_manager.move_marker(current_timestamp, current_low_price)

    def execute_buy_orders(self, index):
        [current_timestamp, current_low_price] = self.data_manager.get_data_for_index_and_price_type(index,
                                                                                                     PriceType.LOW)
        orders_to_remove = []

        for buy_order in self.buy_orders:
            if current_low_price < buy_order.price:
                buy_order.close_order(current_timestamp)
                self.plot_manager.add_buy_triangle(current_timestamp, buy_order.price)
                new_sell_order = SellOrder(price=buy_order.price + (2 * Optimiser.LEVEL_INTERVAL),
                                           order_size=Optimiser.ORDER_SIZE,
                                           start_timestamp=current_timestamp)
                self.sell_orders.append(new_sell_order)
                self.plot_manager.add_sell_line(new_sell_order.price)
                orders_to_remove.append(buy_order)

        for buy_order in orders_to_remove:
            self.buy_orders.remove(buy_order)

    def execute_sell_orders(self, index):
        [current_timestamp, current_high_price] = self.data_manager.get_data_for_index_and_price_type(index,
                                                                                                      PriceType.HIGH)
        orders_to_remove = []

        for sell_order in self.sell_orders:
            if current_high_price > sell_order.price:
                sell_order.close_order(current_timestamp)
                self.plot_manager.add_sell_triangle(current_timestamp, sell_order.price)
                new_buy_order = BuyOrder(price=sell_order.price - (2 * Optimiser.LEVEL_INTERVAL),
                                         order_size=Optimiser.ORDER_SIZE,
                                         start_timestamp=current_timestamp)
                self.sell_orders.append(new_buy_order)
                self.plot_manager.add_buy_line(new_buy_order.price)
                orders_to_remove.append(sell_order)

        for sell_order in orders_to_remove:
            self.sell_orders.remove(sell_order)
