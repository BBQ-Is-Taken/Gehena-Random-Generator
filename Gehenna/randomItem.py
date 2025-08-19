import random

items = open("Items.txt")
lines = items.readlines()
repeatNums = set()
randNum = 0

def getItems(num):
    selectedItem = lines[num].strip()
    return selectedItem

def newRandomNumber():
    num = random.randint(0, len(lines)-1)
    return num

def makeItemList(numItems): #Returns a list of the random items- rewritten for easier future use!
    randNum = newRandomNumber()
    x = 0
    saverList = list()
    
    if not numItems.isdigit(): # If statements to get valid input
        print("Must be a number!")
    elif int(numItems) > len(lines):
        print(f"Too long! Max of {len(lines)}!")
    elif int(numItems) <= 0:
        print("Must be over 0!")
    else:
        while x < int(numItems):
            if randNum in repeatNums:
                randNum = newRandomNumber()
            else:
                repeatNums.add(randNum)
                saverList.append(getItems(randNum))
                randNum = newRandomNumber()
                x += 1
    return saverList



# START OF LOOP
# All this does is makes the list with the number of characters and prints it

def printItems(): #UNUSED
    quit = True

    while quit:
        nc = input("How many items: ")
        print()

        if nc == "q":
            break
        else:
            itemsList = makeItemList(nc)

            for x in range(len(itemsList)):
                print(f"{x+1} : {itemsList[x]}")


        repeatNums.clear()                
        print()

def inABCOrder(): #UNUSED
    inOrder = list()
    for x in range(len(lines)):
        inOrder.append(lines[x])
    inOrder.sort()
    for x in range(len(lines)):
        print(inOrder[x], end = "")


items.close()
