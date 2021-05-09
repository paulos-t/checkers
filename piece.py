B_PEASANT = '\u2688'
W_PEASANT = '\u2686'
B_KING = '\u2689'
W_KING = '\u2687'

W_CHESS_KING = '\u2654'
W_CHESS_QUEEN = '\u2655'
W_CHESS_ROOK = '\u2656'
W_CHESS_BISHOP ='\u2657'
W_CHESS_KNIGHT = '\u2658'
W_CHESS_PAWN = '\u2659'


B_CHESS_KING = '\u265A'
B_CHESS_QUEEN = '\u265B'
B_CHESS_ROOK = '\u265C'
B_CHESS_BISHOP = '\u265D'
B_CHESS_KNIGHT = '\u265E'
B_CHESS_PAWN = '\u265F'

class Piece():

    def __init__(self, color):
        if color == 'b':
            self.color = B_PEASANT
        elif color == 'w':
            self.color = W_PEASANT
        else:
            self.color = None
            print("Invalid color")


    
    def __repr__(self):
        return self.color


class King(Piece):

    def __init__(self, color):
        if color == 'b':
            self.color = B_KING
        elif color == 'w':
            self.color = W_KING
        else:
            self.color = None
            print("Invalid color")


    def __repr__(self):
        return self.color






class Pawn():
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_PAWN
        elif color == 'w':
            self.color = W_CHESS_PAWN
    def __repr__(self):
        return self.color

class Knight():
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_KNIGHT
        elif color =='w':
            self.color = W_CHESS_KNIGHT
    def __repr__(self):
        return self.color

class Bishop():
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_BISHOP
        elif color =='w':
            self.color = W_CHESS_BISHOP
    def __repr__(self):
        return self.color

class Rook():
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_ROOK
        elif color =='w':
            self.color = W_CHESS_ROOK
    def __repr__(self):
        return self.color

class Queen():
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_QUEEN
        elif color == 'w':
            self.color = W_CHESS_QUEEN
    def __repr__(self):
        return self.color

class ChessKing():
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_KING
        elif color =='w':
            self.color = W_CHESS_KING
    def __repr__(self):
        return self.color





            




