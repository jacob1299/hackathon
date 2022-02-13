from constants import *
from pieces import *
from board import *

def clean_board():
	b = Board()
	b.b = {s:None for s in SQUARES}
	return b

if __name__ == "__main__":
	#put tests here
	assert UP("a2")=="a3"
	assert all(UP(c+"6") is None for c in "abcdef")
	assert all(UP(c+r) is not None for c in "abcdef" for r in "12345")
	assert all(DOWN(c+"1") is None for c in "abcdef")
	assert all(LEFT("a"+r) is None for r in "123456")
	assert all(RIGHT("f"+r) is None for r in "123456")

	board = clean_board()
	board.b["a2"] = Ant("white")
	assert len(board.get_moves()) == 1


	board = clean_board()
	board.b["c2"] = Ant("white")
	board.b["c3"] = Ant("white")
	assert len(board.get_moves()) == 1

	board = clean_board()
	board.b["c3"] = Turtle("white")
	board.b["a1"] = Turtle("white")
	assert len(board.get_moves()) == 11

	board = clean_board()
	board.b["c4"] = Monkey("white")
	board.b["c3"] = Ant("white")
	board.b["c5"] = Ant("black")
	assert len(board.get_moves()) == 8

	board = clean_board()
	board.b["c4"] = Lion("white")
	board.b["c3"] = Ant("white")
	board.b["c5"] = Ant("black")
	assert len(board.get_moves()) == 13

	board = clean_board()
	board.b["a2"] = Squirrel("white") 
	board.b["f2"] = Squirrel("white") 
	assert len(board.get_moves()) == 4

	board = clean_board()
	board.b["b2"] = Squirrel("white") #one (NOT TWO) forward move
	board.b["b4"] = Ant("black") 
	assert len(board.get_moves()) == 1

	board = clean_board()
	board.b["b2"] = Squirrel("white") #Two forward, one take
	board.b["c3"] = Ant("black") 
	assert len(board.get_moves()) == 3

	board = clean_board()
	board.b["b2"] = Squirrel("white") #one forward, one take
	board.b["c3"] = Ant("black") 
	board.b["b3"] = Ant("black")
	assert len(board.get_moves()) == 3
	# print (board.get_moves())


	print("All tests passed")
else:
	raise ValueError("Test file was imported.  That is bad.")