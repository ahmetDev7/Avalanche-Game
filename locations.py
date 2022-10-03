from commands import *
from globalmethods import continueKey
from imgrender import render
currentLocation = None

def renderimage(img):
    image = render(img, scale = (20, 20))


def Startpoint():
    global currentLocation
    currentLocation = "Startpoint"
    currentLocationText = "You are standing in front of the mountain at the place you woke up."
    renderimage("avalanche\images\startpoint.jpg")
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
    currentLocationText = "You are standing in front of a river, it's flowing.."
    renderimage("avalanche\images\wriver2.jpg")
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east":
        OutsideCave()
    elif cmd == "west":
        Berries()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        River()


def OutsideCave():
    global currentLocation
    currentLocation = "Outside the Cave"
    currentLocationText = "You are standing in front of a cave, will you enter it?"
    renderimage("avalanche\images\cave.jpg")
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north" or cmd == "enter cave":
        InsideCave()
    elif cmd == "west":
        River()
    elif cmd == "east":
        Tree()
    else:
        print("You can not go there!")
        OutsideCave()
        globalmethods.continueKey()
        OutsideCave()


def InsideCave():
    global currentLocation
    currentLocation = "Inside the Cave"
    currentLocationText = "You are inside the cave, it seems that it is safe here and there is no wind."
    renderimage("avalanche\images\insidecave.jpg")
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "south" or cmd == "exit cave" or cmd == "leave cave":
        OutsideCave()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        InsideCave()


def Tree():
    global currentLocation
    currentLocation = "Tree"
    currentLocationText = "You are standing in front of a tree, it has a nice colour and looks good in shape."
    renderimage("avalanche\images\wtree.jpg")
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
    renderimage("avalanche\images\outsideshack.jpg")
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
    renderimage("avalanche\images\insideshack.jpg")
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
    currentLocationText = "You are inside the storage room of the abandoned shack."
    renderimage("avalanche\images\storageroom.jpg")
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "west" or cmd == "leave storage room" or cmd == "exit storage room":
        InsideShack()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        StorageRoom()


def Berries():
    global currentLocation
    currentLocation = "At the Berries"
    renderimage("avalanche\images\wbush.jpg")
    if globalmethods.hasBerries == True or globalmethods.bearFed == True:
        currentLocationText = "You are in front of the bush that had the berries, it seems that there are none left."
    else:
        currentLocationText = "You are in front of a bush with berries, they seem delicious."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "south":
        Bear()
    elif cmd == "east":
        River()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        Berries()


def Bear():
    global currentLocation
    currentLocation = "At the Bear"
    currentLocationText = "Woah! A wild bear, but it seems that it is hungry and not harmful."
    renderimage("avalanche\images\wbear.jpg")
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north":
        Berries()
    else:
        print("You can not go there!")
        globalmethods.continueKey()
        Bear()

# hal
