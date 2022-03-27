import string
import random

# a list of num, letters, and symbols
numbers = list(string.digits)
letters = list(string.ascii_letters)
specialCharacters = list("!@#$%^&*()_")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_")


def passwordGenerator():
    # user input number of characters
    # length_of_password = int(input("Length of password: "))

    letters_count = int(input("Number of letters in password: "))
    numbers_count = int(input("Number of digits in password: "))
    specialCharacters_count = int(input("Number of special characters in password: "))

    length_of_password = letters_count + numbers_count + specialCharacters_count

    # while length_of_password < 12:
    #     print("You need a password that is 12 or more characters!")
    #     # user input number of characters
    #     length_of_password = int(input("Length of password: "))

    # shuffle the characters for randomness
    # random.shuffle(characters)

    # init empty list
    password = []

    # random pick
    for i in range(letters_count):
        password.append(random.choice(letters))

    for i in range(numbers_count):
        password.append(random.choice(numbers))

    for i in range(specialCharacters_count):
        password.append(random.choice(specialCharacters))

    # fill up remaining spaces with random characters
    if length_of_password < 12:
        random.shuffle(characters)
        for i in range(12 - length_of_password):
            password.append(random.choice(characters))

    # # loop the list based on length of pw
    # for i in range(length_of_password):
    #     # choose random characters from list
    #     character = random.choice(characters)
    #     # password.append(character)

    #     password += character

    #     # not able to shuffle again with str
    #     # randomise pw again
    random.shuffle(password)

    # join the pw to form a string
    print("Your password is: ", end="")
    print("".join(password))


passwordGenerator()
