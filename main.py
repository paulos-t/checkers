from checker_board import CheckerBoard
from player import Human, Random, Greedy
import sys

B_PEASANT = '\u2688'
W_PEASANT = '\u2686'
B_KING = '\u2689'
W_KING = '\u2687'

class CheckersCLI():

    def __init__(self, player1="human", player2="human", history="off"):
        self.game = CheckerBoard()
        self.player1 = player1
        self.player2 = player2
        self.history = history

    def prompt(self, new_turn:bool, history:str):
        if new_turn:
            player_turn = ""
            if self.game.turn % 2 == 1:
                player_turn = "white"
            elif self.game.turn % 2 == 0:
                player_turn = "black"
            print(self.game)
            print("Turn: " + str(self.game.turn) + ", " + player_turn)
            if history == "on":
                print("undo, redo, or next")

    def game_check(self) -> list:
        # check if any pieces have possible jump moves or basic moves
        can_jump, can_move, cannot_move = [], [], []
        for row in self.game.board:
            row_index = self.game.board.index(row)
            for spot in row:
                spot_index = list(row).index(spot)
                coord = self.game.convert_matrix_coord((row_index, spot_index))
                if self.game.has_piece(coord) and self.game.is_current_player_piece(coord):
                    if len(self.game.possible_jump_moves(coord)) > 0:
                        can_jump.append(coord)
                    elif len(self.game.possible_basic_moves(coord)) > 0:
                        can_move.append(coord)
                    else:
                        cannot_move.append(coord)
        return [can_jump, can_move, cannot_move]

    def run(self):
        new_turn = True
        can_jump, can_move = [], []

        if self.player1 == "human":
            self.player1 = Human()
        elif self.player1 == "random":
            self.player1 = Random()
        elif self.player1 == "greedy":
            self.player1 = Greedy()

        if self.player2 == "human":
            self.player2 = Human()
        elif self.player2 == "random":
            self.player2 = Random()
        elif self.player2 == "greedy":
            self.player2 = Greedy()

        while True:
            self.prompt(new_turn, self.history)
            if new_turn:
                status = self.game_check()
                can_jump, can_move, cannot_move = status[0], status[1], status[2]
                if len(can_jump) == len(can_move) == len(cannot_move) == 0:
                    # other player wins
                    if self.game.turn % 2 == 1:
                        print("black has won")
                        break
                    elif self.game.turn % 2 == 0:
                        print("white has won")
                        break
                elif (len(can_jump) == len(can_move) == 0) and len(cannot_move) > 0:
                    print("draw")
                    break
                elif self.game.turns_without_capture == 50:
                    print("draw")
                    break
            if self.game.turn % 2 == 1:
                new_turn = self.player1.take_turn(self.game, can_jump, can_move)
            elif self.game.turn % 2 == 0:
                new_turn = self.player2.take_turn(self.game, can_jump, can_move)



if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 3:
        CheckersCLI(sys.argv[1], sys.argv[2]).run()
    elif argc == 4:
        CheckersCLI(sys.argv[1], sys.argv[2], sys.argv[3]).run()
    elif argc == 2:
        CheckersCLI(sys.argv[1]).run()
    elif argc == 1:
        CheckersCLI().run()
    else:
        print("fix command-line arguments")