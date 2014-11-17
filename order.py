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


class FireOrder(Order):
    def __init__(self, unit_key, firing_position):
        super(FireOrder, self).__init__(
            unit_key, "FIRE"
        )
        self.firing_position = firing_position


class BuildOrder(Order):
    def __init__(self, structure_key, build_unit_type):
        super(BuildOrder, self).__init__(
            structure_key, "BUILD"
        )
        self.build_unit_type = build_unit_type