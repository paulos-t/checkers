## Classes

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
            elif not self.game.can_move(p_to_move):
                print("That piece cannot move")
                new_turn = False
                continue
            else:
                self.game.possible_moves(p_to_move)
                new_turn = True


class CheckerBoard():

    rows, cols = (8, 8)
    b_space = '\u25fc'
    w_space = '\u25fb'
    b_peasant = '\u2688'
    w_peasant = '\u2686'
    b_king = '\u2689'
    w_king = '\u2687'

    def __init__(self):
        self.board = [[self.b_peasant,self.b_space,self.b_peasant,self.b_space, self.b_peasant, self.b_space, self.b_peasant, self.b_space],
            [self.b_space,self.b_peasant,self.b_space,self.b_peasant,self.b_space, self.b_peasant, self.b_space, self.b_peasant],
            [self.b_peasant,self.b_space,self.b_peasant,self.b_space, self.b_peasant, self.b_space, self.b_peasant, self.b_space],
            [self.b_space,self.w_space,self.b_space,self.w_space,self.b_space, self.w_space, self.b_space, self.w_space],
            [self.w_space,self.b_space,self.w_space,self.b_space, self.w_space, self.b_space, self.w_space, self.b_space],
            [self.b_space,self.w_peasant,self.b_space,self.w_peasant,self.b_space, self.w_peasant, self.b_space, self.w_peasant],
            [self.w_peasant,self.b_space,self.w_peasant,self.b_space, self.w_peasant, self.b_space, self.w_peasant, self.b_space],
            [self.b_space,self.w_peasant,self.b_space,self.w_peasant,self.b_space, self.w_peasant, self.b_space, self.w_peasant]]
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

    def convert_checker_coord(coord:str):
        col = coord[:1]
        row = coord[1:]
        col = ord(col) - 96
        row = int(row)
        return (row - 1, col - 1)

    def convert_matrix_coord(coord:tuple):
        row, col = coord
        return chr(col + 96 + 1) + str(row + 1)

    def has_piece(self, piece:str) -> bool:
        pass

    def is_current_player_piece(self, piece:str) -> bool:
        pass

    def can_move(self, piece:str) -> bool:
        pass

    def possible_moves(self, piece:str) -> list:
        pass


class Piece():
    def __init__(self, color):
        if color == 'b':
            self.color = '\u2688'
        elif color == 'w':
            self.color = '\u2686'
        else:
            self.color = None
            print("Please provide a valid color")

    def move(self):
        pass

    def jump(self):
        pass

    def double_jump(self):
        pass

class King(Piece):
    def __init__(self, color):
        if color == 'b':
            self.color = '\u2689'
        elif color == 'w':
            self.color = '\u2687'
        else:
            self.color = None
            print("Please provide a valid color")

    def move(self):
        return super().move() # can move backwards too

    def jump(self):
        return super().jump() # can jump backwards too

    def double_jump(self):
        return super().double_jump() # can double-jump backwards too



if __name__ == "__main__":
    CheckersCLI().run()