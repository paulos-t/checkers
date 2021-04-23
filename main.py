## Main module for the assignment

class CheckerBoard():

    rows, cols = (8, 8)

    b_space = '\u25fc'
    w_space = '\u25fb'
    b_peasant = '\u2688'
    w_peasant = '\u2686'
    b_king = '\u2689'
    w_king = '\u2687'

    def __init__(self):
        # self.board = [["n"] * CheckerBoard.cols] * CheckerBoard.rows
        self.board = ["n"] * CheckerBoard.cols

        

    # def __repr__(self):
    #     for row in self.board:
    #         print("1 " + )
            


class Piece():
    def __init__(self, color):
        if color == 'b':
            self.color = '\u2688'
        elif color == 'w':
            self.color = '\u2686'
        else:
            print("Please provide a valid color")


if __name__ == "__main__":
    new = CheckerBoard()
    print(new.board)