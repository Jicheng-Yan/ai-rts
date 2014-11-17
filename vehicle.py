from math import sqrt, sin, cos


class Vehicle(object):
    def __init__(
        self, unit_type, faction, team, map_ref, dt,
        position, max_speed, radius, hit_points
    ):
        self.unit_type = unit_type
        self.faction = faction  # Unit/structure set
        self.team = team  # Playable/AI Team
        self.map_ref = map_ref  # Map reference
        self.dt = dt  # Timestep

        self.max_speed = max_speed  # Metres/second
        self.radius = radius  # Metres
        self.hit_points = hit_points  # Total health
        self.max_mov_dist = self.max_speed * self.dt

        self.cur_speed = 0.0  # Metres/second
        self.cur_health = hit_points  # Percent
        self.cur_pos = position  # Current x, y co-ords
        self.cur_dest = position  # Destination x, y co-ords

    def set_destination(self, new_pos):
        self.cur_dest = new_pos

    def update_position(self):
        if self.cur_pos != self.cur_dest:
            mov_dist = self.max_speed * self.dt
            self.cur_pos[0] += self.max_mov_dist
            self.cur_pos[1] += self.max_mov_dist


class Tank(Vehicle):
    def __init__(self, team, map_ref, dt):
        super(Tank, self).__init__(
            "tank", "faction1", team,
            map_ref, dt, [0.0, 0.0], 10.0,
            3.0, 1000
        )

