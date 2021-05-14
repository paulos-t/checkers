from board import CheckerBoard
from player import Human, Random, Greedy, HumanChess, RandomChess, GreedyChess
import sys, copy, re

B_PEASANT = '\u2688'
W_PEASANT = '\u2686'
B_KING = '\u2689'
W_KING = '\u2687'
B_CHESS_KING = '\u265A'
W_CHESS_KING = '\u2654'

class CheckersCLI():

    def __init__(self, type="chess", player1="human", player2="human", history="off"):
        self.game = CheckerBoard(type)
        self.type = type
        self.player1 = player1
        self.player2 = player2
        self.history = history

    def prompt(self, new_turn:bool):
        if new_turn:
            player_turn = ""
            if self.game.turn % 2 == 1:
                player_turn = "white"
            elif self.game.turn % 2 == 0:
                player_turn = "black"
            print(self.game)
            print("Turn: " + str(self.game.turn) + ", " + player_turn)

    def game_check(self) -> list:
        if self.type == "chess":
            chess_can_move, chess_cannot_move = [], []
            b_king, w_king = False, False
            for row in self.game.board:
                row_index = self.game.board.index(row)
                for spot in row:
                    spot_index = list(row).index(spot)
                    coord = self.game.convert_matrix_coord((row_index, spot_index))
                    if self.game.has_piece(coord) and self.game.is_current_player_piece(coord):
                        if self.game.board[row_index][spot_index].type == B_CHESS_KING:
                            b_king = True
                        elif self.game.board[row_index][spot_index].type == W_CHESS_KING:
                            w_king = True
                        if len(self.game.board[row_index][spot_index].possible_moves(self.game, coord)) > 0:
                            chess_can_move.append(coord)
                        else:
                            chess_cannot_move.append(coord)
            return [chess_can_move, chess_cannot_move, b_king, w_king]
        elif self.type == "checkers":
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

    ## Fix undo/redo ##
    def undo_redo_next(self) -> bool:
        action = input("undo, redo, or next\n")
        if action == "undo" and len(self.game.mementos) + self.game.state_index >= 0:
            self.game.state_index -= 1
            self.game.change_state(self.game.mementos[self.game.state_index])
            self.game.available_redos += 1
            return True
        elif action == "redo" and self.game.available_redos > 0:
            self.game.state_index += 1
            self.game.change_state(self.game.mementos[self.game.state_index])
            self.game.available_redos -= 1
            return True
        elif action == "next":
            if self.game.state_index + 1 < 0:
                self.game.mementos = copy.deepcopy(self.game.mementos[:(self.game.state_index + 1)])
            self.game.state_index = -1
            self.game.available_redos = 0
            return False

    def run(self):
        new_turn = True
        can_jump, can_move, cannot_move = [], [], []
        chess_can_move, chess_cannot_move = [], []

        if self.type == "chess":
            if self.player1 == "human":
                self.player1 = HumanChess()
            elif self.player1 == "random":
                self.player1 = RandomChess()
            elif self.player1 == "greedy":
                self.player1 = GreedyChess()
            elif re.search("^minimax", self.player1):
                self.player1 = GreedyChess()

            if self.player2 == "human":
                self.player2 = HumanChess()
            elif self.player2 == "random":
                self.player2 = RandomChess()
            elif self.player2 == "greedy":
                self.player2 = GreedyChess()
            elif re.search("^minimax", self.player2):
                self.player2 = GreedyChess()

        if self.type == "checkers":
            if self.player1 == "human":
                self.player1 = Human()
            elif self.player1 == "random":
                self.player1 = Random()
            elif self.player1 == "greedy":
                self.player1 = Greedy()
            elif re.search("^minimax", self.player1):
                self.player1 = Greedy()

            if self.player2 == "human":
                self.player2 = Human()
            elif self.player2 == "random":
                self.player2 = Random()
            elif self.player2 == "greedy":
                self.player2 = Greedy()
            elif re.search("^minimax", self.player2):
                self.player2 = Greedy()

        while True:
            self.prompt(new_turn)
            if new_turn:
                if self.history == "on":
                    if self.undo_redo_next():
                        continue
                status = self.game_check()

                if self.type == "chess":
                    chess_can_move, chess_cannot_move, b_king, w_king = status[0], status[1], status[2], status[3]
                    if len(chess_can_move) == len(chess_cannot_move) == 0: # FIX: check if king is taken instead
                        # other player wins
                        if self.game.turn % 2 == 1:
                            print("black has won")
                            break
                        elif self.game.turn % 2 == 0:
                            print("white has won")
                            break
                    elif b_king == False:
                        print("white has won")
                        break
                    elif w_king == False:
                        print("black has won")
                        break
                    elif len(chess_can_move) == 0 and len(chess_cannot_move) > 0:
                        print("draw")
                        break
                    elif self.game.turns_without_capture == 50:
                        print("draw")
                        break

                elif self.type == "checkers":
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

            
            if self.type == "chess":
                if self.game.turn % 2 == 1:
                    new_turn = self.player1.take_turn(self.game, chess_can_move)
                    if new_turn:
                        self.game.mementos.append(self.game.create_memento())
                elif self.game.turn % 2 == 0:
                    new_turn = self.player2.take_turn(self.game, chess_can_move)
                    if new_turn:
                        self.game.mementos.append(self.game.create_memento())

            elif self.type == "checkers":
                if self.game.turn % 2 == 1:
                    new_turn = self.player1.take_turn(self.game, can_jump, can_move)
                    if new_turn:
                        self.game.mementos.append(self.game.create_memento())
                elif self.game.turn % 2 == 0:
                    new_turn = self.player2.take_turn(self.game, can_jump, can_move)
                    if new_turn:
                        self.game.mementos.append(self.game.create_memento())




if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 5:
        CheckersCLI(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]).run()
    elif argc == 4:
        CheckersCLI(sys.argv[1], sys.argv[2], sys.argv[3]).run()
    elif argc == 3:
        CheckersCLI(sys.argv[1], sys.argv[2]).run()
    elif argc == 2:
        CheckersCLI(sys.argv[1]).run()
    elif argc == 1:
        CheckersCLI().run()
    else:
        print("fix command-line arguments")