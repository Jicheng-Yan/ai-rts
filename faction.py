# faction.py

class Faction(object):
    def __init__(self, name, strategic_colour):
        self.name = name
        self.strategic_colour = strategic_colour


factions = {
    "EDF": Faction("Earth Defence Force", [46, 123, 211]),
    "BAK": Faction("Ba'ktul Alliance", [49, 211, 73]),
    "TYR": Faction("Tyranos Collective", [211, 49, 49])
}
