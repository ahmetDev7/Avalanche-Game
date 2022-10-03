from commands import *
from globalmethods import continueKey
import climage
currentLocation = None


def Startpoint():
    global currentLocation
    currentLocation = "Startpoint"
    currentLocationText = "You are standing in front of the mountain at the place you woke up."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north":
        OutsideCave()
    else:
        print(colored("You can not go there!", "red"))
        globalmethods.continueKey()
        Startpoint()


def River():
    global currentLocation
    currentLocation = "River"
    currentLocationText = "You are standing in front of a river, it's flowing.. Looks like that there is some fish swimming in the water."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east":
        OutsideCave()
    elif cmd == "west":
        Berries()
    elif cmd == 0:
        globalmethods.continueKey()
        River()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        River()


def OutsideCave():
    global currentLocation
    currentLocation = "Outside the Cave"
    currentLocationText = "You are standing in front of a cave, will you enter it?"
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north" or cmd == "enter cave":
        InsideCave()
    elif cmd == "west":
        River()
    elif cmd == "east":
        Tree()
    elif cmd == "south":
        Startpoint()
    else:
        print("You can not go there!")
        OutsideCave()
        globalmethods.continueKey()
        OutsideCave()


def InsideCave():
    global currentLocation
    currentLocation = "Inside the Cave"

    if globalmethods.woodPlaced == True:
        currentLocationText = "You are inside the cave, and your wood has been placed. But it needs something flamable like paper on top of it to start a fire."
        if globalmethods.survivalBookOnWood == True:
            currentLocationText = "You are inside the cave, and your wood and paper have been placed. It looks like it is ready to be fired up!"
            if globalmethods.matchesUsed == True:
                currentLocationText = "You are inside the cave, your fire is burning nicely. Time for some cooking!"
                if globalmethods.steelPanPlaced == True and globalmethods.fishPlaced == False:
                    currentLocationText = "You are inside the cave, your water is ready to consume! The fire is still burning."
                elif globalmethods.fishPlaced == True and globalmethods.steelPanPlaced == False:
                    currentLocationText = "You are inside the cave, your fish is cooking is ready to consume! The fire is still burning."
                elif globalmethods.steelPanPlaced == True and globalmethods.fishPlaced == True:
                    currentLocationText = "You are inside the cave, your fish and water are ready to consume! The fire is still burning."
    else:
        currentLocationText = "You are inside the cave, it seems that it is safe here and there is no wind."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "south" or cmd == "exit cave" or cmd == "leave cave":
        OutsideCave()
    elif cmd == 0:
        globalmethods.continueKey()
        InsideCave()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        InsideCave()


def Tree():
    global currentLocation
    currentLocation = "Tree"
    currentLocationText = "You are standing in front of a tree, it has a nice colour and looks good in shape."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "west":
        OutsideCave()
    elif cmd == "south":
        OutsideShack()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        Tree()


def OutsideShack():
    global currentLocation
    currentLocation = "Outside the Shack"
    currentLocationText = "You are standing outside of a shack, it seems like it is abandoned.."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east" or cmd == "enter shack":
        InsideShack()
    elif cmd == "north":
        Tree()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        OutsideShack()


def InsideShack():
    global currentLocation
    currentLocation = "Inside the Shack"
    currentLocationText = "You are inside the abandoned shack, in the back there is a storage room."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east" or cmd == "enter storage room":
        StorageRoom()
    elif cmd == "west" or cmd == "leave shack" or cmd == "exit shack":
        OutsideShack()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        InsideShack()


def StorageRoom():
    global currentLocation
    currentLocation = "Inside the Storage Room"

    if globalmethods.hasJacket == True and globalmethods.hasBoots == False and globalmethods.hasFishingRod == False:
        currentLocationText = "You are inside the storage room of the abandoned shack. There are boots and a fishing rod."
    elif globalmethods.hasJacket == True and globalmethods.hasBoots == True and globalmethods.hasFishingRod == False:
        currentLocationText = "You are inside the storage room of the abandoned shack. There is a fishing rod."
    elif globalmethods.hasJacket == True and globalmethods.hasBoots == False and globalmethods.hasFishingRod == True:
        currentLocationText = "You are inside the storage room of the abandoned shack. There are boots."
    elif globalmethods.hasJacket == False and globalmethods.hasBoots == True and globalmethods.hasFishingRod == False:
        currentLocationText = "You are inside the storage room of the abandoned shack. There is a jacket on the wall and under it is a fishing rod."
    elif globalmethods.hasJacket == False and globalmethods.hasBoots == False and globalmethods.hasFishingRod == True:
        currentLocationText = "You are inside the storage room of the abandoned shack. There is a jacket on the wall and under it are boots."
    elif globalmethods.hasJacket == True and globalmethods.hasBoots == True and globalmethods.hasFishingRod == True:
        currentLocationText = "You are inside the storage room of the abandoned shack. Seems like there is nothing left."
    else:
        currentLocationText = "You are inside the storage room of the abandoned shack. There is a jacket on the wall and under it are boots and a fishing rod."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "west" or cmd == "leave storage room" or cmd == "exit storage room":
        InsideShack()
    elif cmd == 0:
        globalmethods.continueKey()
        StorageRoom()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        StorageRoom()


def Berries():
    global currentLocation
    currentLocation = "At the Berries"
    if globalmethods.hasBerries == True or globalmethods.bearFed == True:
        currentLocationText = "You are in front of the bush that had the berries, it seems that there are none left."
    else:
        currentLocationText = "You are in front of a bush with berries, they seem delicious."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "south":
        Bear()
    elif cmd == "east":
        River()
    elif cmd == 0:
        globalmethods.continueKey()
        Berries()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        Berries()


def Bear():
    global currentLocation
    currentLocation = "At the Bear"
    if globalmethods.bearFed == False:
        currentLocationText = "Woah! A wild bear, but it seems that it is hungry and not harmful."
    else:
        currentLocationText = "The bear looks very happy. He seems friendly now."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north":
        Berries()
    elif cmd == 0:
        globalmethods.continueKey()
        Bear()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        Bear()
