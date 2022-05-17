import random
import time
from enum import IntEnum

# python class for storing var and values
class Moves(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# get user choice
def getUserMove():
    # dynamic way of printing
    moves = [f"{move.value}. {move.name}" for move in Moves]
    print("- - - MOVES AVAILABLE - - -")
    moves_str = ", ".join(moves)
    print(moves_str)

    # user select move by typing string
    userSelection = int(input("Your move: "))
    userMove = Moves(userSelection)
    print(f"You choose {userMove.name}")
    return userMove


# randomise computer choice
def getComputerMove():
    print("Computer is choosing a move . . .")
    time.sleep(1.2)

    computerSelection = random.randint(1, len(Moves))
    computerMove = Moves(computerSelection)
    print(f"Computer choose {computerMove.name}")
    return computerMove


def jankenpon(userMove, computerMove):
    userScore = 0
    computerScore = 0

    # check logic
    if userMove == computerMove:
        print(f"ITS A TIE")

    elif userMove == Moves.ROCK:
        if computerMove == Moves.SCISSORS:
            print("YOU WIN!")
            userScore += 1
        else:
            print("YOU LOSE!")
            computerScore += 1

    elif userMove == Moves.PAPER:
        if computerMove == Moves.ROCK:
            print("YOU WIN!")
            userScore += 1
        else:
            print("YOU LOSE!")
            computerScore += 1

    elif userMove == Moves.SCISSORS:
        if computerMove == Moves.PAPER:
            print("YOU WIN!")
            userScore += 1
        else:
            print("YOU LOSE!")
            computerScore += 1


while True:
    try:
        userMove = getUserMove()

    # if user enter a value not in Moves
    except ValueError as e:
        movesRange = f"[1, {len(Moves)}]"
        print(f"INVALID MOVE. ENTER A MOVE VALUE FROM {movesRange}")
        continue

    computerMove = getComputerMove()
    jankenpon(userMove, computerMove)

    playAgain = input("Play again? (y/n): ")

    if playAgain.lower() != "y":
        print("THANKS FOR PLAYING JANKENPON!")
        print("EXITING JANKENPON . . .")
        break
