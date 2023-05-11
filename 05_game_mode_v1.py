game_mode = str(input("The game modes available are:\n"
                      "\tNumbers\n"
                      "\tColours\n"
                      "\tLocation Words\n"
                      "What game mode would you like to play? ")).lower()

# keep asking until valid mode is entered
while not "numbers" == game_mode or "colours" == game_mode or "location words" == game_mode:
    print("Try again. Please enter a valid game mode (Numbers, Colours, "
          "Location Words)")
    # ask for the input
    game_mode = str(input("What game mode would you like to play? ")).lower()

# set and display game mode according to one of the three possible answers
if game_mode == "numbers":
    print("You have set the game mode to Numbers!")
if game_mode == "colours":
    print("You have set the game mode to Colours!")
if game_mode == "location words":
    print("You have set the game mode to Location Words!")