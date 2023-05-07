# Ask the user if they have played before
played_before = str(input("Have you played before?"))

# If they say yes,  output 'Program Continues'
if played_before == "yes":
    print("Program Continues")

# If they say no , output 'Display Instructions'
elif played_before == "no":
    print("Display Instructions")

# Otherwise - show error
else:
    print(" please input yes or no")