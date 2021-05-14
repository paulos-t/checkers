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
            self.type = B_PEASANT
        elif color == 'w':
            self.color = W_PEASANT
            # self.type = W_PEASANT
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
            self.type = B_KING
        elif color == 'w':
            self.color = W_KING
            self.type = W_KING
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

    def possible_moves(self, board, piece:str):
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
        return self.type

    def possible_moves(self, board, piece):
        coord = board.convert_checker_coord(piece)
        piece_color = board.board[coord[0]][coord[1]].color
        p_basic_moves = []

        if piece_color == 'b':
            basic_movement = (1, 0)
            capture_movement = [(1, 1), (1, -1)]
        elif piece_color == 'w':
            basic_movement = (-1, 0)
            capture_movement = [(-1, 1), (-1, -1)]

        if board.has_piece(board.convert_matrix_coord((coord[0] + basic_movement[0], coord[1]))):
            # if piece right in front
            return p_basic_moves
        elif (piece_color == "b" and coord[0] == 1) or (piece_color == "w" and coord[0] == 6):
            # if in starting row
            if not board.has_piece(board.convert_matrix_coord((coord[0] + basic_movement[0]*2, coord[1]))):
                # if no piece two spaces in front
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0], coord[1])), 0))
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0]*2, coord[1])), 0))
        else:
            p_basic_moves.append((board.convert_matrix_coord((coord[0] + basic_movement[0], coord[1])), 0))

        for move in capture_movement:
            if coord[0] + move[0] > 7 or coord[0] + move[0] < 0 or coord[1] + move[1] > 7 or coord[1] + move[1] < 0:
                continue
            if board.has_piece(board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1]))) and \
                not board.is_current_player_piece(board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1]))):
                # if captureable piece diagonally in front
                p_basic_moves.append(
                    (board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1])), \
                        board.board[coord[0] + move[0]][coord[1] + move[1]].get_value()))
        
        return p_basic_moves


class Knight(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.type = B_CHESS_KNIGHT
            self.color = 'b'
        elif color == 'w':
            self.type = W_CHESS_KNIGHT
            self.color = 'w'
        self.value = 3

    def __repr__(self):
        return self.type

    def possible_moves(self, board, piece):
        coord = board.convert_checker_coord(piece)
        p_basic_moves = []

        movement = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        for move in movement:
            if coord[0] + move[0] > 7 or coord[0] + move[0] < 0 or coord[1] + move[1] > 7 or coord[1] + move[1] < 0:
                continue
            elif not board.has_piece(board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1]))):
                p_basic_moves.append((board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1])), 0))
            elif board.has_piece(board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1]))) and \
                not board.is_current_player_piece(board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1]))):
                p_basic_moves.append(
                    (board.convert_matrix_coord((coord[0] + move[0], coord[1] + move[1])), \
                        board.board[coord[0] + move[0]][coord[1] + move[1]].get_value()) )
        return p_basic_moves


class Bishop(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.type = B_CHESS_BISHOP
            self.color = 'b'
        elif color == 'w':
            self.type = W_CHESS_BISHOP
            self.color = 'w'
        self.value = 3

    def __repr__(self):
        return self.type

    def possible_moves(self, board, piece):
        coord = board.convert_checker_coord(piece)
        p_basic_moves = []

        movement = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in movement:
            temp_coord = [coord[0], coord[1]]
            while True:
                if temp_coord[0] + direction[0] > 7 or temp_coord[0] + direction[0] < 0 or \
                    temp_coord[1] + direction[1] > 7 or temp_coord[1] + direction[1] < 0:
                    # if goes off the board
                    break
                temp_coord[0] = temp_coord[0] + direction[0]
                temp_coord[1] = temp_coord[1] + direction[1]
                if not board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                    # if empty space
                    p_basic_moves.append((board.convert_matrix_coord((temp_coord[0], temp_coord[1])), 0))
                elif board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))) and \
                    board.is_current_player_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                    # if capture available
                    p_basic_moves.append(
                        (board.convert_matrix_coord((temp_coord[0], temp_coord[1])), \
                            board.board[temp_coord[0]][temp_coord[1]].get_value()) )
                    break
                else:
                    # if own piece blocking path
                    break
        return p_basic_moves


class Rook(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.type = B_CHESS_ROOK
            self.color = 'b'
        elif color == 'w':
            self.type = W_CHESS_ROOK
            self.color = 'w'
        self.value = 5

    def __repr__(self):
        return self.type

    def possible_moves(self, board, piece):
        coord = board.convert_checker_coord(piece)
        p_basic_moves = []

        movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in movement:
            temp_coord = [coord[0], coord[1]]
            while True:
                if temp_coord[0] + direction[0] > 7 or temp_coord[0] + direction[0] < 0 or \
                    temp_coord[1] + direction[1] > 7 or temp_coord[1] + direction[1] < 0:
                    # if goes off the board
                    break
                temp_coord[0] = temp_coord[0] + direction[0]
                temp_coord[1] = temp_coord[1] + direction[1]
                if not board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                    # if empty space
                    p_basic_moves.append((board.convert_matrix_coord((temp_coord[0], temp_coord[1])), 0))
                elif board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))) and \
                    not board.is_current_player_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                    # if capture available
                    p_basic_moves.append(
                        (board.convert_matrix_coord((temp_coord[0], temp_coord[1])), \
                            board.board[temp_coord[0]][temp_coord[1]].get_value()) )
                    break
                else:
                    # if own piece blocking path
                    break
        return p_basic_moves


class Queen(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.type = B_CHESS_QUEEN
            self.color = 'b'
        elif color == 'w':
            self.type = W_CHESS_QUEEN
            self.color = 'w'
        self.value = 9

    def __repr__(self):
        return self.type

    def possible_moves(self, board, piece):
        coord = board.convert_checker_coord(piece)
        p_basic_moves = []

        movement = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in movement:
            temp_coord = [coord[0], coord[1]]
            while True:
                if temp_coord[0] + direction[0] > 7 or temp_coord[0] + direction[0] < 0 or \
                    temp_coord[1] + direction[1] > 7 or temp_coord[1] + direction[1] < 0:
                    # if goes off the board
                    break
                temp_coord[0] = temp_coord[0] + direction[0]
                temp_coord[1] = temp_coord[1] + direction[1]
                if not board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                    # if empty space
                    p_basic_moves.append((board.convert_matrix_coord((temp_coord[0], temp_coord[1])), 0))
                elif board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))) and \
                    not board.is_current_player_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                    # if capture available
                    p_basic_moves.append(
                        (board.convert_matrix_coord((temp_coord[0], temp_coord[1])), \
                            board.board[temp_coord[0]][temp_coord[1]].get_value()) )
                    break
                else:
                    # if own piece blocking path
                    break
        return p_basic_moves


class ChessKing(ChessPiece):
    def __init__(self, color):
        if color == 'b':
            self.type = B_CHESS_KING
            self.color = 'b'
        elif color == 'w':
            self.type = W_CHESS_KING
            self.color = 'w'
        self.value = 100

    def __repr__(self):
        return self.type

    def possible_moves(self, board, piece):
        coord = board.convert_checker_coord(piece)
        p_basic_moves = []

        movement = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in movement:
            temp_coord = [coord[0], coord[1]]
            if temp_coord[0] + direction[0] > 7 or temp_coord[0] + direction[0] < 0 or \
                temp_coord[1] + direction[1] > 7 or temp_coord[1] + direction[1] < 0:
                # if goes off the board
                continue
            temp_coord[0] = temp_coord[0] + direction[0]
            temp_coord[1] = temp_coord[1] + direction[1]
            if not board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                # if empty space
                p_basic_moves.append((board.convert_matrix_coord((temp_coord[0], temp_coord[1])), 0))
            elif board.has_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))) and \
                not board.is_current_player_piece(board.convert_matrix_coord((temp_coord[0], temp_coord[1]))):
                # if capture available
                p_basic_moves.append(
                    (board.convert_matrix_coord((temp_coord[0], temp_coord[1])), \
                        board.board[temp_coord[0]][temp_coord[1]].get_value()) )
                continue
            else:
                # if own piece blocking path
                continue
        return p_basic_moves
