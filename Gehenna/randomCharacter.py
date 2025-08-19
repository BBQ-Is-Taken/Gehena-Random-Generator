import random

character = open("Characters.txt")
lines = character.readlines()
repeatNums = set()
randNum = 0

def getCharacter(num):
    selectedCharacter = lines[num].strip()
    return selectedCharacter

def newRandomNumber():
    num = random.randint(0, len(lines)-1)
    return num

def makeCharacterList(numCharacters): #Returns a list of the random characters- rewritten for easier future use!
    randNum = newRandomNumber()
    x = 0
    saverList = list()
    
    if not numCharacters.isdigit(): # If statements to get valid input
        print("Must be a number!")
    elif int(numCharacters) > len(lines):
        print(f"Too long! Max of {len(lines)}!")
    elif int(numCharacters) <= 0:
        print("Must be over 0!")
    else:
        while x < int(numCharacters):
            if randNum in repeatNums:
                randNum = newRandomNumber()
            else:
                repeatNums.add(randNum)
                saverList.append(getCharacter(randNum))
                randNum = newRandomNumber()
                x += 1
    return saverList



# START OF LOOP
# All this does is makes the list with the number of characters and prints it

def printCharacters():
    quit = True

    while quit:
        nc = input("How many characters: ")
        print()

        if nc == "q":
            break
        else:
            characterList = makeCharacterList(nc)

            for x in range(len(characterList)):
                print(f"{x+1} : {characterList[x]}")


        repeatNums.clear()                
        print()



character.close()
