from checker_board import CheckerBoard
import random

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
                # check if any pieces have possible jump moves or basic moves
                can_jump = []
                can_move = []
                cannot_move = []
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
                self.game.turns_without_capture = 0
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
                self.game.turns_without_capture += 1
                new_turn = True
                can_jump = []
    def random_player(self, can_jump:list, can_move:list):
        if can_jump:
            random_choice = random.choice(can_jump)
            possible_j_moves = self.game.possible_jump_moves(random_choice)
            random_dest_selection = random.choice(possible_j_moves)
            self.game.multi_jump(random_choice,random_dest_selection[0], random_dest_selection[1:])
        elif can_move:
            random_choice = random.choice(can_move)
            possible_b_moves = self.game.possible_basic_moves(random_choice)
            random_dest_selection = random.choice(possible_b_moves)
            self.game.move(random_choice,random_dest_selection)


    def greedy_player(self, can_jump:list,can_move:list):
        list_jump_nums = []
        potential_jump = []
        final_random_jump_selector = []
        if can_jump:
            for i in range(len(can_jump))
                storage = self.game.possible_jump_moves(can_jump[i])
                biggest_length = 0
                for j in range(len(storage)):
                    if len(storage[j]) >= biggest_length:
                        biggest_length = len(storage[j])
                
                list_jump_nums.append((can_jump[i],biggest_length))
                biggest_length = 0
            sorted_by_second = sorted(foo, key=lambda tup: tup[1])
            biggest_length2 = sorted_by_second[-1][1]
            for a in range(len(list_jump_nums)):
                if list_jump_nums[a][1] == biggest_length2:
                    potential_jump.append(list_jump_nums[a][0])
            for b in range(len(potential_jump)):
                holder = self.game.possible_jump_moves(potential_jump[b])
                for c in range(len(holder)):
                    if len(holder[c]) == biggest_length2:
                        final_random_jump_selector.append((potential_jump[b],holder[c]))

            random_jump = random.choice(final_random_jump_selector)
            self.game.multi_jump(random_jump[0],random_jump[1][0],random_jump[1][1:])
        elif can_move:
            random_choice = random.choice(can_move)
            possible_b_moves = self.game.possible_basic_moves(random_choice)
            random_dest_selection = random.choice(possible_b_moves)
            self.game.move(random_choice,random_dest_selection)



    
        



if __name__ == "__main__":
    CheckersCLI().run()