from constants import *
from pieces import *
from board import *
import unittest

def clean_board():
	b = Board()
	b.b = {s:None for s in SQUARES}
	return b

class TestMoveArounds(unittest.TestCase):
	def test_move(self):
		self.assertTrue(UP("a2")=="a3")
		self.assertTrue(all(UP(c+"6") is None for c in "abcdef"))
		self.assertTrue(all(UP(c+r) is not None for c in "abcdef" for r in "12345"))
		self.assertTrue(all(DOWN(c+"1") is None for c in "abcdef"))
		self.assertTrue(all(LEFT("a"+r) is None for r in "123456"))
		self.assertTrue(all(RIGHT("f"+r) is None for r in "123456"))

class TestPieces(unittest.TestCase):
	def setUp(self) -> None:
		self.board = clean_board()

	def test_ant(self):
		board = self.board
		board.b["a2"] = Ant("white")
		self.assertEqual(len(self.board.get_moves()), 1)
	
	def test_ant2(self):
		board = self.board
		board.b["c2"] = Ant("white")
		board.b["c3"] = Ant("white")
		self.assertEqual(len(self.board.get_moves()), 1)

	def test_turtle(self):
		board = self.board
		board.b["c3"] = Turtle("white")
		board.b["a1"] = Turtle("white")
		self.assertEqual(len(board.get_moves()), 11)

	def test_monkey(self):
		board = self.board
		board.b["c4"] = Monkey("white")
		board.b["c3"] = Ant("white")
		board.b["c5"] = Ant("black")
		self.assertEqual(len(board.get_moves()), 8)

	def test_lion(self):
		board = self.board
		board.b["c4"] = Lion("white")
		board.b["c3"] = Ant("white")
		board.b["c5"] = Ant("black")
		self.assertEqual(len(board.get_moves()), 13)

	def test_squirrel1(self):
		board = self.board
		board.b["a2"] = Squirrel("white") 
		board.b["f2"] = Squirrel("white") 
		self.assertEqual(len(board.get_moves()), 4)

	def test_squirrel2(self):
		board = self.board
		board.b["b2"] = Squirrel("white") #one (NOT TWO) forward move
		board.b["b4"] = Ant("black") 
		self.assertEqual(len(board.get_moves()), 1)

	def test_squirrel3(self):
		board = self.board
		board.b["b2"] = Squirrel("white") #Two forward, one take
		board.b["c3"] = Ant("black") 
		self.assertEqual(len(board.get_moves()), 3)

	def test_squirrel4(self):
		board = self.board
		board.b["b2"] = Squirrel("white") #one forward, one take
		board.b["c3"] = Ant("black") 
		board.b["b4"] = Ant("black")
		self.assertEqual(len(board.get_moves()), 2)


if __name__ == '__main__':
    unittest.main()
# else:
# 	raise ValueError("Test file was imported.  That is bad.")