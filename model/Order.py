from datetime import datetime
from Enum.OrderState import OrderState


class Order:
    def __init__(self, price: float, order_size: int, start_timestamp: datetime):
        self.state: OrderState = OrderState.OPEN
        self.start_timestamp = start_timestamp
        self.end_timestamp: datetime = None
        self.order_size: int = order_size
        self.price: float = price

    def __str__(self) -> str:
        return'''
        Price = {}, 
        Order Size = {}, 
        Start Time = {}, 
        State = {}
        '''.format(self.price, self.order_size, self.start_timestamp, self.state)

    def close_order(self, closing_timestamp):
        self.end_timestamp = closing_timestamp
        self.state = OrderState.CLOSED
