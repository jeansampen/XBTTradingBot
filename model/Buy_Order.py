from datetime import datetime

from model.Order import Order


class BuyOrder(Order):
    def __init__(self, price: float, order_size: int, start_timestamp: datetime):
        super().__init__(price, order_size, start_timestamp)


