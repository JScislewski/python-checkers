from .constants import BLACK, WHITE


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == WHITE:
            self.direction = -1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
