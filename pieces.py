B_PEASANT = '\u2688'
W_PEASANT = '\u2686'
B_KING = '\u2689'
W_KING = '\u2687'

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
