import random


def rollDice():
    choice = input("Roll dice? Y/N: ")

    if choice.upper() == "Y":
        print("Guess a number between 1 and 6! ", end="")
        answer = int(input(""))
        if answer < 1 or answer > 6:
            print("Guess a number between 1 and 6! ", end="")
            answer = input("")

        dice = random.randint(1, 6)

        if int(answer) == dice:
            print(f"You got it right! ")
            rollDice()
        else:
            print(f"The number is {dice}")
            print("Try again! ")
            rollDice()

    elif choice.upper() == "N":
        print("Exiting dice game ... ")

    else:
        print("Invalid option! Choose Y/N")
        rollDice()


def main():

    rollDice()


main()
