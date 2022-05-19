import random


# select level
def displayMenu():
    menuList = ["1. 1 digit", "2. 2 digits", "3. 3 digits", "4. Exit"]
    print("Choose a level")
    for choice in menuList:
        print(choice)


# validate user level
def getUserChoice():
    userChoice = int(input("Choose a level: "))
    while userChoice > 4 or userChoice <= 0:
        print("Invalid level. Choose again: ")
        userChoice = int(input("Choose a level: "))
    if userChoice == 1:
        level1()
    elif userChoice == 2:
        level2()


def level1():
    number = random.randint(1, 9)
    userGuess = int(input("Guess a number from 1 - 9: "))
    while userGuess != number:
        print(f"Wrong! Guess again")
        userGuess = int(input("Guess a number from 1 - 9: "))
    else:
        print(f"Correct! The number is {number}")
        userInput = input("Enter next level? Y/N: ").upper()
        if userInput == "Y":
            print("Entering Level 2 ...")
            level2()
        else:
            print("Thanks for playing!\n Exiting Jankenpon ...")


def level2():
    number = random.randint(10, 20)
    userGuess = int(input("Guess a number from 10 - 20: "))
    while userGuess != number:
        print(f"Wrong! Guess again")
        userGuess = int(input("Guess a number from 10 - 20: "))
    else:
        print(f"Correct! The number is {number}")
        userInput = input("Enter next level? Y/N: ").upper()
        if userInput == "Y":
            print("Entering Level 2 ...")
            level2()
        else:
            print("Thanks for playing!\n Exiting Jankenpon ...")


def main():
    displayMenu()
    getUserChoice()


main()
