"""
LU Yes/No
Based on 01_yes_no_v3
"""


# Functions go here:
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


# Main routine goes here:
played_before = yes_no("Have you played this game before?")
print(f"You entered {played_before}")
having_fun = yes_no("Are you having fun?")
print(f"You entered {having_fun}")