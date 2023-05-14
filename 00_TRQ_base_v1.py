"""
Version 1 - Te Reo Quiz base component
"""


# Imports
import sys


# Functions
# yes/no checking function
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = str(input(question_text)).strip().lower()

        # If they say yes,  output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no , output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print(" please input yes or no")


# function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the quiz will go here")
    print()
    print("Program continues")
    print()


# age checking function
def num_check(question, low, high):
    error = ("That was not a valid input\n"
             "Please enter a valid number between {} and {}\n".format(low, high))

    # Keep asking until a valid amount (1-100) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# function to set the game mode
def mode():
    error = "Try again. Please enter a valid game mode (Numbers, Colours, " \
            "Location Words)\n"
    modes = ["numbers", "colours", "location words"]
    valid = False
    game_mode_1 = ""

    # keep asking until valid mode is entered
    while not valid:
        try:
            # ask for game mode
            game_mode_1 = str(input("The game modes available are:\n"
                                  "\t(1) Numbers\n"
                                  "\t(2) Colours\n"
                                  "\t(3) Location Words\n"
                                  "What game mode would you like to play? ")).lower()
            print()
            if game_mode_1 != modes[0] and game_mode_1 != modes[1] and \
               game_mode_1 != modes[2]:
                valid = False
            else:
                valid = True

        finally:
            if not valid:
                print(error)
            else:
                # set and display game mode according to one of the three
                # possible answers
                print("You have set the game mode to {}."
                      .format(game_mode_1.title()))
                return game_mode_1


# Main routine goes here:
# checking if the user has played yet
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# checking the user's age
user_age = num_check("What is your age? ", 1, 100)
# If age is not between 5 and 15, the user is too young/old to play
# the quiz; terminate the program at this point
if user_age < 5:
    print("Sorry, you are too young to play this quiz.")
    sys.exit()
elif user_age > 15:
    print("Sorry, you are too old to play this quiz.")
    sys.exit()
else:
    print("You are the perfect age to play this quiz!")

# setting the game mode
game_mode = mode().title()