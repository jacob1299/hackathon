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

class TestMovePieces(unittest.TestCase):
	def setUp(self) -> None:
		self.board = Board()
		self.board.state = PLAYING

	def test_ant_move(self):
		self.board.make_move('a2', 'a3')
		self.assertEqual(self.board.b['a2'], None)
		self.assertEqual(type(self.board.b['a3']),Ant)
	def test_ant_bad_move(self):
		self.board.make_move('a2', 'a4')
		self.assertEqual(type(self.board.b['a2']),Ant)
		self.assertEqual(self.board.b['a4'], None)

	def test_monkey_friendly_move(self):
		self.board.b['a1'] = Monkey('white')
		self.assertTrue(self.board.make_move('a1', 'a2'))
		self.assertEqual(type(self.board.b['a2']),Monkey)
		self.assertEqual(type(self.board.b['a1']),Ant)

	def test_monkey_enemy_move(self):
		self.board.b['a6'] = Monkey('white')
		self.assertTrue(self.board.make_move('a6', 'a5'))
		self.assertEqual(type(self.board.b['a5']),Monkey)
		self.assertEqual(self.board.b['a6'], None)

	def test_bee_enemy_move(self):
		self.board.b['a6'] = Bee('white')
		self.assertTrue(self.board.make_move('a6', 'a5'))
		self.assertEqual(self.board.b['a5'], None)
		self.assertEqual(self.board.b['a6'], None)

	def test_bee_blank_move(self):
		self.board.b['a4'] = Bee('white')
		self.assertTrue(self.board.make_move('a4', 'a3'))
		self.assertEqual(self.board.b['a4'], None)
		self.assertEqual(type(self.board.b['a3']),Bee)



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
	
	def test_ant3(self):
		board = self.board
		board.b["c2"] = Ant("white")
		board.b["d3"] = Ant("black")
		self.assertEqual(len(self.board.get_moves()), 2)

	def test_swan1(self):
		board = self.board
		board.b["c2"] = Swan("white")
		self.assertEqual(len(self.board.get_moves()), 4)

	def test_swan2(self):
		board = self.board
		board.b["c3"] = Swan("white")
		self.assertEqual(len(self.board.get_moves()), 3)
	
	## arguably this should be 3, but swans can jump because they're upgraded
	def test_swan3(self):
		board = self.board
		board.b["c2"] = Swan("white")
		board.b["c3"] = Ant("black")
		self.assertEqual(len(self.board.get_moves()), 4)

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

	def test_bee(self):
		board = self.board
		board.b["c4"] = Bee("white")
		board.b["c5"] = Bee("white")
		self.assertEqual(len(board.get_moves()), 14)

	def test_fox(self):
		board = self.board
		board.b["c4"] = Fox("white")
		board.b["c5"] = Fox("black")
		self.assertEqual(len(board.get_moves()),9)

	def test_tiger(self):
		board = self.board
		board.b["c4"] = Tiger("white")
		board.b["c5"] = Tiger("black")
		self.assertEqual(len(board.get_moves()), 18)

	def test_rabbit(self):
		board = self.board
		board.b["b5"] = Rabbit("white")
		board.b["a6"] = Rabbit("white")
		#print (len(board.get_moves()))
		self.assertEqual(len(board.get_moves()), 4)

	def test_hyena(self):
		board = self.board
		board.b["d3"] = Hyena("white")
		board.b["a6"] = Hyena("white")
		board.b["c2"] = Ant("black")
		self.assertEqual(len(board.get_moves()), 9)

	def test_mouse(self):
		board = self.board
		board.b["d3"] = Mouse("white")
		board.b["e4"] = Mouse("white")
		board.b["c2"] = Ant("black")
		self.assertEqual(len(board.get_moves()), 14)

	def test_shark(self):
		board = self.board
		board.b["a1"] = Shark("white")
		board.b["a6"] = Shark("white")
		board.b["c2"] = Ant("white")
		board.b["c3"] = Ant("black")
		#print (len(board.get_moves()))
		self.assertEqual(len(board.get_moves()), 3)

	def test_kangaroo(self):
		board = self.board
		board.b["a1"] = Kangaroo("white")
		board.b["a6"] = Kangaroo("white")
		board.b["c2"] = Ant("white")
		board.b["c3"] = Ant("black")
		self.assertEqual(len(board.get_moves()), 9)


if __name__ == '__main__':
	unittest.main()
# else:
# 	raise ValueError("Test file was imported.  That is bad.")