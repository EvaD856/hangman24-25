'''
HANGMAN
Author: Eva Donahue
Based on: Al Sweigart's Hangman from The Big Book of Small Python Projects
'''

# Imports 
import random, sys 


# ASCII Graphics 
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 0  |
    |
    |
    |
=====
""",
r"""
 +--+
 |  |
 0  |
 |  |
    |
    |
=====
""",
r"""
 +--+
 |  |
 0  |
/|  |
    |
    |
=====
""",
r"""
 +--+
 |  |
 0  |
/|\ |
    |
    |
=====
""",
r"""
 +--+
 |  |
 0  |
/|\ |
/   |
    |
=====
""",
r"""
 +--+
 |  |
 0  |
/|\ |
/ \ |
    |
=====
""",
]


# Categories & Word section
CATEGORY = 'Animals'

WORDS = 'ANT BADGER BEAVER DONKEY EAGLE GOOSE LIZARD MONKEY MOUSE PARROT PYTHON RABBIT SPIDER TURTLE WEASEL WOMBAT SHARK'.split()


# Main Program Function
def main():
    print("Hangman, by Eva Donahue")
    print("=========================================================\n")
    print("based on Al Sweigart's Big Book of Small Python Projects\n\n")

    #Setup variable for a new game:
    missedLetters = [] # List of incorrect letter guesses 
    correctLetters = [] # List of correct letter guesses.
    secretWord = random.choice(WORDS)  



'''
Draw the current state of the hangman game, along with the missed and correctly guessed letters of the secret word
'''
def drawHangman(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category selected is:', CATEGORY)
    print()

    # Show the incorrectly guessed letters


    # Display the blanks for the secret word (one blank per letter)
    blanks = ['_'] * len(secretWord)

    # Replace blanks with correctly guessed letters:


    # Show the secret word with spaces in between each letter
  
'''
Returns the letter the player entered. This function makes sure the player entered a single letter that they haven't guessed before 
'''



# If this program was run(instead of imported), run the game: 
if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-C is pressed, end the program
