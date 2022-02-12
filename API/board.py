from pieces import Piece
import pieces
class Board:
    def __init__(self):
        self.b = [[None for _ in range(6)] for _ in range(6)]
    def __str__(self):
        out = ''
        for line in self.b:
            str_line = [str(animal) for animal in line]
            out += '|' + '|'.join(str_line) + '|\n'
        return out

    def make_white_side(self, edge_row: list[Piece], second_row: list[Piece]):
        for animal in edge_row:
            animal.color = "W"
        for animal in second_row:
            animal.color = "W"

        self.b[0] = edge_row
        self.b[1] = second_row
    def make_black_side(self, edge_row: list[Piece], second_row: list[Piece]):
        for animal in edge_row:
            animal.color = "B"
        for animal in second_row:
            animal.color = "B"

        self.b[5] = reversed(edge_row)
        self.b[4] = reversed(second_row)

    def get_moves(self, position: list[int]):
        x,y = position
        if (type(self.b[x,y]) is not Piece):
            return None
        animal = self.b[x,y]
        pos_moves = animal.generate_moves(position)
        actual_moves = []
        for move in pos_moves:
            x0,y0 = move
            if animal.color is not self.b[x0,y0]:
                actual_moves.append(move)
        return actual_moves

    def make_move(self, origin: list[int], destination) -> bool:
        if (destination in self.get_moves(origin)):
            x0,y0 = origin
            x1,y1 = destination
            self.b[x1,y1] = self.b[x0,y0] 
            self.b[x0,y0] = None
            return True
        else:
            print("INVALID MOVE")
            return False
        
        
    def make_default_board(self):
        S = pieces.Squirrel
        L = pieces.Lion
        edge_row = [S(), S(), S(), L(), S(), S()]
        second_row = [S(), S(), S(), S(), S(), S()]
        self.make_white_side(edge_row, second_row)
        self.make_black_side(edge_row, second_row)

def main():
    b = Board()
    b.make_default_board()
    print(b)

if __name__ == "__main__":
    main()