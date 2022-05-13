import math
import random

# Step 1: create a Player class with basic functionality of Computer and Human players
# Step 2:


# base class of a Player
# allows Computer and Human player to be built based off this class
# basic functions needed of a player
class Player:
    def __init__(self, letter):
        # player letter X or O
        self.letter = letter

    def get_move(self, game):
        pass


# Computer Player
# based off Player class
class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # referencing game.py
        # get a random spot
        square = random.choice(game.available_moves())
        return square


# Human Player
# based off Player class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-9) ")

            # check if the input is valid
            # convert to int
            # if box is unavailable, input will be invalid as well

            try:
                val = int(square)
                # invalid input
                if val not in game.available_moves():
                    raise ValueError
                # valid input
                valid_square = True

            except ValueError:
                print("Invalid square. Try again")
        return val
