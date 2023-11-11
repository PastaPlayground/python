import string
import random
import os.path
import datetime
import encrypt_file
import load_key
import decrypt_file


# a list of num, letters, and symbols
numbers = list(string.digits)
letters = list(string.ascii_letters)
specialCharacters = list("!@#_")


def passwordGenerator():
    account = input("Generating password for: ")
    min_len = 14

    # random number for each type of characters
    letters_count = 6
    numbers_count = 4
    specialCharacters_count = random.randint(
        1, min_len - letters_count - numbers_count)

    # init empty list to append characters
    password = []

    # random pick
    for _ in range(letters_count):
        password.append(random.choice(letters))

    for _ in range(numbers_count):
        password.append(random.choice(numbers))

    for _ in range(specialCharacters_count):
        password.append(random.choice(specialCharacters))

    # append extra characters when min length is not met
    total = letters_count + numbers_count + specialCharacters_count
    if total != min_len:
        remain = min_len - total
        for _ in range(remain):
            password.append(random.choice(letters))

    random.shuffle(password)
    password = "".join(password)

    print("Generated new password!", end="\n \n")

    # save password to a txt file with timestamp
    today = datetime.datetime.now().strftime("%Y:%m:%d")

    # get random username
    # usernames = open("usernames.txt").read().splitlines()
    with open("usernames.txt") as usernames:
        lines = usernames.read().splitlines()
        username = random.choice(lines)

    with open("passwords.txt", "a") as file:
        file.write(f'{account} {username} {password}\n')


if __name__ == "__main__":

    # check if user wants to view passwords or add new passwords
    print("1. View all passwords")
    print("2. Add new password")
    action = int(input("Choice 1 or 2: "))

    # load key
    key = load_key.load_key()
    print("Key loaded")

    if action == 1:
        try:
            if os.path.isfile("./passwords.txt"):
                print("File exist")
                # decrypt the existing file
                file = decrypt_file.decrypt("passwords.txt", key)
                print("Decrypting file ...")
                print(file.read())

            else:
                print("File does not exist")
        finally:
            exit

    elif action == 2:
        try:
            if os.path.isfile("./passwords.txt"):
                print("File exist")
                # decrypt the existing file
                file = decrypt_file.decrypt("passwords.txt", key)
                print("Decrypting file ...")
                print(file)
            else:
                print("File does not exist")
        finally:
            print(2)

    # try:
    #     if os.path.isfile("./passwords.txt"):
    #         print("File exist")
    #         # decrypt the existing file
    #         file = decrypt_file.decrypt("passwords.txt", key)
    #         print("Decrypting file ...")
    #         print(file)
    #     else:
    #         # create a new password file and encrypt it
    #         print("Creating passwords file ...")
    #         file = open("passwords.txt", "x")
    #         print("Created passwords file!")

    #         encrypt_file.encrypt("passwords.txt", key)
    # finally:
    #     # write file
    #     passwordGenerator()
    #     print("Writing to file ...")
    #     print("Please wait a moment ...")

    #     # encrypt file
    #     encrypt_file.encrypt("passwords.txt", key)

    #     print("Encrypting file ....")
    #     print("Encrypted passwords file!")
