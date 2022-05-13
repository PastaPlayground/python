import random

# list of words to guess from
from words import words
import string

# Step1: computer choose a random word from words
# Step2: break down word into letters
# Step3: guess the letters

# get the basic functions of hangman down
# keep track of the letters guessed
# check if letter is in word
# check if letter is guessed multiple times
# check if wrong letter is guessed
# using a while loop to allow user to guess the letters till completed

# reveal letter in word

# adding lives to limit the amount of guesses


def get_valid_word(words):
    word = random.choice(words)

    # if word contains - or space, choose another word
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    # get a word
    word = get_valid_word(words)

    # letters in a word
    # used to keep track what has been guessed
    # use set to get iterables, no repeated elements
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)

    # track guessed letters
    # empty set
    used_letters = set()

    # lives = amount of guess
    lives = 10

    # user keeps guessing as long as there is still valid letters
    while len(word_letters) > 0 and lives > 0:

        # letting the user to know what letters have been guessed
        print(
            f"You have {lives} lives left and used these letters: ",
            " ".join(used_letters),
        )

        # print word with - as letters not guessed
        # show letters that have been guessed
        # W - R D
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        # get user input
        user_letter = input("Guess a letter: ").upper()

        # valid letter that has not been used
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            # correct letter guessed
            # remove it from the word combination
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            # wrong letter guessed
            else:
                lives = lives - 1
                print("Letter is not in the word")

        # user entered same letter more than once
        elif user_letter in used_letters:
            print(f"You have guessed {user_letter} before. Try again!")

        # invalid character
        else:
            print("Invalid character. Try again!")

    # if user ran out of guesses
    if lives == 0:
        print(f"You died. The word is {word}")
    else:
        print(f"You won! The word is {word} ")


hangman()
