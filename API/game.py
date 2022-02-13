import random
from constants import *

def rand_name():
	random.seed()
	return f"{random.choice(COLORS)}_{random.choice(PLACES)}"

class Game:
	games = dict()
	def __init__(self):
		instr = rand_name()
		while instr in Game.games:
			instr = rand_name()
		self.name = instr
		self.board = Board()
		Game.games[self.name] = self
