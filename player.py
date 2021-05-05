from checker_board import CheckerBoard
import random

class Player():
    def __init__(self):
        self.game = None
    
    def take_turn(self):
        pass


class Human(Player):
    def take_turn(self, game:CheckerBoard, can_jump:list, can_move:list) -> bool:
        self.game = game

        p_to_move = input("Select a piece to move\n")
        if not self.game.has_piece(p_to_move):
            print("No piece at that location")
            return False
        elif not self.game.is_current_player_piece(p_to_move):
            print("That is not your piece")
            return False
        
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
            return True

        elif len(p_jump_moves) == 0 and (len(can_jump) > 0 or len(p_basic_moves) == 0):
            # if this piece has no jump moves, and either other pieces can jump or this piece has no basic moves
            print("That piece cannot move")
            return False

        elif len(p_basic_moves) > 0:
            # if this piece has at least one possible basic move
            for string in self.game.display_moves(p_to_move, p_basic_moves, "basic"):
                print(string)
            selected_move = int(input("Select a move by entering the corresponding index\n"))
            # make a move
            self.game.move(p_to_move, p_basic_moves[selected_move])
            self.game.turn += 1
            self.game.turns_without_capture += 1
            return True


class Random(Player):
    def take_turn(self, game:CheckerBoard, can_jump:list, can_move:list) -> bool:
        self.game = game
        
        if can_jump:
            random_choice = random.choice(can_jump)
            possible_j_moves = self.game.possible_jump_moves(random_choice)
            random_dest_selection = random.choice(possible_j_moves)
            self.game.multi_jump(random_choice, random_dest_selection[0], random_dest_selection[1:])
            self.game.turn += 1
            self.game.turns_without_capture = 0
            return True

        elif can_move:
            random_choice = random.choice(can_move)
            possible_b_moves = self.game.possible_basic_moves(random_choice)
            random_dest_selection = random.choice(possible_b_moves)
            self.game.move(random_choice, random_dest_selection)
            self.game.turn += 1
            self.game.turns_without_capture += 1
            return True


class Greedy(Player):
    def take_turn(self, game:CheckerBoard, can_jump:list, can_move:list) -> bool:
        self.game = game

        list_jump_nums = []
        potential_jump = []
        final_random_jump_selector = []
        if can_jump:
            for i in range(len(can_jump)):
                storage = self.game.possible_jump_moves(can_jump[i])
                biggest_length = 0
                for j in range(len(storage)):
                    if len(storage[j]) >= biggest_length:
                        biggest_length = len(storage[j])
                
                list_jump_nums.append((can_jump[i],biggest_length))
                biggest_length = 0
            sorted_by_second = sorted(list_jump_nums, key=lambda tup: tup[1])
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
            self.game.turn += 1
            self.game.turns_without_capture = 0
            return True

        elif can_move:
            random_choice = random.choice(can_move)
            possible_b_moves = self.game.possible_basic_moves(random_choice)
            random_dest_selection = random.choice(possible_b_moves)
            self.game.move(random_choice,random_dest_selection)
            self.game.turn += 1
            self.game.turns_without_capture += 1
            return True