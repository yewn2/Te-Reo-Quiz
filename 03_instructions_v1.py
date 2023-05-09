"""
Took the function from component 02_v1 as the basis for this new function.
Incorporates both yes/no and show instructions.
"""


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


# Main routine goes here:
played_before = yes_no("Have you played this game before?")

if played_before == "No":
    instructions()
else:
    print("Program continues")