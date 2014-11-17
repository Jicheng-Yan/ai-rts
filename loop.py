# loop.py
import hashlib
import Queue

from order import MovementOrder
from vehicle import Tank


def create_units(map_ref, dt):
    t1 = Tank(1, map_ref, dt)
    units = {
        "%s_%s" % (
            t1.unit_type, hashlib.md5().hexdigest()
        ): t1
    }
    return units


if __name__ == "__main__":
    dt = 1/20.0  # 50fps
    orders = Queue.Queue()
    game_map = None
    #ai_list = create_ai(1)
    units = create_units(game_map, dt)
    t = 0

    unit_key = units.items()[0][0]
    order = MovementOrder(unit_key, [1.0, 1.0])
    orders.put(order)

    while t <= 1.0:
        print "time t = %s" % t

        # Loop through game AIs to carry out orders
        #for ai in ai_list:
        #    ai.give_orders(units, orders)

        # Update orders to units
        while True:
            try:
                order = orders.get(False)
            except Queue.Empty:
                break
            else:
                if order.order_type == "MOVEMENT":
                    units[order.unit_key].set_destination(
                        order.new_position
                    )

        # Update unit positions
        for u in units:
            units[u].update_position()
            print units[u].cur_pos
        t += dt
