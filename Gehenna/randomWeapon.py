import random

weapon = open("Weapons.txt")
lines = weapon.readlines()
repeatNums = set()
randNum = 0

def getWeapon(num):
    selectedWeapon = lines[num].strip()
    return selectedWeapon

def newRandomNumber():
    num = random.randint(0, len(lines)-1)
    return num

def makeWeaponList(numWeapons): #Returns a list of the random weapons- rewritten for easier future use!
    randNum = newRandomNumber()
    x = 0
    saverList = list()
    
    if not numWeapons.isdigit(): # If statements to get valid input
        print("Must be a number!")
    elif int(numWeapons) > len(lines):
        print(f"Too long! Max of {len(lines)}!")
    elif int(numWeapons) <= 0:
        print("Must be over 0!")
    else:
        while x < int(numWeapons):
            if randNum in repeatNums:
                randNum = newRandomNumber()
            else:
                repeatNums.add(randNum)
                saverList.append(getWeapon(randNum))
                randNum = newRandomNumber()
                x += 1
    return saverList



# START OF LOOP
def printWeapons():
    quit = True

    while quit:
        nc = input("How many Weapons: ")
        print()

        if nc == "q":
            break
        else:
            weaponsList = makeWeaponList(nc)

            for x in range(len(weaponsList)):
                print(f"{x+1} : {weaponsList[x]}")


        repeatNums.clear()                
        print()

def inABCOrder():
    inOrder = list()
    for x in range(len(lines)):
        inOrder.append(lines[x])
    inOrder.sort()
    for x in range(len(lines)):
        print(inOrder[x], end = "")

weapon.close()
