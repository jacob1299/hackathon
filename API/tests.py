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

	print("All tests passed")
else:
	raise ValueError("Test file was imported.  That is bad.")