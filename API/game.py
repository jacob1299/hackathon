import random
from board import Board
from constants import *

def rand_name():
	random.seed()
	return f"{random.choice(COLORS)}_{random.choice(PLACES)}"

class Game:
	games = dict()

	def getGameBoard(id):
		return Game.games[id].board

	def __init__(self, color, ante, user):
		instr = rand_name()
		# makes sure that name is unique
		while instr in Game.games:
			print("new name")
			instr = rand_name()

		self.id = instr
		self.board = Board()
		self.ante = ante
		self.players = [user, ""] if color=="white" else ["", user]
		Game.games[self.id] = self

	def get_link(self):
		return f"34.75.42.233:5000/game&id={self.id}"