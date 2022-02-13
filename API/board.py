from pieces import *
from constants import *

class Board:
	def __init__(self):
		self.turn = "white"
		self.b = {s:None for s in SQUARES}
		for c in "abcdef":	#Add Ants
			self.b[c+"2"] = Ant("white")
			self.b[c+"5"] = Ant("black")

	def __str__(self):
		out = ''
		for line in self.b:
			str_line = [str(animal) for animal in line]
			out += '|' + '|'.join(str_line) + '|\n'
		return out
	
	def for_json(self):
		out = dict()
		for position, piece in self.b.items():
			out[position] = str(piece) if piece else ""
		return out
			

	def get_moves(self):
		blank_squares = {s for s in SQUARES if self.b[s] is None}
		ally_squares  = {s for s in SQUARES if self.b[s] is not None and self.b[s].color == self.turn}
		enemy_squares = {s for s in SQUARES if self.b[s] is not None and self.b[s].color != self.turn}
		assert (len(blank_squares) + len(ally_squares) + len(enemy_squares)) == len(SQUARES)
		square_types = {
			EMPTY: blank_squares,
			ALLY: ally_squares,
			ENEMY: enemy_squares,
			EMPTY | ALLY: blank_squares.union(ally_squares),
			EMPTY | ENEMY: blank_squares.union(enemy_squares),
			ALLY | ENEMY: ally_squares.union(enemy_squares),
			EMPTY | ALLY | ENEMY: ally_squares.union(enemy_squares).union(blank_squares)
		}
		moves = []
		for square in SQUARES:
			if self.b[square] is not None and self.b[square].color == self.turn:
				self.b[square].generate_moves(moves, square, square_types)
		return moves

	def set_pieces(self, data: dict[str: str], color: str):
		columns = range(1,3) if color == "white" else range(5,7)
		for num in columns:
			for letter in "abcedf":
				pos = letter + str(num)
				if data[pos] == '':
					self.b[pos] = None
				else:
					self.b[pos] = parseName(data[pos])(color)
	
	def swap_turns(self):
		self.turn = "white" if self.turn == "black" else "black"