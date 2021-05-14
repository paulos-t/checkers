from piece import Piece, King, ChessPiece, Pawn, Knight, Rook, Bishop, Queen, ChessKing
import copy

B_PEASANT = '\u2688'
W_PEASANT = '\u2686'
B_KING = '\u2689'
W_KING = '\u2687'
B_CHESS_PAWN = '\u265F'
W_CHESS_PAWN = '\u2659'

class CheckerBoard():

    rows, cols = (8, 8)
    b_space = '\u25fc'
    w_space = '\u25fb'

    def __init__(self, type):
        if type == "checkers":
            self.board = [[Piece('b'), self.b_space, Piece('b'), self.b_space, Piece('b'), self.b_space, Piece('b'), self.b_space],
                [self.b_space, Piece('b'), self.b_space, Piece('b'), self.b_space, Piece('b'), self.b_space, Piece('b')],
                [Piece('b'), self.b_space, Piece('b'), self.b_space, Piece('b'), self.b_space, Piece('b'), self.b_space],
                [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
                [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
                [self.b_space, Piece('w'), self.b_space, Piece('w'), self.b_space, Piece('w'), self.b_space, Piece('w')],
                [Piece('w'), self.b_space, Piece('w'), self.b_space, Piece('w'), self.b_space, Piece('w'), self.b_space],
                [self.b_space, Piece('w'), self.b_space, Piece('w'), self.b_space, Piece('w'), self.b_space, Piece('w')]]
            # Checkers Test Board
            # self.board = [[self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            # [self.b_space, self.w_space, self.b_space, Piece('w'), self.b_space, self.w_space, self.b_space, self.w_space],
            # [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space,King('b'), self.b_space],
            # [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            # [self.w_space, self.b_space, King('b'), self.b_space, self.w_space, self.b_space, King('b'), self.b_space],
            # [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            # [self.w_space, self.b_space, King('b'), self.b_space, King('b'), self.b_space, self.w_space, self.b_space],
            # [self.b_space, self.w_space, self.b_space, Piece('w'), self.b_space, self.w_space, self.b_space, self.w_space]]
        elif type == "chess":
            self.board = [[Rook('b'),Knight('b'), Bishop('b'), Queen('b'), ChessKing('b'), Bishop('b'), Knight('b'), Rook('b')],
                [Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')],
                [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
                [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
                [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
                [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
                [Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')],
                [Rook('w'),Knight('w'), Bishop('w'), Queen('w'), ChessKing('w'), Bishop('w'), Knight('w'), Rook('w')]]
            # Chess Test Board
            # self.board = [[Rook('b'),Knight('b'), Bishop('b'), Queen('b'), ChessKing('b'), Bishop('b'), Knight('b'), Rook('b')],
            #     [Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b')],
            #     [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            #     [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            #     [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            #     [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            #     [Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')],
            #     [Rook('w'),Knight('w'), Bishop('w'), Queen('w'), ChessKing('w'), Bishop('w'), Knight('w'), Rook('w')]]
        self.blank_board = [[self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space]]
        self.turn = 1
        self.turns_without_capture = 0
        self.mementos = [Memento(self.board, self.turn, self.turns_without_capture)]
        self.state_index = -1
        self.available_redos = 0

    def __repr__(self):
        i = 1
        out = ""
        for row in self.board:
            r_out = ""
            for col in range(len(row)):
                r_out += " " + str(row[col])
            out += str(i) + r_out + "\n"
            i += 1
        return out + "  a b c d e f g h"

    def convert_checker_coord(self, coord:str) -> tuple:
        """ Converts board coordinates into matrix coordinates """
        col = coord[:1]
        row = coord[1:]
        col = ord(col) - 96
        row = int(row)
        return (row - 1, col - 1)

    def convert_matrix_coord(self, coord:tuple) -> str:
        """ Converts matrix coordinates into board coordinates """
        row, col = coord
        return chr(col + 96 + 1) + str(row + 1)

    def has_piece(self, spot:str) -> bool:
        coord = self.convert_checker_coord(spot)
        ret = isinstance(self.board[coord[0]][coord[1]], Piece) or isinstance(self.board[coord[0]][coord[1]], ChessPiece)
        return ret

    def is_current_player_piece(self, piece:str) -> bool:
        coord = self.convert_checker_coord(piece)
        piece_color = self.board[coord[0]][coord[1]].color
        if self.turn % 2 == 1:
            if piece_color == W_PEASANT or piece_color == W_KING or piece_color == 'w':
                return True
            else:
                return False
        elif self.turn % 2 == 0:
            if piece_color == B_PEASANT or piece_color == B_KING or piece_color == 'b':
                return True
            else:
                return False

    def move(self, piece:str, move_to:str):
        coord1 = self.convert_checker_coord(piece)
        coord2 = self.convert_checker_coord(move_to)
        # peasant becoming king or pawn becoming queen
        if str(self.board[coord1[0]][coord1[1]]) == B_PEASANT and coord2[0] == 7:
            self.board[coord2[0]][coord2[1]] = King('b')
            self.board[coord1[0]][coord1[1]] = self.w_space
        elif str(self.board[coord1[0]][coord1[1]]) == W_PEASANT and coord2[0] == 0:
            self.board[coord2[0]][coord2[1]] = King('w')
            self.board[coord1[0]][coord1[1]] = self.w_space
        elif self.board[coord1[0]][coord1[1]].type == B_CHESS_PAWN and coord2[0] == 7:
            self.board[coord2[0]][coord2[1]] = ChessKing('b')
            self.board[coord1[0]][coord1[1]] = self.blank_board[coord1[0]][coord1[1]]
        elif self.board[coord1[0]][coord1[1]].type == W_CHESS_PAWN and coord2[0] == 0:
            self.board[coord2[0]][coord2[1]] = ChessKing('b')
            self.board[coord1[0]][coord1[1]] = self.blank_board[coord1[0]][coord1[1]]
        else:
            self.board[coord2[0]][coord2[1]] = self.board[coord1[0]][coord1[1]]
            self.board[coord1[0]][coord1[1]] = self.blank_board[coord1[0]][coord1[1]]


    ## -- Checkers Specifc -- ##
    def jump(self, piece:str, jump_to:str, captured_piece:str):
        self.move(piece, jump_to)
        coord3 = self.convert_checker_coord(captured_piece)
        self.board[coord3[0]][coord3[1]] = self.w_space
    
    def multi_jump(self, piece:str, jump_to:str, captured_pieces:list):
        self.move(piece, jump_to)
        for captured in captured_pieces:
            coord3 = self.convert_checker_coord(captured)
            self.board[coord3[0]][coord3[1]] = self.w_space

    def possible_basic_moves(self, piece:str) -> list:
        coord = self.convert_checker_coord(piece)
        piece_color = str(self.board[coord[0]][coord[1]])
        p_basic_moves = []
        
        if piece_color == B_PEASANT:
            if coord[1] == 0:
                if self.board[coord[0]+1][coord[1]+1] == self.w_space:
                    # when in left column
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]+1)))
                else:
                    return p_basic_moves
            elif coord[1] == 7:
                if self.board[coord[0]+1][coord[1]-1] == self.w_space:
                    # when in right column
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]-1)))
                else:
                    return p_basic_moves
            else:
                # everywhere else
                if self.board[coord[0]+1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]-1)))
                if self.board[coord[0]+1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]+1)))

        elif piece_color == W_PEASANT:
            if coord[1] == 0:
                if self.board[coord[0]-1][coord[1]+1] == self.w_space:
                    # when in left column
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]+1)))
                else:
                    return p_basic_moves
            elif coord[1] == 7:
                if self.board[coord[0]-1][coord[1]-1] == self.w_space:
                    # when in right column
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]-1)))
                else:
                    return p_basic_moves
            else:
                # everywhere else
                if self.board[coord[0]-1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]-1)))
                if self.board[coord[0]-1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]+1)))

        elif piece_color == B_KING or piece_color == W_KING:
            if coord[0] == 0 and coord[1] == 0:
                if self.board[coord[0]+1][coord[1]+1] == self.w_space:
                    # top-left corner
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]+1)))
                else:
                    return p_basic_moves
            elif coord[0] == 7 and coord[1] == 7:
                if self.board[coord[0]-1][coord[1]-1] == self.w_space:
                    # bottom-right corner
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]-1)))
                else:
                    return p_basic_moves
            elif coord[0] == 0:
                # when king is in top row
                if self.board[coord[0]+1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]-1)))
                if self.board[coord[0]+1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]+1)))
                return p_basic_moves
            elif coord[0] == 7:
                # when king is in bottom row
                if self.board[coord[0]-1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]-1)))
                if self.board[coord[0]-1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]+1)))
                return p_basic_moves
            elif coord[1] == 0:
                # when king is in left column
                if self.board[coord[0]-1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]+1)))
                if self.board[coord[0]+1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]+1)))
                return p_basic_moves
            elif coord[1] == 7:
                # when king is in right column
                if self.board[coord[0]-1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]-1)))
                if self.board[coord[0]+1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]-1)))
                return p_basic_moves
            else:
                # everywhere else (middle of board)
                if self.board[coord[0]-1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]-1)))
                if self.board[coord[0]-1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]-1, coord[1]+1)))
                if self.board[coord[0]+1][coord[1]-1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]-1)))
                if self.board[coord[0]+1][coord[1]+1] == self.w_space:
                    p_basic_moves.append(self.convert_matrix_coord((coord[0]+1, coord[1]+1)))

        return p_basic_moves

    # def possible_jump_moves(self, piece:str) -> list:
        coord = self.convert_checker_coord(piece)
        piece_color = str(self.board[coord[0]][coord[1]])
        p_jump_moves = [] # [ [new location of moved piece, captured piece location] [ , ] ... ]

        down_right = self.convert_matrix_coord( (coord[0]+1, coord[1]+1) )
        down_left = self.convert_matrix_coord( (coord[0]+1, coord[1]-1) )
        up_right = self.convert_matrix_coord( (coord[0]-1, coord[1]+1) )
        up_left = self.convert_matrix_coord( (coord[0]-1, coord[1]-1) )
        down_right_2 = self.convert_matrix_coord( (coord[0]+2, coord[1]+2) )
        down_left_2 = self.convert_matrix_coord( (coord[0]+2, coord[1]-2) )
        up_right_2 = self.convert_matrix_coord( (coord[0]-2, coord[1]+2) )
        up_left_2 = self.convert_matrix_coord( (coord[0]-2, coord[1]-2) )

        if piece_color == B_PEASANT:
            if coord[0] == 7 or coord[0] == 6:
                # when in bottom two rows
                return p_jump_moves
            elif (coord[1] == 0 or coord[1] == 1):
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    # when in first two columns
                    p_jump_moves.append( [down_right_2, down_right] )
                else:
                    return p_jump_moves
            elif (coord[1] == 7 or coord[1] == 6):
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    # when in last two columns
                    p_jump_moves.append( [down_left_2, down_left] )
                else:
                    return p_jump_moves
            else:
                # everywhere else
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    p_jump_moves.append( [down_right_2, down_right] )
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    p_jump_moves.append( [down_left_2, down_left] )
        
        elif piece_color == W_PEASANT:
            if coord[0] == 0 or coord[0] == 1:
                # when in top two rows
                return p_jump_moves
            elif (coord[1] == 0 or coord[1] == 1):
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    # when in first two columns
                    p_jump_moves.append( [up_right_2, up_right] )
                else:
                    return p_jump_moves
            elif (coord[1] == 7 or coord[1] == 6):
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    # when in last two columns
                    p_jump_moves.append( [up_left_2, up_left] )
                else:
                    return p_jump_moves
            else:
                # everywhere else
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    p_jump_moves.append( [up_right_2, up_right] )
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    p_jump_moves.append( [up_left_2, up_left] )
        
        elif piece_color == B_KING or piece_color == W_KING:
            if ((coord[0] == 0 and coord[1] == 0) or (coord[0] == 1 and coord[1] == 1)):
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    # top left corner
                    p_jump_moves.append( [down_right_2, down_right] )
                else:
                    return p_jump_moves
            elif ((coord[0] == 7 and coord[1] == 7) or (coord[0] == 6 and coord[1] == 6)):
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    # bottom right corner
                    p_jump_moves.append( [up_left_2, up_left] )
                else:
                    return p_jump_moves
            elif ((coord[0] == 6 and coord[1] == 0) or (coord[0] == 7 and coord[1] == 1)):
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    # when king is on a7 or b8
                    p_jump_moves.append( [up_right_2, up_right] )
                else:
                    return p_jump_moves
            elif ((coord[0] == 0 and coord[1] == 6) or (coord[0] == 1 and coord[1] == 7)):
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    # when king is on g1 or h2
                    p_jump_moves.append( [down_left_2, down_left] )
                else:
                    return p_jump_moves
            elif coord[0] == 0 or coord[0] == 1:
                # when king is in top two rows
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    p_jump_moves.append( [down_right_2, down_right] )
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    p_jump_moves.append( [down_left_2, down_left] )
                if len(p_jump_moves) == 0:
                    return p_jump_moves
            elif coord[0] == 7 or coord[0] == 6:
                # when king is in bottom two rows
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    p_jump_moves.append( [up_right_2, up_right] )
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    p_jump_moves.append( [up_left_2, up_left] )
                if len(p_jump_moves) == 0:
                    return p_jump_moves
            elif coord[1] == 0 or coord[1] == 1:
                # when king is in first two columns
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    p_jump_moves.append( [up_right_2, up_right] )
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    p_jump_moves.append( [down_right_2, down_right] )
                if len(p_jump_moves) == 0:
                    return p_jump_moves
            elif coord[1] == 7 or coord[1] == 6:
                # when king is in last two columns
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    p_jump_moves.append( [up_left_2, up_left] )
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    p_jump_moves.append( [down_left_2, down_left] )
                if len(p_jump_moves) == 0:
                    return p_jump_moves
            else:
                # everywhere else (middle of board)
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    p_jump_moves.append( [down_right_2, down_right] )
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    p_jump_moves.append( [down_left_2, down_left] )
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    p_jump_moves.append( [up_right_2, up_right] )
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    p_jump_moves.append( [up_left_2, up_left] )
        
        # recursion  
        if len(p_jump_moves) == 0:
            return p_jump_moves

        elif len(p_jump_moves) > 0:
            for jump in p_jump_moves:
                new_board = CheckerBoard()
                new_board.board = copy.deepcopy(self.board)
                new_board.jump(piece, jump[0], jump[-1])
                more_jumps = new_board.possible_jump_moves(jump[0])
                # print(more_jumps) # print statement
                if len(more_jumps) > 0:
                    # print("a")# print statement
                    # print(p_jump_moves) # print statement
                    for new_jump in more_jumps:
                        new_jump = new_jump + p_jump_moves[0][1:]
                        p_jump_moves.append(new_jump)
                    p_jump_moves.remove(p_jump_moves[0])
                    # print(f"Possible jumps: {p_jump_moves}") # print statement
            return p_jump_moves

    # def possible_basic_moves(self, piece:str) -> list:
    #     ret = []
    #     coord = self.convert_checker_coord(piece)
    #     piece_color = str(self.board[coord[0]][coord[1]])
    #     if piece_color == B_PEASANT:
    #         possible_spots = [(1, 1), (1, -1)]
    #     elif piece_color == W_PEASANT:
    #         possible_spots = [(-1, 1), (-1, -1)]
    #     elif piece_color == B_KING or piece_color == W_KING:
    #         possible_spots = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def possible_jump_moves(self, piece:str) -> list:
        ret = []
        coord = self.convert_checker_coord(piece)
        piece_color = str(self.board[coord[0]][coord[1]])
        if piece_color == B_PEASANT:
            possible_jumps = [(2, 2), (2, -2)]
            possible_captures = [(1, 1), (1, -1)]
        elif piece_color == W_PEASANT:
            possible_jumps = [(-2, 2), (-2, -2)]
            possible_captures = [(-1, 1), (-1, -1)]
        elif piece_color == B_KING or piece_color == W_KING:
            possible_jumps = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
            possible_captures = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        def recurse(c_piece:str, board:CheckerBoard, p_jump_moves:list):
            c_x, c_y = board.convert_checker_coord(c_piece)
            valid_moves = []
            for jump_to, captured in zip(possible_jumps, possible_captures):
                if c_x + jump_to[0] > 7 or c_x + jump_to[0] < 0 or c_y + jump_to[1] > 7 or c_y + jump_to[1] < 0:
                    continue
                captured_piece = board.convert_matrix_coord((c_x + captured[0], c_y + captured[1]))
                new_spot = board.convert_matrix_coord((c_x + jump_to[0], c_y + jump_to[1]))
                if board.has_piece(captured_piece) and not board.is_current_player_piece(captured_piece) and\
                    not board.has_piece(new_spot):
                    valid_moves.append((new_spot, captured_piece))
            
            if valid_moves:
                for move in valid_moves:
                    new_move = copy.copy(p_jump_moves)
                    new_move.append(move)
                    new_board = CheckerBoard("checkers")
                    new_board.board = copy.deepcopy(board.board)
                    new_board.turn = board.turn
                    new_board.jump(c_piece, move[0], move[1])
                    recurse(move[0], new_board, new_move)
            elif p_jump_moves:
                ret.append(p_jump_moves)

        recurse(piece, self, [])
        # ret == [ [('e5', 'd6'), ('c3', 'd4')], [('e5', 'd6'), ('g7', 'f6')] ]

        out = []
        for jump_move in ret:
            temp = []
            temp.append(jump_move[-1][0])
            for jump in jump_move:
                temp.append(jump[1])
            out.append(temp)
        # ret == [ ['c3', 'd6', 'd4], ['g7', 'd6', 'f6'] ]
        return out
    ## -- -- ##


    def display_moves(self, piece:str, moves:list, type:str) -> list:
        out = []
        if type == "basic":
            for move in enumerate(moves):
                out.append(f"{move[0]}: basic move: {piece}->{move[1]}")
        elif type == "jump":
            for move in enumerate(moves):
                cap = "["
                for x in move[1][1:]:
                    cap = cap + x + ", "
                cap = cap[:-2] + "]"
                out.append(f"{move[0]}: jump move: {piece}->{move[1][0]}, capturing {cap}")
        elif type == "chessmove":
            for move in enumerate(moves):
                out.append(f"{move[0]}: move: {piece}->{move[1][0]}")
        return out


    ## Fix undo/redo ##

    def create_memento(self):
        return Memento(self.board, self.turn, self.turns_without_capture)

    def change_state(self, memento):
        self.board = memento.board_state
        self.turn = memento.turn_state
        self.turns_without_capture = memento.turns_without_capture_state


class Memento():
    def __init__(self, board, turn, turns_without_capture):
        self.board_state = board
        self.turn_state = turn
        self.turns_without_capture_state = turns_without_capture