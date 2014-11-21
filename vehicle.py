# vehicle.py

from unit import Unit


class Vehicle(Unit):
    def __init__(
        self, unit_type, team, hit_points, mass_build_cost, 
        mass_generate_rate, mass_bleed_rate,
        energy_build_cost, energy_generate_rate,
        energy_bleed_rate, position, max_speed, radius
    ):
        super(Vehicle, self).__init__(
            self, unit_type, team, 
            hit_points, mass_build_cost, 
            mass_generate_rate, mass_bleed_rate,
            energy_build_cost, energy_generate_rate,
            energy_bleed_rate, position
        )
        self.max_speed = max_speed  # Metres/second
        self.radius = radius  # Metres

        self.cur_speed = 0.0  # Metres/second
        self.cur_dest = position  # Destination x, y co-ords

    def set_destination(self, new_pos):
        self.cur_dest = new_pos

    def update_position(self, dt):
        if self.cur_pos != self.cur_dest:
            mov_dist = self.max_speed * dt
            self.cur_pos[0] += mov_dist
            self.cur_pos[1] += mov_dist


class Tank(Vehicle):
    def __init__(self, team, initial_position):
        super(Tank, self).__init__(
            "tank", team, 100.0,
            100.0, 0.0, 0.0,
            250.0, 0.0, 0.0,
            initial_position
        )

