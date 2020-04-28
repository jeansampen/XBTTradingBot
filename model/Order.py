from datetime import datetime

from Enum.OrderState import OrderState


class Order:
    def __init__(self, price: float = None, order_size: int = None):
        self.state: OrderState = OrderState.OPEN
        self.end_timestamp: datetime = None
        self.start_timestamp: datetime = datetime.now()
        self.order_size: int = order_size
        self.price: float = price
