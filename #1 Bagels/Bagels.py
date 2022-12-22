"""Bagels: A deductuive logic game where you must guess a number based on clues."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digit 0 to 9
    random.shuffle(numbers) # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def get_clues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        print('You got it!')

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the corret place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorret place.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their originarl order
        # doesn't give informatin away
        clues.sort()

        # Make a single string from the list of string clues.
        return ' '.join(clues)
def main():
    print(f'''Bagels, a deductive logic game.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong postision.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.''')

    while True:
        # This stores the secret number the player needs to guess:
        secretNUM = get_secret_num()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'\nGuess #{numGuesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secretNUM)
            print(clues)
            numGuesses += 1

            if guess == secretNUM:
                break # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNUM}.')

        # ASK PLAYER IF THEY WANT TO PLAY AGAIN
        print('\nDo you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')


if __name__ == '__main__':
    main()