###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# IMPORTS
import random

# FUNCTIONS


def get_guess():
    """
    Function to get user's guesses.

    User input 3 single digits number one after another

    Return:
        guess (Array): List with user's 3 digits in String format 
    """

    # Get user's digits in a List
    guess = list(input("Tell us your 3 single digits guesses: "))

    return guess


def generate_numbers():
    """
    Function to generate 3 random digits to be guessed.  

    Generate 3 random in a list in order to be compare to the user's digits.

    Return:
        str_digits (Array): List with 3 random digits converted to String
    """

    # List comprehension to generate numbers from 0 to 9 and cast it as String
    str_digits = [str(num) for num in range(10)]

    # Shuffle randomly the list
    random.shuffle(str_digits)

    return str_digits[:3]


def generate_clues():
    """
    Function to compare user and game numbers.

    Check if number has been guessed or if there is some match or even close to
    guess the game's number. 

    Returns: 
        String message 
    """

    if user_numbers == game_numbers:
        return ["GAME CRACKED"]

    clues = []  # Empty List to add the messages

    # Use enumerate to loop into individual numbers
    for i, num in enumerate(user_numbers):
        if num == game_numbers[i]:
            clues.append("MATCH")
        elif num in game_numbers:
            clues.append("CLOSE")

    if clues == []:
        return ["GUESS AGAIN"]
    else:
        return clues


# RUN GAME FUNCTIONS

print("\n*** WELCOME TO THE GAME ***")

# Call function to get random numbers to be guessed
game_numbers = generate_numbers()
print("Game has generated 3 numbers, Can you guess them??? ", game_numbers)

# Create empty list to get messages
clues = []

while clues != ["GAME CRACKED"]:

    # Call function to get user's numbers
    user_numbers = get_guess()
    print("User's numners: ", user_numbers)
    print("Game's numbers: ", game_numbers)  # To debug

    clues = generate_clues()

    for clue in clues:
        print(clue)
