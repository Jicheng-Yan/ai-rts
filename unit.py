# unit.py

import pygame

import settings


class Unit(object):
    def __init__(
        self, unit_type, faction, team, 
        hit_points, mass_build_cost, 
        mass_generate_rate, mass_bleed_rate,
        energy_build_cost, energy_generate_rate,
        energy_bleed_rate, position
    ):
        self.unit_type = unit_type
        self.faction = faction  # Unit/structure set
        self.team = team  # Playable/AI Team
        self.hit_points = hit_points  # Total health

        self.mass_build_cost = mass_build_cost
        self.mass_generate_rate = mass_generate_rate
        self.mass_bleed_rate = mass_bleed_rate
        self.energy_build_cost = energy_build_cost
        self.energy_generate_rate = energy_generate_rate
        self.energy_bleed_rate =energy_bleed_rate

        self.cur_health = hit_points  # Percent
        self.cur_pos = position  # Current x, y co-ords

    def draw_strategic_icon(self, screen):
        # TODO: This would be better handled with sprites
        x = self.cur_pos[0]
        y = self.cur_pos[1]
        pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(x, y, 11, 11))
        pygame.draw.rect(
            screen, settings.STRATEGIC_COLOURS[self.faction], 
            pygame.Rect(x+1, y+1, 9, 9)
        )


class MassExtractor(Unit):
    def __init__(self, faction, team, position):
        super(MassExtractor, self).__init__(
            "mass_extractor", faction, team,
            100, 250.0, 1.0, 0.0, 
            500.0, 0.0, 5.0, position
        )

    def draw_strategic_icon(self, screen):
        x = self.cur_pos[0]
        y = self.cur_pos[1]
        super(MassExtractor, self).draw_strategic_icon(
            screen
        )
        screen.set_at((x+4, y+3), [0, 0, 0])
        screen.set_at((x+5, y+3), [0, 0, 0])
        screen.set_at((x+6, y+3), [0, 0, 0])
        screen.set_at((x+3, y+4), [0, 0, 0])
        screen.set_at((x+7, y+4), [0, 0, 0])
        screen.set_at((x+3, y+5), [0, 0, 0])
        screen.set_at((x+4, y+5), [0, 0, 0])
        screen.set_at((x+6, y+5), [0, 0, 0])
        screen.set_at((x+7, y+5), [0, 0, 0])
        screen.set_at((x+5, y+7), [0, 0, 0])


class PowerStation(Unit):
    def __init__(self, faction, team, position):
        super(PowerStation, self).__init__(
            "power_station", faction, team,
            100, 150.0, 0.0, 0.0, 
            500.0, 25.0, 5.0, position
        )

    def draw_strategic_icon(self, screen):
        x = self.cur_pos[0]
        y = self.cur_pos[1]
        super(PowerStation, self).draw_strategic_icon(
            screen
        )
        screen.set_at((x+4, y+3), [0, 0, 0])
        screen.set_at((x+5, y+4), [0, 0, 0])
        screen.set_at((x+4, y+5), [0, 0, 0])
        screen.set_at((x+5, y+5), [0, 0, 0])
        screen.set_at((x+6, y+5), [0, 0, 0])
        screen.set_at((x+5, y+6), [0, 0, 0])
        screen.set_at((x+6, y+7), [0, 0, 0])


class LandFactory(Unit):
    pass


class PointDefence(Unit):
    pass
    

class Artillery(Unit):
    pass


class ShortRangeArtillery(Artillery):
    pass


class LongRangeArtillery(Artillery):
    pass
