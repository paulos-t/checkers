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
