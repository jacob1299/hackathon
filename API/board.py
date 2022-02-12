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
        white_edge = []
        for animal in edge_row:
            animal.color = "W"
            white_edge.append(animal)

        white_second = []
        for animal in second_row:
            animal.color = "W"
            white_second.append(animal)

        self.b[0] = white_edge
        self.b[1] = white_second

    def make_black_side(self, edge_row: list[Piece], second_row: list[Piece]):
        black_edge = []
        for animal in edge_row:
            animal.color = "B"
            black_edge.append(animal)

        black_second = []
        for animal in second_row:
            animal.color = "B"
            black_second.append(animal)


        self.b[5] = list(reversed(black_edge))
        self.b[4] = list(reversed(black_second))

    def get_moves(self, position: list[int]):
        y,x = position
        if (not issubclass(type(self.b[x][y]), Piece)):
            print(f"Was {type(self.b[x][y])}, not Piece")
            return None
        animal = self.b[x][y]
        pos_moves = animal.generate_moves(position)
        actual_moves = []
        for move in pos_moves:
            y0,x0 = move
            if (self.b[x0][y0] and animal.color == self.b[x0][y0].color ):
                print(f"animal: {animal.color}, other: {self.b[x0][y0].color}")
            else:
                # print(f"animal: {animal.color}, other: {self.b[x0][y0].color}")
                actual_moves.append(move)
                
        return actual_moves

    def make_move(self, origin: list[int], destination) -> bool:
        if (destination in self.get_moves(origin)):
            y0,x0 = origin
            y1,x1 = destination
            self.b[x1][y1] = self.b[x0][y0] 
            self.b[x0][y0] = None
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
        
        edge_row2 = [S(), S(), S(), L(), S(), S()]
        second_row2 = [S(), S(), S(), S(), S(), S()]
        self.make_black_side(edge_row2, second_row2)

def main():
    b = Board()
    b.make_default_board()
    print(b)

    origin = [0,1]
    moves = b.get_moves(origin)
    print(moves)
    b.make_move(origin, moves[0])
    print(b)


if __name__ == "__main__":
    main()