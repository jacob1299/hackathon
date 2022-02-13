from constants import *

def UP(instr):
	return None if instr is None or instr[1]=="6" else instr[0]+str(int(instr[1])+1)
def DOWN(instr):
	return None if instr is None or instr[1]=="1" else instr[0]+str(int(instr[1])-1)
def LEFT(instr):
	return None if instr is None or instr[0]=="a" else chr(ord(instr[0])-1)+instr[1]
def RIGHT(instr):
	return None if instr is None or instr[0]=="f" else chr(ord(instr[0])+1)+instr[1]
def UPLEFT(instr):
	return UP(LEFT(instr))
def UPRIGHT(instr):
	return UP(RIGHT(instr))
def DOWNLEFT(instr):
	return DOWN(LEFT(instr))
def DOWNRIGHT(instr):
	return DOWN(RIGHT(instr))

def MOVE(current_square, target_square):
	return {"from": current_square, "to": target_square}

class Piece:
	def __init__(self, name, color):
		# name of piece 
		self.name = name
		# black or white 
		self.color = color

	#default move handling.  For custom move handling for a piece, override this function
	def generate_moves(self, moves, current_square, squares):
		for target in self.targets:	#target = [function, square_type]
			if target[0](current_square) in squares[target[1]]:
				moves.append(MOVE(current_square, target_square))
		for delta in self.deltas:	#delta = [function, limit]
			sqr = delta[0](current_square)
			i=1
			while sqr is not None and sqr in squares[EMPTY] and i<=limit:
				moves.append(MOVE(current_square, sqr))
				sqr = delta[0](sqr)
				i += 1
			if sqr in squares[ENEMY] and i<=limit:
				moves.append(MOVE(current_square, sqr))


	def __str__(self) -> str:
		return self.name[:4] + ": " + self.color

class Ant(Piece):
	def __init__(self, color):
		super.__init__("Ant", color)
		self.targets = [(UP if color == "white" else DOWN, EMPTY), (UPLEFT if color == "white" else DOWNLEFT, ENEMY), (UPRIGHT if color == "white" else DOWNRIGHT, ENEMY)]
		self.deltas  = []

def inBoard(x,y):
	return 0 <= x <= 5 and 0 <= y <= 5