import random

character = open("Characters.txt")
lines = character.readlines()
quit = True
repeatNums = set()
randNum = 0

def getCharacter(num):
    selectedCharacter = lines[num].strip()
    return selectedCharacter

def newRandomNumber():
    num = random.randint(1, len(lines)-1)
    return num

    
while quit:
    numCharacters = input("How many characters: ")
    print()
    randNum = newRandomNumber()
    x = 0
    
    if numCharacters == "q":
        break
    else:
        while x < int(numCharacters):
            if randNum in repeatNums:
                randNum = newRandomNumber()
            else:
                repeatNums.add(randNum)
                print(getCharacter(randNum))
                randNum = newRandomNumber()
                x += 1
        print()
                
    repeatNums.clear()                
    print()
character.close()