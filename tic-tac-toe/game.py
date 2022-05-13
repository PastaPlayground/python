# Basic functionality of tictactoe
# game board of 3x3
# lines

# give indices to each box

# availables moves to take

# iterate the game while there is empty space
# take note of empty space with self.board returns bool


class TicTacToe:
    def __init__(self):
        # a LIST to rep 3x3 board
        self.board = [" " in range(9)]
        # index to rep each box

        # keep track of current winner
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("|" + "|".join(row) + "|")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        # indices of each box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("|" + "|".join(row) + "|")

    def available_moves(self):
        # list comprehension method
        return [i for i, box in enumerate(self.board) if box == " "]

        # moves = []
        # for (i, box) in enumerate(self.board):
        #     # changes into a list with tuples
        #     # ['x' 'x' 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]

        #     # empty spot, append the indices of the spot to available moves
        #     if box == " ":
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    # first player starting letter
    letter = "X"

    # iterate the game while it still has empty spaces
    while game.empty_squares():
        # get move from next player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
