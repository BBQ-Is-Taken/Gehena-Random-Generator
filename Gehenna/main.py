from randomCharacter import makeCharacterList, printCharacters
from randomLocation import makeLocationList, printLocations

quit = True

while quit:
    select = input("Make a selection! (h for help):  ")

    if select == "q":
        break
    elif select == "h":
        print("Choose Locations or Characters")
    elif select == "Locations":
        printLocations()
    elif select == "Characters":
        printCharacters()
    else:
        print("Choose an option!")
    print()
