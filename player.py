from board import CheckerBoard
import random

class Player():
    def __init__(self):
        self.game = None
        # seed = str(open("seed.txt"))
        # random.seed(seed)
    
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
                biggest_val = 0
                net_value = 0
                for j in range(len(storage)):
                    for k in range(1,len(storage[j])):
                        coord = self.game.convert_checker_coord(storage[j][k])
                        net_value += self.game.board[coord[0]][coord[1]].value
                    if net_value > biggest_val:
                        biggest_val = net_value
                        net_value =0
                    
                    # if sum(storage[j]) >= biggest_val:
                    #     biggest_val = len(storage[j])
                
                list_jump_nums.append((can_jump[i],biggest_val))
                    
                biggest_val = 0
            sorted_by_second = sorted(list_jump_nums, key=lambda tup: tup[1])
            biggest_val2 = sorted_by_second[-1][1]
            net_value2 = 0
            for a in range(len(list_jump_nums)):
                if list_jump_nums[a][1] == biggest_val2:
                    potential_jump.append(list_jump_nums[a][0])
            for b in range(len(potential_jump)):
                holder = self.game.possible_jump_moves(potential_jump[b])
                for c in range(len(holder)):
                    for d in range(1,len(holder[c])):
                        coord = self.game.convert_checker_coord(holder[c][d])
                        net_value2 += self.game.board[coord[0]][coord[1]].value
                    if net_value2 == biggest_val2:
                        # biggest_val = net_value
                    # if len(holder[c]) == biggest_length2:
                        final_random_jump_selector.append((potential_jump[b],holder[c]))
                    net_value2 = 0
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

class GreedyChess(Player):
    def take_turn(self, game:CheckerBoard, chess_can_move:list) -> bool:
        self.game = game
        best_piece_val = 0
        possible_m = []

        for i in range(len(chess_can_move)):
            coord = self.game.convert_checker_coord(chess_can_move[i])
            piece = self.game.board[coord[0]][coord[1]]
            p_moves_i = piece.possible_moves(chess_can_move[i])
            for j in range(len(p_moves_i)):
                if p_moves_i[j][1] >= best_piece_val:
                    best_piece_val = p_moves_i[j][1]
        for k in range(len(chess_can_move)):
            coord = self.game.convert_checker_coord(chess_can_move[k])
            piece = self.game.board[coord[0]][coord[1]]
            p_moves_k = piece.possible_moves(chess_can_move[k])
            for l in range(len(p_moves_k)):
                if p_moves_k[l][1] == best_piece_val:
                    possible_m.append((chess_can_move[k],p_moves_k[k]))
        move_selector = random.choice(possible_m)
        self.game.move(move_selector[0],move_selector[1][0])
        print("move: " + move_selector[0] + "->"+ move_selector[1][0])
        self.game.turn += 1
        if move_selector[1][1] == 0:
            self.game.turns_without_capture += 1
        else:
            self.game.turns_without_capture = 0
        return True

class RandomChess(Player):
    def take_turn(self, game:CheckerBoard, chess_can_move:list) -> bool:
        self.game = game
        p_random_move = random.choice(chess_can_move)
        coord = self.game.convert_checker_coord(p_random_move)
        piece = self.game.board[coord[0]][coord[1]]
        p_moves_i = piece.possible_moves(p_random_move)
        p_moves_i_random = random.choice(p_moves_i)
        self.game.move(p_random_move,p_moves_i_random[0])
        print("move: " + p_random_move + "->"+ p_moves_i_random[0])
        self.game.turn += 1
        if p_moves_i_random[1] == 0:
            self.game.turns_without_capture += 1
        else:
            self.game.turns_without_capture = 0
        return True

class HumanChess(Player):
    def take_turn(self, game:CheckerBoard, chess_can_move:list) -> bool:
        self.game = game
        p_to_move = input("Select a piece to move\n")
        if not self.game.has_piece(p_to_move):
            print("No piece at that location")
            return False
        elif not self.game.is_current_player_piece(p_to_move):
            print("That is not your piece")
            return False
        coord = self.game.convert_checker_coord(p_to_move)
        piece = self.game.board[coord[0]][coord[1]]
        p_basic_moves = piece.possible_moves(self.game,p_to_move)
        if len(p_basic_moves) == 0:
            print("That piece cannot move")
            return False
        else:
            for string in self.game.display_moves(p_to_move, p_basic_moves, "chessmove"):
                print(string)
            selected_move = int(input("Select a move by entering the corresponding index\n"))
            self.game.move(p_to_move, p_basic_moves[selected_move][0])
            
            if p_basic_moves[selected_move][1] == 0:
                self.game.turns_without_capture += 1
            else:
                self.game.turns_without_capture = 0
            self.game.turn += 1
            return True