"""
Component 5 (Question, Answer, Points) v1
First version of a component which will first pick a random question from 10
options, then check that the user's answer is correct, then award points
according whether the answer is correct or not. This then repeats 5 times to
make a quiz.
"""


# Imports
import random

# game mode for testing
game_mode = "Numbers"
game_modes_ = ["Numbers", "Colours", "Location Words"]

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

# question template
question = "The Māori term '{}' in English is:\n" \
           "\t(1) {}\n" \
           "\t(2) {}\n" \
           "\t(3) {}\n"

# picking term + answer according to game mode
if game_mode == game_modes_[0]:
    t_a = random.choice(list(numbers.items()))
    answers = ["one", "two", "three", "four", "five", "six", "seven", "eight",
               "nine", "ten"]
elif game_mode == game_modes_[1]:
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
answer_list = [correct_ans, incorrect_1, incorrect_2]

# check for same answers
while not incorrect_1 != incorrect_2 != correct_ans:
    while incorrect_1 == incorrect_2:
        incorrect_1 = random.choice(answers)
    while correct_ans == incorrect_1:
        incorrect_1 = random.choice(answers)
    while correct_ans == incorrect_2:
        incorrect_2 = random.choice(answers)

# setting 3 choices randomly and checking to make sure there are no duplicates
choice1 = random.choice(answer_list)
choice2 = random.choice(answer_list)
choice3 = random.choice(answer_list)
while not choice1 != choice2 != choice3:
    while choice1 == choice2:
        choice1 = random.choice(answer_list)
    while choice2 == choice3:
        choice2 = random.choice(answer_list)
    while choice1 == choice3:
        choice3 = random.choice(answer_list)

# print the question
answer = input(question.format(term, choice1, choice2, choice3))
