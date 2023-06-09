"""
Component 4 (Māori terms) v1
used to display terms, in English and Māori
"""


# game mode used for testing
game_mode = "Numbers"
# possible game modes
game_modes = ["Numbers", "Colours", "Location Words"]
# Two statements to show the user the language terms
māori_statement = "These are the Māori {}".format(game_mode)
english_statement = "These are the English {}".format(game_mode)
# the māori terms and corresponding english terms beneath
māori_numbers = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru",
                 "iwa", "tekau"]
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
if game_mode == game_modes[0]:
    print(māori_statement)
    print(māori_numbers)
    print(english_statement)
    print(numbers)
elif game_mode == game_modes[1]:
    print(māori_statement)
    print(māori_colours)
    print(english_statement)
    print(colours)
else:
    print(māori_statement)
    print(māori_locatives)
    print(english_statement)
    print(locatives)