#!/usr/bin/env python3
"""HANGMAN GAME"""
import random


def word():
    """Collection of words to guess"""

    words = ["hangman", "game", "words", "collection", "python"]
    word = random.choice(words)
    return word


def hangman_image(guess):
    """Output after a wrong guesses and initial output"""

    hangman = {
        6:
        """
        ______________
        |        |
        |        
        |       
        |        
      __|__
        """,
        5:
        """
        ______________
        |        |
        |        0
        |       
        |        
      __|__
        """,
        4:
        """
        ______________
        |        |
        |        0
        |        |
        |        
      __|__
        """,
        3:
        """
        ______________
        |        |
        |        0
        |       /|
        |        
      __|__
        """,
        2:
        """
        ______________
        |        |
        |        0
        |       /|\\
        |        
      __|__
        """,
        1:
        """
        ______________
        |        |
        |        0
        |       /|\\
        |       /
      __|__
        """,
        0:
        """
        ______________
        |        |
        |        0
        |       /|\\
        |       / \\
      __|__
        """
    }
 
    for i in hangman:
        if i == guess:
            return hangman[i]


def display(word, correct_guess):
    """Display the current state of the hidden word"""

    # Generator expression
    return " ".join(l if l in correct_guess else '_' for l in word)


def hangman_game():
    """Implementation of hangman game"""

    random_word = word()
    attempts = 6
    correct_guess = set()
    incorrect_guess = set()
    

    while attempts > 0:
        print("\n", display(random_word, correct_guess))
        print(hangman_image(attempts))
        print(f"Incorrect guesses are: {', '.join(incorrect_guess)}")
        print(f"Remaining attempts: {attempts}\n")
    
        letter = input("Guess letter: ")
    
        if letter in correct_guess or letter in incorrect_guess:
            print("YOU'VE ALREADY GUESSED THAT LETTER")
            continue

        if letter in random_word:
            correct_guess.add(letter)
            if set(random_word).issubset(correct_guess):
                print("\n", display(random_word, correct_guess))
                print(f"\nCONGRATULATIONS!, YOU'VE GUESSED THE CORRECT WORD: {random_word}\n")
                break
        else:
            incorrect_guess.add(letter)
            attempts -= 1

        if attempts == 0:
            print(hangman_image(0))
            print(f"\nGAME OVER. The word was: {random_word}\n")


if __name__ == "__main__":
    print("\nHANGMAN GAME\n")

    mes = f"The following is a text-based version of the classic Hangman game, "\
        f"which uses a predefined list of words. Each player has only 6 guesses.\n"

    print(mes)

    hangman_game()
