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


## Checkers ##

class Piece():
    def __init__(self, color):
        if color == 'b':
            self.color = B_PEASANT
        elif color == 'w':
            self.color = W_PEASANT
        else:
            self.color = None
            print("Invalid color")
        self.value = 1
    
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
        self.value = 2

    def __repr__(self):
        return self.color


## Chess ##

class ChessPiece():
    def __init__(self):
        self.value = 0

    def possible_moves(self, board:CheckerBoard, piece:str):
        pass

    def get_value(self):
        return self.value


class Pawn(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.type = B_CHESS_PAWN
            self.color = 'b'
        elif color == 'w':
            self.type = W_CHESS_PAWN
            self.color = 'w'
        self.value = 1

    def __repr__(self):
        return self.color

    def possible_moves(self, board:CheckerBoard, piece):
        coord = board.convert_checker_coord(piece)
        piece_color = str(board[coord[0]][coord[1]])
        p_basic_moves = []

        if piece_color == 'b':
            basic_movement = (1, 0)
            capture_movement = [(1, 1), (1, -1)]
        elif piece_color == 'w':
            basic_movement = (-1, 0)
            capture_movement = [(-1, 1), (-1, -1)]

        if board.has_piece(board[coord[0] + basic_movement[0]][coord[1]]):
            # if piece right in front
            return p_basic_moves
        elif not board.has_piece(board[coord[0] + basic_movement[0]*2][coord[1]]):
            # if no piece two spaces in front
            if piece_color == "b" and coord[0] == 1:
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0], coord[1])), 0))
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0]*2, coord[1])), 0))
            elif piece_color == "w" and coord[0] == 6:
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0], coord[1])), 0))
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0]*2, coord[1])), 0))

        for move in capture_movement:
            if board.has_piece(board[coord[0] + move[0]][coord[1] + move[1]]) and \
                not board.is_current_player_piece(board[coord[0] + move[0]][coord[1] + move[1]]):
                # if captureable piece diagonally in front
                p_basic_moves.append(
                    (board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[0])), \
                        board[coord[0] + move[0]][coord[1] + move[1]].get_value()))
        
        return p_basic_moves


class Knight(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.color = B_CHESS_KNIGHT
        elif color =='w':
            self.color = W_CHESS_KNIGHT
    def __repr__(self):
        return self.color

class Bishop(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.color = B_CHESS_BISHOP
        elif color =='w':
            self.color = W_CHESS_BISHOP
    def __repr__(self):
        return self.color

class Rook(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.color = B_CHESS_ROOK
        elif color =='w':
            self.color = W_CHESS_ROOK
    def __repr__(self):
        return self.color

class Queen(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.color = B_CHESS_QUEEN
        elif color == 'w':
            self.color = W_CHESS_QUEEN
    def __repr__(self):
        return self.color

class ChessKing(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.color = B_CHESS_KING
        elif color =='w':
            self.color = W_CHESS_KING
    def __repr__(self):
        return self.color
