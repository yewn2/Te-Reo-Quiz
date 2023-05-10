"""
Component 2 (Age check) v3
More efficient method - includes valid range as the basis of the while loop
This eliminates the need to use the 'valid' variable
"""


import sys


error = "That was not a valid input. Please try again.\n"
user_age = 0

# Keep asking until a valid age (1-100) is entered
while not 1 <= user_age <= 100:
    try:
        # ask for age
        user_age = int(input("Please enter a whole number between 1 and 100.\n"
                             "What is your age? "))
        print()

    except ValueError:
        print(error)

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