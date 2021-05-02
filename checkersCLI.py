from checker_board import CheckerBoard

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
        can_jump = []
        while True:
            self.prompt(new_turn)

            if new_turn:
                # check if any pieces have possible_jump_moves bc if yes, then only those pieces can move
                can_jump = []
                for row in self.game.board:
                    row_index = self.game.board.index(row)
                    for spot in row:
                        spot_index = list(row).index(spot)
                        coord = self.game.convert_matrix_coord((row_index, spot_index))
                        if self.game.has_piece(coord) and self.game.is_current_player_piece(coord):
                            if len(self.game.possible_jump_moves(coord)) > 0:
                                can_jump.append(coord)

            p_to_move = input("Select a piece to move\n")
            if not self.game.has_piece(p_to_move):
                print("No piece at that location")
                new_turn = False
                continue
            elif not self.game.is_current_player_piece(p_to_move):
                print("That is not your piece")
                new_turn = False
                continue

            p_jump_moves = self.game.possible_jump_moves(p_to_move)
            p_basic_moves = self.game.possible_basic_moves(p_to_move)
            if len(p_jump_moves) > 0:
                # if this piece has at least one possible jump move
                for string in self.game.display_moves(p_to_move, p_jump_moves, "jump"):
                    print(string)
                selected_move = int(input("Select a move by entering the corresponding index\n"))
                # make a move
                self.game.multi_jump(p_to_move, p_jump_moves[selected_move][0], p_jump_moves[selected_move][1:])
                self.game.turn += 1
                new_turn = True
                can_jump = []

            elif len(p_jump_moves) == 0 and (len(can_jump) > 0 or len(p_basic_moves) == 0):
                ## (not p_to_move in can_jump) should be the same as (len(p_jump_moves) == 0)
                # if this piece has no jump moves, and either other pieces can jump or this piece has no basic moves
                print("That piece cannot move")
                new_turn = False
                continue

            elif len(p_basic_moves) > 0:
                # if this piece has at least one possible basic move
                for string in self.game.display_moves(p_to_move, p_basic_moves, "basic"):
                    print(string)
                selected_move = int(input("Select a move by entering the corresponding index\n"))
                # make a move
                self.game.move(p_to_move, p_basic_moves[selected_move])
                self.game.turn += 1
                new_turn = True
                can_jump = []


if __name__ == "__main__":
    CheckersCLI().run()