class Piece:
    def __init__(self, color):
        self.color = color
    def __repr__(self):
        return self.symbol

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♙' if self.color == 'White' else '♟'
        
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♔' if self.color == 'White' else '♚'
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♕' if self.color == 'White' else '♛'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♖' if self.color == 'White' else '♜'

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♗' if self.color == 'White' else '♝'

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♘' if self.color == 'White' else '♞'