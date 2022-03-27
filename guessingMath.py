# print("hello world")

import random

# select level
def displayMenu():
    menuList = ["1. 1 digit", "2. 2 digits", "3. 3 digits", "4. Exit"]
    print(menuList[0])
    print(menuList[1])
    print(menuList[2])
    print(menuList[3])


# validate user level
def getUserChoice():
    userChoice = int(input("Choose a level: "))
    while userChoice > 4 or userChoice <= 0:
        print("Invalid level. Choose again: ")
        userChoice = int(input("Choose a level: "))
    else:
        return userChoice


# user guess
def getUserGuess(problem):
    # get user to guess the number
    print("Enter guess")
    print(problem, end="")
    userGuess = int(input(""))
    return userGuess


# check user's answer
# scoring system
def checkGuess(userGuess, number, count):
    # scoring system
    if userGuess == number:
        count = count + 1
        print("You are right!")
        return count
    else:
        print(f"Wrong! The hidden number is: {number}")
        # userGuess = int(input("Guess again: "))
        return count


# scoring system
def menuOption(level, count):
    if level == 1:
        number = random.randint(1, 9)
        problem = "Guess a random number from 1 - 9: "
        userGuess = getUserGuess(problem)
        count = checkGuess(userGuess, number, count)
        return count

    if level == 2:
        number = random.randint(10, 50)
        problem = "Guess a random number from 10 - 50: "
        userGuess = getUserGuess(problem)
        count = checkGuess(userGuess, number, count)
        return count

    if level == 3:
        number = random.randint(100, 200)
        problem = "Guess a random number from 100 - 200: "
        userGuess = getUserGuess(problem)
        count = checkGuess(userGuess, number, count)
        return count


def displayResults(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep="")


def main():
    # generateNumber()
    displayMenu()

    level = getUserChoice()
    total = 0
    correct = 0

    # if user continues to play
    while level != 4:
        total += 1
        correct = menuOption(level, correct)
        level = getUserChoice

    print("Exit game")
    displayResults(total, correct)


main()
