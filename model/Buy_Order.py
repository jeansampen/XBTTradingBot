from model.Order import Order


class SellOrder(Order):
    def __init__(self, price: float, order_size: int):
        super().__init__(price, order_size)
