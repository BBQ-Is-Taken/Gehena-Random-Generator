from randomCharacter import makeCharacterList
from randomItem import makeItemList, inABCOrder
from randomLocation import makeLocationList
from misc import printList, randomIntensity

quit = True
numOf = 0

while quit:
    select = input("Make a selection! (h for help):  ")

    if select == "q":
        break
    elif select == "h":
        print("Choose: Locations, Characters, Items, Intensity, or All")
        
    elif select == "Locations" or select == "L":
        numOf = input("How many Locations: ")
        printList(makeLocationList(numOf))
        
    elif select == "Characters" or select == "C":
        numOf = input("How many Characters: ")
        printList(makeCharacterList(numOf))
        
    elif select == "Items" or select == "I":
        numOf = input("How many Items: ")
        printList(makeItemList(numOf))
    
    elif select == "Intensity":
        print(randomIntensity())
        
    elif select == "All":
        numOf2, numOf3 = 0, 0
        numOf = input("How many Locations: ")
        numOf2 = input("How many Characters: ")
        numOf3 = input("How many Items: ")
        
        printList(makeLocationList(numOf))
        printList(makeCharacterList(numOf2))
        printList(makeItemList(numOf3))
        print(randomIntensity())
        
    elif select == "ABC":
        inABCOrder()
        
    else:
        print("Choose an option!")
    print()
