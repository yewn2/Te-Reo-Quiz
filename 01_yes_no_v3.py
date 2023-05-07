"""
LU Yes/No
Puts the code created in v2 into a loop to make testing easier and more
efficient.
"""
played_before = ""

while played_before != "x":
    # Ask the user if they have played before
    played_before = str(input("Have you played before? ")).strip().lower()

    # If they say yes,  output 'Program Continues'
    if played_before == "yes" or played_before == "y":
        print("Program Continues")

    # If they say no , output 'Display Instructions'
    elif played_before == "no" or played_before == "n":
        print("Display Instructions")

    # Otherwise - show error
    else:
        print(" please input yes or no")

    print(f"You entered {played_before}")