# order.py

class Order(object):
    def __init__(self, unit_key, order_type):
        self.unit_key = unit_key
        self.order_type = order_type


class MovementOrder(Order):
    def __init__(self, unit_key, new_position):
        super(MovementOrder, self).__init__(
            unit_key, "MOVEMENT"
        )
        self.new_position = new_position