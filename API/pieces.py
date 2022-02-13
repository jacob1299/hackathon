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
def UP2(instr):
    return UP(UP(instr))
def DOWN2(instr):
    return DOWN(DOWN(instr))
def LEFT2(instr):
    return LEFT(LEFT(instr))
def RIGHT2(instr):
    return RIGHT(RIGHT(instr))
def UPRIGHT2(instr):
    return UPRIGHT(UPRIGHT(instr))
def UPLEFT2(instr):
    return UPLEFT(UPLEFT(instr))
def DOWNRIGHT2(instr):
    return DOWNRIGHT(DOWNRIGHT(instr))
def DOWNLEFT2(instr):
    return DOWNLEFT(DOWNLEFT(instr))
def UUL(instr):
    return UP(UP(LEFT(instr)))
def UUR(instr):
    return UP(UP(RIGHT(instr)))
def ULL(instr):
    return UP(LEFT(LEFT(instr)))
def URR(instr):
    return UP(RIGHT(RIGHT(instr)))
def DDL(instr):
    return DOWN(DOWN(LEFT(instr)))
def DDR(instr):
    return DOWN(DOWN(RIGHT(instr)))
def DLL(instr):
    return DOWN(LEFT(LEFT(instr)))
def DRR(instr):
    return DOWN(RIGHT(RIGHT(instr)))

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
				moves.append(MOVE(current_square, target[0](current_square)))
		for delta in self.deltas:	#delta = [function, limit]
			sqr = delta[0](current_square)
			i=1
			while sqr is not None and sqr in squares[EMPTY] and i<=delta[1]:
				moves.append(MOVE(current_square, sqr))
				sqr = delta[0](sqr)
				i += 1
			if sqr in squares[ENEMY] and i<=delta[1]:
				moves.append(MOVE(current_square, sqr))


	def __str__(self) -> str:
		return self.name[:4] + ": " + self.color

class Ant(Piece):
	def __init__(self, color):
		super().__init__("Ant", color)
		self.targets = [(UP if color == "white" else DOWN, EMPTY), (UPLEFT if color == "white" else DOWNLEFT, ENEMY), (UPRIGHT if color == "white" else DOWNRIGHT, ENEMY)]
		self.deltas  = []

class Squirrel(Piece):
	def __init__(self, color):
		super().__init__("Squirrel", color)
		self.targets = [(UPLEFT if color == "white" else DOWNLEFT, ENEMY), (UPRIGHT if color == "white" else DOWNRIGHT, ENEMY)]
		self.deltas  = []
	def generate_moves(self, moves, current_square, squares):
		# get possible take moves using Piece method
		self.deltas  = []
		super().generate_moves(moves, current_square, squares)

		# If we are on the starting position
		if self.color == "white" and current_square[1] == "2":
			self.deltas = [(UP, 2)]
		elif self.color == "black" and current_square[1] == "5":
			self.deltas = [(DOWN, 2)]

		# same as generate moves in piece, but it doen't allow you to take on a delta move
		# this appends to the take moves from the piece method 
		for delta in self.deltas:	#delta = [function, limit]
				sqr = delta[0](current_square)
				i=1
				while sqr is not None and sqr in squares[EMPTY] and i<=delta[1]:
					moves.append(MOVE(current_square, sqr))
					sqr = delta[0](sqr)
					i += 1

class Turtle(Piece):
	def __init__(self, color):
		super().__init__("Turtle", color)
		self.targets = [(UP, EMPTY | ENEMY),(DOWN, EMPTY | ENEMY),(LEFT, EMPTY | ENEMY),(RIGHT, EMPTY | ENEMY), 
			(UPLEFT, EMPTY | ENEMY),(DOWNLEFT, EMPTY | ENEMY),(UPRIGHT, EMPTY | ENEMY),(DOWNRIGHT, EMPTY | ENEMY)]
		self.deltas  = []

class Monkey(Piece):
	def __init__(self, color):
		super().__init__("Monkey", color)
		self.targets = [(UP, EMPTY | ENEMY | ALLY),(DOWN, EMPTY | ENEMY | ALLY),(LEFT, EMPTY | ENEMY | ALLY),(RIGHT, EMPTY | ENEMY | ALLY), 
			(UPLEFT, EMPTY | ENEMY | ALLY),(DOWNLEFT, EMPTY | ENEMY | ALLY),(UPRIGHT, EMPTY | ENEMY | ALLY),(DOWNRIGHT, EMPTY | ENEMY | ALLY)]
		self.deltas  = []

class Lion(Piece):
	def __init__(self, color):
		super().__init__("Lion", color)
		self.targets = []
		self.deltas  = [(UP, 2), (DOWN,2), (LEFT, 2), (RIGHT, 2), (UPRIGHT, 2), (DOWNLEFT,2), (UPLEFT, 2), (DOWNRIGHT, 2)]

class Bee(Piece):
    def init(self, color):
        super().init("Bee", color)
        self.targets = []
        self.deltas = [(UP, 10), (DOWN, 10), (LEFT, 10), (RIGHT, 10)]

class Fox(Piece):
    def init(self, color):
        super().init("Fox", color)
        self.targets = []
        self.deltas = [(UP, 10), (DOWN, 10), (LEFT, 10), (RIGHT, 10)]

class Tiger(Piece):
    def init(self, color):
        super().init("Tiger", color)
        self.targets = []
        self.deltas = [(UP, 10), (DOWN, 10), (LEFT, 10), (RIGHT, 10), (UPRIGHT, 10), (DOWNLEFT,10), (UPLEFT, 10), (DOWNRIGHT, 10)]
class Rabbit(Piece):
    def init(self, color):
        super().init("Rabbit", color)
        self.targets = []
        self.deltas = [(UPRIGHT, 2), (DOWNLEFT, 2), (UPLEFT, 2), (DOWNRIGHT, 2)]

class Hyena(Piece):
    def init(self, color):
        super().init("Hyena", color)
        self.targets = []
        self.deltas = [(UPRIGHT, 10), (DOWNLEFT, 10), (UPLEFT, 10), (DOWNRIGHT, 10)]

class Mouse(Piece):
    def init(self, color):
        super().init("Mouse", color)
        self.targets = []
        self.deltas = [(UP2, EMPTY | ENEMY), (DOWN2, EMPTY | ENEMY), (LEFT2, EMPTY | ENEMY), (RIGHT2, EMPTY | ENEMY), (UPRIGHT2, EMPTY | ENEMY), (UPLEFT2, EMPTY | ENEMY), (DOWNRIGHT2, EMPTY | ENEMY), (DOWNLEFT2, EMPTY | ENEMY)]

class Shark(Piece):
    def init(self, color):
        super().init("Shark", color)
        self.targets = [(UUR, EMPTY | ENEMY), (UUL, EMPTY | ENEMY), (URR, EMPTY | ENEMY), (ULL, EMPTY | ENEMY), (DDR, EMPTY | ENEMY), (DDL, EMPTY | ENEMY), (DRR, EMPTY | ENEMY), (DLL, EMPTY | ENEMY)]
        self.deltas = []

class Kangaroo(Piece):
    def init(self, color):
        super().init("Kangaroo", color)
        self.targets = [(UP, EMPTY | ENEMY),(DOWN, EMPTY | ENEMY),(LEFT, EMPTY | ENEMY),(RIGHT, EMPTY | ENEMY), 
            (UPLEFT, EMPTY | ENEMY),(DOWNLEFT, EMPTY | ENEMY),(UPRIGHT, EMPTY | ENEMY),(DOWNRIGHT, EMPTY | ENEMY),
            (UUR, EMPTY | ENEMY), (UUL, EMPTY | ENEMY), (URR, EMPTY | ENEMY), (ULL, EMPTY | ENEMY), (DDR, EMPTY | ENEMY), (DDL, EMPTY | ENEMY), (DRR, EMPTY | ENEMY), (DLL, EMPTY | ENEMY)]
        self.deltas = []
