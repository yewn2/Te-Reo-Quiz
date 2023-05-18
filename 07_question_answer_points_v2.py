"""
Component 5 (Question, Answer, Points) v2
This version will form v1 into a function
"""


# Imports
import random


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

        incorrect_1 = t_a[1]
        incorrect_2 = t_a[1]

        # check for same answers
        while correct_ans == incorrect_1 or correct_ans == incorrect_2 or incorrect_1 == incorrect_2:
            incorrect_1 = random.choice(answers)
            incorrect_2 = random.choice(answers)
        answer_list = [correct_ans, incorrect_1, incorrect_2]

        # setting 3 choices randomly and checking to make sure
        # there are no duplicates
        choice1 = ""
        choice2 = ""
        choice3 = ""

        while choice1 == choice2 or choice1 == choice3 or choice2 == choice3:
            choice1 = random.choice(answer_list)
            choice2 = random.choice(answer_list)
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


# Main routine
game_mode = "Numbers"
questions_needed = 5
total_points = question_answer_points(game_mode, questions_needed)
print(total_points)
