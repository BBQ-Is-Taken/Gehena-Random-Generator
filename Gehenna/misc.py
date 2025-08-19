import random

list = list()

def printList(list):
    counter = 0
    
    print()
    for x in list:
        counter += 1
        print(f"{counter} : {x}")
    print()
    
intensityLevels = {
    1 : "Cake Walk",
    2 : "Light Work",
    3 : "Little Sweat",
    4 : "Grounded",
    5 : "Mid!",
    6 : "Aight - Kinda Spicy",
    7 : "Bring it ON!",
    8 : "AYE AYE AYE, CALIENTE",
    9 : "Avengers Level Threat!",
    10: "BEYOND COOKED"
}
    
def randomIntensity():
    x = random.randint(1, len(intensityLevels))
    return intensityLevels[x]
