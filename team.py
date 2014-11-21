# team.py

class Team(object):
	def __init__(self, name, faction):
		self.name = name
		self.faction = faction
		self.unit_list = []