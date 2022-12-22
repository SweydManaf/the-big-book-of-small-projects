"""Bagels: A deductuive logic game where you must guess a number based on clues."""

import random

class Bagels:
    def __init__(self):
        self.NUM_DIGITS = 3
        self.numGuesses = 1
        self.MAX_GUESSES = 10

        self.secretNum = self.get_secret_num()
        self.guess = ''
        self.win = None


    def get_secret_num(self):
        """Returns a string made up of NUM_DIGITS unique random digits."""
        numbers = list('0123456789')  # Create a list of digit 0 to 9
        random.shuffle(numbers)  # Shuffle them into random order.

        # Get the first NUM_DIGITS digits in the list for the secret number:
        secretNum = ''
        for i in range(self.NUM_DIGITS):
            secretNum += str(numbers[i])
        return secretNum

    def main_game(self):
        if len(self.guess) != self.NUM_DIGITS or not self.guess.isdecimal():
            pass
        else:
            clues = self.get_clues(self.guess, self.secretNum)

            if self.numGuesses == self.MAX_GUESSES:
                self.win = 0
                return f'You ran out of guesses.\nThe answer was {self.secretNum}.'
            else:
                return clues

    def get_clues(self, guess, secretNum):
        """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
        if guess == secretNum:
            self.win = 1
            return 'You got it!'
        else:
            self.numGuesses += 1
        clues = []

        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                # A correct digit is in the corret place.
                clues.append('Fermi')
            elif guess[i] in secretNum:
                # A correct digit is in the incorret place.
                clues.append('Pico')

        if len(clues) == 0:
            return 'Bagels'  # There are no correct digits at all.
        else:
            # Sort the clues into alphabetical order so their originarl order
            # doesn't give informatin away
            clues.sort()

            # Make a single string from the list of string clues.
            return ' '.join(clues)

    def reset(self):
        self.NUM_DIGITS = 3
        self.numGuesses = 1
        self.MAX_GUESSES = 10
        self.win = None

        self.secretNum = self.get_secret_num()