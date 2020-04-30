from datetime import datetime

from Enum.OrderType import OrderType
from Enum.OrderState import OrderState


class Order:
    def __init__(self, price: float, order_size: int, start_timestamp: datetime, line_id: str, order_type: OrderType):
        self.state: OrderState = OrderState.OPEN
        self.start_timestamp: datetime = start_timestamp
        self.end_timestamp: datetime = None
        self.order_size: int = order_size
        self.price: float = price
        self.line_id: str = line_id
        self.order_type: OrderType = order_type

    def __str__(self) -> str:
        return'''
        Price = {}, 
        Order Size = {}, 
        Start Time = {}, 
        State = {},
        LineID = {}
        '''.format(self.price, self.order_size, self.start_timestamp, self.state, self.line_id)

    def close_order(self, closing_timestamp):
        self.end_timestamp = closing_timestamp
        self.state = OrderState.CLOSED
