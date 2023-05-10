"""
Component 2 (Age check) v2
Use try/accept and pull error message out of the loop
"""


import sys


error = "Try again. Please enter a whole number between 1 and 100.\n"
valid = False

# Keep asking until a valid age (1-100) is entered
while not valid:
    try:
        # ask for age
        user_age = int(input("What is your age? (must be a whole number "
                             "between 1 and 100) "))

        # check if amount is too high/low
        if 0 < user_age < 100:
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
                valid = True
        else:
            print(error)

    except ValueError:
        print(error)