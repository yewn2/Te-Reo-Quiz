"""
Version 2 - Te Reo Quiz base component
"""

# Imports
import sys
import random


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
             "Please enter a valid number between {} and {}\n".format(low,
                                                                      high))

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
                                    "What game mode would you like to "
                                    "play? ")).lower()
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


# show the terms in māori and english
def show_terms(mode_used):
    # possible game modes
    game_modes = ["Numbers", "Colours", "Location Words"]
    # Two statements to show the user the language terms
    māori_statement = "These are the Māori {}".format(game_mode)
    english_statement = "These are the English {}".format(game_mode)
    # the māori terms and corresponding english terms beneath
    māori_numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu",
                     "waru",
                     "tekau"]
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight",
               "nine", "ten"]
    māori_colours = ["whero", "karaka", "kōwhai", "kākāriki", "kikorangi",
                     "waiporoporo", "paraone", "māwhero", "mā", "pango"]
    colours = ["red", "orange", "yellow", "green", "blue", "purple", "brown",
               "pink", "white", "black"]
    māori_locatives = ["kei", "runga", "raro", "roto", "muri", "waenganui",
                       "mauῑ",
                       "matau", "mua", "waho"]
    locatives = ["at", "on", "under", "inside", "behind", "in between",
                 "left side",
                 "right side", "in front", "outside"]
    if mode_used == game_modes[0]:
        print(māori_statement)
        print(māori_numbers)
        print(english_statement)
        print(numbers)
    elif mode_used == game_modes[1]:
        print(māori_statement)
        print(māori_colours)
        print(english_statement)
        print(colours)
    else:
        print(māori_statement)
        print(māori_locatives)
        print(english_statement)
        print(locatives)
    keep_going = input("Press enter when finished.")
    # prints ten thousand lines to prevent cheating
    for i in range(1, 10000):
        print()


# generate a random question, check the answer and award points accordingly
def question_answer_points(mode_used, question_amount):
    game_modes_ = ["Numbers", "Colours", "Location Words"]
    points = 0
    questions = 1

    # terms + answers
    numbers = {'tahi': 'one',
               'rua': 'two',
               'toru': 'three',
               'whā': 'four',
               'rima': 'five',
               'ono': 'six',
               'whitu': 'seven',
               'waru': 'eight',
               'iwa': 'nine',
               'tekau': 'ten'}

    colours = {'whero': 'red',
               'karaka': 'orange',
               'kōwhai': 'yellow',
               'kākāriki': 'green',
               'kikorangi': 'blue',
               'waiporoporo': 'purple',
               'paraone': 'brown',
               'māwhero': 'pink',
               'mā': 'white',
               'pango': 'black'}

    location_words = {'kei': 'at',
                      'runga': 'on',
                      'raro': 'under',
                      'roto': 'inside',
                      'muri': 'behind',
                      'waenganui': 'in between',
                      'mauῑ': 'left side',
                      'matau': 'right side',
                      'mua': 'in front',
                      'waho': 'outside'}

    # answer list
    answers = []

    # question template + error message
    question = "Question {}\n" \
               "The Māori term '{}' in English is:\n" \
               "\t(1) {}\n" \
               "\t(2) {}\n" \
               "\t(3) {}\n" \
               "Please answer with what is written.\n" \
               "Answer: "
    error = "Please enter one of the three listed answers.\n"

    # sets amount of questions
    while questions <= question_amount:
        # picking term + answer according to game mode
        if mode_used == game_modes_[0]:
            t_a = random.choice(list(numbers.items()))
            answers = ["one", "two", "three", "four", "five", "six", "seven", "eight",
                       "nine", "ten"]
        elif mode_used == game_modes_[1]:
            t_a = random.choice(list(colours.items()))
            answers = ["red", "orange", "yellow", "green", "blue", "purple", "brown",
                       "pink", "white", "black"]
        else:
            t_a = random.choice(list(location_words.items()))
            answers = ["at", "on", "under", "inside", "behind", "in between",
                       "left side", "right side", "in front", "outside"]

        # assigning term
        term = t_a[0]

        # setting 1 correct and 2 incorrect answers according to game mode
        correct_ans = t_a[1]
        incorrect_1 = random.choice(answers)
        incorrect_2 = random.choice(answers)

        # check for same answers
        while not incorrect_1 != incorrect_2 != correct_ans:
            while incorrect_1 == incorrect_2:
                incorrect_1 = random.choice(answers)
            while correct_ans == incorrect_1:
                incorrect_1 = random.choice(answers)
            while correct_ans == incorrect_2:
                incorrect_2 = random.choice(answers)
        answer_list = [correct_ans, incorrect_1, incorrect_2]

        # setting 3 choices randomly and checking to make sure
        # there are no duplicates
        choice1 = random.choice(answer_list)
        choice2 = random.choice(answer_list)
        choice3 = random.choice(answer_list)
        while not choice1 != choice2 != choice3 != choice1:
            while choice1 == choice2:
                choice1 = random.choice(answer_list)
            while choice2 == choice3:
                choice2 = random.choice(answer_list)
            while choice1 == choice3:
                choice3 = random.choice(answer_list)

        # print the question
        answer = input(question.format(questions, term, choice1,
                                       choice2, choice3)).lower()

        # make sure that answer is one of the choices
        while answer != choice1 and answer != choice2 and answer != choice3:
            print(error)
            answer = input(question.format(questions, term, choice1,
                                           choice2, choice3)).lower()

        # correct/incorrect statements
        corr_state = "Correct! +50 points"
        incorr_state = "Incorrect! -20 points"

        # check if answer is correct
        if answer == correct_ans:
            print(corr_state)
            points += 50
        else:
            print(incorr_state)
            points -= 20
        questions += 1
    return points


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

# showing the terms according to the game mode
show_terms(game_mode)

# generate 5 questions, get points
questions_needed = 5
total_points = question_answer_points(game_mode, questions_needed)
print(total_points)
