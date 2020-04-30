from Enum.OrderType import OrderType
from Enum.PriceType import PriceType
from model.Order import Order
from simple_trading_algorithm.PlotManager import *
import random
import string


def generateId(stringLength=12):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class Optimiser:
    CURRENT_POSITION = 0
    INITIAL_BALANCE = 2000
    LEVEL_INTERVAL = 5
    ORDER_SIZE = 200
    NUM_OF_BUY_LEVELS = 10
    MOVING_MARKER_ID = 'MOVING_MARKER_ID'

    def __init__(self):
        self.data_manager = DataManager()
        self.buy_orders: list = []
        self.sell_orders: list = []
        self.plot_manager: PlotManager = PlotManager(self.data_manager)
        self.figure = self.plot_manager.fig
        self.balance = Optimiser.INITIAL_BALANCE

        self.init_buy_orders()

    def generate_new_order(self, price: float, start_timestamp: datetime, order_type: OrderType):
        new_line_id = generateId()
        buy_order = Order(price, Optimiser.ORDER_SIZE, start_timestamp, new_line_id, order_type)
        if order_type == OrderType.BUY:
            self.plot_manager.add_buy_line(buy_order.price, new_line_id)
        else:
            self.plot_manager.add_sell_line(buy_order.price, new_line_id)
        return buy_order

    def init_buy_orders(self):
        [start_timestamp, start_price] = self.data_manager.get_starting_point_for_price_type(PriceType.LOW)
        for i in range(1, Optimiser.NUM_OF_BUY_LEVELS + 1):
            buy_order = self.generate_new_order(start_price - i * Optimiser.LEVEL_INTERVAL, start_timestamp,
                                                OrderType.BUY)
            self.buy_orders.append(buy_order)

        self.plot_manager.add_starting_point_triangle()

    def run_algorithm_step(self, index):
        self.move_marker(index)
        self.execute_buy_orders(index)
        self.execute_sell_orders(index)
        return self.calculate_descriptors(index)

    def move_marker(self, index):
        [current_timestamp, current_low_price] = self.data_manager.get_data_for_index_and_price_type(index,
                                                                                                     PriceType.LOW)
        self.plot_manager.move_marker(current_timestamp, current_low_price, Optimiser.MOVING_MARKER_ID)

    def execute_buy_orders(self, index):
        [current_timestamp, current_low_price] = self.data_manager.get_data_for_index_and_price_type(index,
                                                                                                     PriceType.LOW)
        orders_to_remove = []

        for buy_order in self.buy_orders:
            if current_low_price < buy_order.price:
                self.close_order(buy_order, current_timestamp)
                new_sell_order = self.generate_new_order(price=buy_order.price + (2 * Optimiser.LEVEL_INTERVAL),
                                                         start_timestamp=current_timestamp,
                                                         order_type=OrderType.SELL)

                self.sell_orders.append(new_sell_order)
                orders_to_remove.append(buy_order)

        for buy_order in orders_to_remove:
            self.buy_orders.remove(buy_order)

    def execute_sell_orders(self, index):
        [current_timestamp, current_high_price] = self.data_manager.get_data_for_index_and_price_type(index,
                                                                                                      PriceType.HIGH)
        orders_to_remove = []

        for sell_order in self.sell_orders:
            if current_high_price > sell_order.price:
                self.close_order(sell_order, current_timestamp)
                new_buy_order = self.generate_new_order(price=sell_order.price - (2 * Optimiser.LEVEL_INTERVAL),
                                                        start_timestamp=current_timestamp,
                                                        order_type=OrderType.BUY)
                self.buy_orders.append(new_buy_order)
                orders_to_remove.append(sell_order)

        for sell_order in orders_to_remove:
            self.sell_orders.remove(sell_order)

    def close_order(self, order: Order, closing_timestamp):
        order.close_order(closing_timestamp)
        self.plot_manager.remove_line_by_id(order.line_id)
        if order.order_type == OrderType.BUY:
            self.plot_manager.add_buy_triangle(closing_timestamp, order.price)
        else:
            self.plot_manager.add_sell_triangle(closing_timestamp, order.price)
            diff = 2 * Optimiser.LEVEL_INTERVAL
            self.balance += (Optimiser.ORDER_SIZE / (order.price - diff)) * diff



    def calculate_descriptors(self, index):
        [time, price] = self.data_manager.get_data_for_index_and_price_type(index, PriceType.CLOSE)
        return [time, price, self.balance]
