import random

location = open("Locations.txt")
lines = location.readlines()
repeatNums = set()
randNum = 0

def getLocation(num):
    selectedLocation = lines[num].strip()
    return selectedLocation

def newRandomNumber():
    num = random.randint(0, len(lines)-1)
    return num

def makeLocationList(numLocations): #Returns a list of the random locations- rewritten for easier future use!
    randNum = newRandomNumber()
    x = 0
    saverList = list()
    
    if not numLocations.isdigit(): # If statements to get valid input
        print("Must be a number!")
    elif int(numLocations) > len(lines):
        print(f"Too long! Max of {len(lines)}!")
    elif int(numLocations) <= 0:
        print("Must be over 0!")
    else:
        while x < int(numLocations):
            if randNum in repeatNums:
                randNum = newRandomNumber()
            else:
                repeatNums.add(randNum)
                saverList.append(getLocation(randNum))
                randNum = newRandomNumber()
                x += 1
    return saverList



# START OF LOOP
def printLocations():
    quit = True

    while quit:
        nc = input("How many locations: ")
        print()

        if nc == "q":
            break
        else:
            locationList = makeLocationList(nc)

            for x in range(len(locationList)):
                print(f"{x+1} : {locationList[x]}")


        repeatNums.clear()                
        print()



location.close()
