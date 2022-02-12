class Piece:
    def __init__(self, name, color):
        # name of piece 
        self.name = name
        # black or white 
        self.color = color
    def generate_moves(self, deltas: list[int], position: list[int]) -> list[list[int]]:
        pos_moves = []
        y0, x0 = position
        for dy,dx in deltas:
            x1 = x0 + dx
            y1 = y0 + dy
            if inBoard(x1,y1):
                pos_moves.append([x1,y1])
        return pos_moves

    def __str__(self) -> str:
        return self.name[:4] + ": " + self.color

class Squirrel(Piece):
    def __init__(self, color=None):
        super().__init__('Squirrel', color)
    def generate_moves(self, position: list[int]):
        deltas = [[0, 1], [0, 2]]
        return super().generate_moves(deltas, position)
        
    def __str__(self) -> str:
        return super().__str__()

class Lion(Piece):
    def __init__(self, color=None):
        super().__init__('Lion', color)
    def generate_moves(self, position: list[int]):
        deltas = [[1,0],[-1,0],[0,1],[0,-1]]
        return super().generate_moves(deltas, position)

    def __str__(self) -> str:
        return super().__str__()

def inBoard(x,y):
    return 0 <= x <= 5 and 0 <= y <= 5