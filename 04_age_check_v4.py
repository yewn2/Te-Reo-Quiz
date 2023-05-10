"""
Component 2 (Age check) v4
Puts v3 into a function for easier use
"""


import sys


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


# Main routine
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
