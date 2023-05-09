"""
Component 2 (Age check) v1
Ask user how old they are and check that the input is a valid integer between
1 and 100.If this integer is between 5 and 15, the user is the right age
to play the game.
"""


import sys


user_age = int(input("What is your age? (must be a whole number "
                     "between 1 and 100) "))

# Keep asking until a valid age is entered
while not 1 <= user_age <= 100:
    print("Try again. Please enter a whole number between 1 and 100.")
    # ask for the input
    user_age = int(input("What is your age? "))

# If age is not between 5 and 15, the user is too young/old to play the game;
# terminate the program at this point
if user_age < 5:
    print("Sorry, you are too young to play this quiz.")
    sys.exit()
elif user_age > 15:
    print("Sorry, you are too old to play this quiz.")
    sys.exit()
else:
    print("You are the perfect age to play this quiz!")