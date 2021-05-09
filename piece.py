from board import CheckerBoard
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





class ChessPiece():
    # def __init__(self):
    #     coord = board.convert_checker_coord(piece)
    #     piece_color = str(board[coord[0]][coord[1]])
    #     p_basic_moves = []
    def possible_move(self, board:CheckerBoard, piece:str):
        pass









class Pawn(ChessPiece):
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_PAWN
            self.type = 'b'
        elif color == 'w':
            self.color = W_CHESS_PAWN
            self.type = 'w'
    def __repr__(self):
        return self.type


    def possible_move(self, board, piece):
        coord = board.convert_checker_coord(piece)
        piece_type = str(board[coord[0]][coord[1]])
        p_basic_moves = []
        if piece_type == 'b':
            if board.has_piece(board[coord[0]+1][coord[1]]):
                if coord[0] == 1:
                    p_basic_moves.append(())
        

            






class Knight(ChessPiece):
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_KNIGHT
        elif color =='w':
            self.color = W_CHESS_KNIGHT
    def __repr__(self):
        return self.color

class Bishop(ChessPiece):
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_BISHOP
        elif color =='w':
            self.color = W_CHESS_BISHOP
    def __repr__(self):
        return self.color

class Rook(ChessPiece):
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_ROOK
        elif color =='w':
            self.color = W_CHESS_ROOK
    def __repr__(self):
        return self.color

class Queen(ChessPiece):
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_QUEEN
        elif color == 'w':
            self.color = W_CHESS_QUEEN
    def __repr__(self):
        return self.color

class ChessKing(ChessPiece):
    def __init__(self,color):
        if color == 'b':
            self.color = B_CHESS_KING
        elif color =='w':
            self.color = W_CHESS_KING
    def __repr__(self):
        return self.color





            




