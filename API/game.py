import random
from board import Board
from constants import *

def rand_name():
	random.seed()
	return f"{random.choice(COLORS)}_{random.choice(PLACES)}"

class Game:
	games = dict()

	def getGameBoard(id) -> Board:
		return Game.games[id].board

	def __init__(self):
		instr = rand_name()
		# makes sure that name is unique
		while instr in Game.games:
			instr = rand_name()

		self.name = instr
		self.board = Board()
		Game.games[self.name] = self
