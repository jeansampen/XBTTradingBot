from datetime import datetime


class Order:
    def __init__(self,
                 price: float = None,
                 order_size: int = None,
                 order_type: str = None, # Buy or sell
                 start_timestamp: datetime = None,
                 end_timestamp: datetime = None,
                 state: str = None, #Open or closed
                 ):
        self.state = state
        self.end_timestamp = end_timestamp
        self.start_timestamp = start_timestamp
        self.order_type = order_type
        self.order_size = order_size
        self.price = price
