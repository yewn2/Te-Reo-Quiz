"""
Component 3 (Game mode) v2
More efficient method, using a try/finally loop and eliminating the longer
'if' statement at the end
Also uses a list of the possible modes
"""

error = "Try again. Please enter a valid game mode (Numbers, Colours, " \
        "Location Words)\n"
modes = ["numbers", "colours", "location words"]
valid = False
game_mode = ""

# keep asking until valid mode is entered
while not valid:
    try:
        # ask for game mode
        game_mode = str(input("The game modes available are:\n"
                              "\t(1) Numbers\n"
                              "\t(2) Colours\n"
                              "\t(3) Location Words\n"
                              "What game mode would you like to play? ")).lower()
        print()
        if game_mode != modes[0] and game_mode != modes[1] and \
           game_mode != modes[2 ]:
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
                  .format(game_mode.title()))