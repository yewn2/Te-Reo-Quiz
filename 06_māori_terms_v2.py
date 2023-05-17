"""
Component 4 (Māori terms) v2
changing v1 into a function for easier use
"""


def show_terms(mode_used):
    # possible game modes
    game_modes = ["Numbers", "Colours", "Location Words"]
    # Two statements to show the user the language terms
    māori_statement = "These are the Māori {}".format(game_mode)
    english_statement = "These are the English {}".format(game_mode)
    # the māori terms and corresponding english terms beneath
    māori_numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu",
                     "waru", "iwa", "tekau"]
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight",
               "nine", "ten"]
    māori_colours = ["whero", "karaka", "kōwhai", "kākāriki", "kikorangi",
                     "waiporoporo", "paraone", "māwhero", "mā", "pango"]
    colours = ["red", "orange", "yellow", "green", "blue", "purple", "brown",
               "pink", "white", "black"]
    māori_locatives = ["kei", "runga", "raro", "roto", "muri", "waenganui", "mauῑ",
                       "matau", "mua", "waho"]
    locatives = ["at", "on", "under", "inside", "behind", "in between", "left side",
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


# main routine
game_mode = "Numbers"
show_terms(game_mode)