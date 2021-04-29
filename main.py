import copy

B_PEASANT = '\u2688'
W_PEASANT = '\u2686'
B_KING = '\u2689'
W_KING = '\u2687'

class CheckersCLI():
    def __init__(self):
        self.game = CheckerBoard()
        # self.player1 = Player('w')
        # self.player2 = Player('b')

    def prompt(self, new_turn:bool):
        if new_turn:
            player_turn = ""
            if self.game.turn % 2 == 1:
                player_turn = "white"
            elif self.game.turn % 2 == 0:
                player_turn = "black"
            print(self.game)
            print("Turn: " + str(self.game.turn) + ", " + player_turn)

    def run(self):
        new_turn = True
        while True:
            self.prompt(new_turn)
            p_to_move = input("Select a piece to move\n")
            if not self.game.has_piece(p_to_move):
                print("No piece at that location")
                new_turn = False
                continue
            elif not self.game.is_current_player_piece(p_to_move):
                print("That is not your piece")
                new_turn = False
                continue

            # must check if any pieces have jump_moves bc if yes, then only those pieces can move
            # possible_moves = self.game.possible_moves(p_to_move)
            # if len(possible_moves) == 0:
            #     print("That piece cannot move")
            #     new_turn = False
            #     continue
            else:
                # selected_move = input(possible_moves)

                # basic_move = self.game.possible_basic_moves(p_to_move)
                # if basic_move:
                #     for i in range(len(basic_move)):
                #         print(str(i) + ": basic move: " + p_to_move + "->" + basic_move[i])

                ## make a move
                print(self.game.possible_basic_moves(p_to_move))
                print(self.game.possible_jump_moves(p_to_move))
                self.game.turn += 1
                new_turn = True


class CheckerBoard():

    rows, cols = (8, 8)
    b_space = '\u25fc'
    w_space = '\u25fb'

    def __init__(self):
        self.board = [[self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space, self.b_space, self.w_space]]
        self.turn = 1

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
        return isinstance(self.board[coord[0]][coord[1]], Piece)

    def is_current_player_piece(self, piece:str) -> bool:
        coord = self.convert_checker_coord(piece)
        piece_color = str(self.board[coord[0]][coord[1]])
        if self.turn % 2 == 1:
            if piece_color == W_PEASANT or piece_color == W_KING:
                return True
            else:
                return False
        elif self.turn % 2 == 0:
            if piece_color == B_PEASANT or piece_color == B_KING:
                return True
            else:
                return False

    def jump(self, piece:str, jump_to:str, captured_spot:str):
        coord1 = self.convert_checker_coord(piece)
        coord2 = self.convert_checker_coord(jump_to)
        coord3 = self.convert_checker_coord(captured_spot)
        self.board[coord2[0]][coord2[1]] = self.board[coord1[0]][coord1[1]]
        self.board[coord1[0]][coord1[1]] = self.w_space
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

    def possible_jump_moves(self, piece:str) -> list:
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
                return p_jump_moves
            elif coord[0] == 7 or coord[0] == 6:
                # when king is in bottom two rows
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    p_jump_moves.append( [up_right_2, up_right] )
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    p_jump_moves.append( [up_left_2, up_left] )
                return p_jump_moves
            elif coord[1] == 0 or coord[1] == 1:
                # when king is in first two columns
                if self.has_piece(up_right) and not self.is_current_player_piece(up_right) and not self.has_piece(up_right_2):
                    p_jump_moves.append( [up_right_2, up_right] )
                if self.has_piece(down_right) and not self.is_current_player_piece(down_right) and not self.has_piece(down_right_2):
                    p_jump_moves.append( [down_right_2, down_right] )
                return p_jump_moves
            elif coord[1] == 7 or coord[1] == 6:
                # when king is in last two columns
                if self.has_piece(up_left) and not self.is_current_player_piece(up_left) and not self.has_piece(up_left_2):
                    p_jump_moves.append( [up_left_2, up_left] )
                if self.has_piece(down_left) and not self.is_current_player_piece(down_left) and not self.has_piece(down_left_2):
                    p_jump_moves.append( [down_left_2, down_left] )
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
                if len(more_jumps) > 0:
                    for new_jump in more_jumps:
                        new_jump.append(p_jump_moves[0][1:])
                        p_jump_moves.append(new_jump)
                    p_jump_moves.remove(p_jump_moves[0])
            return p_jump_moves

    # def possible_moves(self, piece:str) -> list:
    #     p_basic_moves = self.possible_basic_moves(piece)
    #     p_jump_moves = self.possible_jump_moves(piece)
    #     if len(p_jump_moves) > 0:
    #         while True:
    #             pass



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

    def move(self, move_to):
        pass

    def jump(self, jump_to):
        pass

    def double_jump(self, jump_to):
        pass


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

    def move(self, move_to):
        return super().move() # can move backwards too

    def jump(self, jump_to):
        return super().jump() # can jump backwards too

    def double_jump(self, jump_to):
        return super().double_jump() # can double-jump backwards too



if __name__ == "__main__":
    CheckersCLI().run()