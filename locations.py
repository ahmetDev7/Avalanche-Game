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
        print("You can not go there!")
    continueKey()


def River():
    global currentLocation
    currentLocation = "River"
    currentLocationText = "You are standing in front of a river, it's flowing.."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east":
        OutsideCave()
    elif cmd == "west":
        Berries()
    else:
        print("You can not go there!")
    continueKey()


def OutsideCave():
    global currentLocation
    currentLocation = "Outside the Cave"
    currentLocationText = "You are standing in front of a cave, will you enter it?"
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north" or "enter cave":
        InsideCave()
    elif cmd == "west":
        River()
    elif cmd == "east":
        Tree()
    else:
        print("You can not go there!")
        OutsideCave()
    continueKey()


def InsideCave():
    global currentLocation
    currentLocation = "Inside the Cave"
    currentLocationText = "You are inside the cave, it seems that it is safe here and there is no wind."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "south" or "exit cave" or "leave cave":
        OutsideCave()
    else:
        print("You can not go there!")
    continueKey()



def Tree():
    global currentLocation
    currentLocation = "Tree"
    currentLocationText = "You are standing in front of a tree, there is a log next to it."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "west":
        OutsideCave()
    elif cmd == "south":
        OutsideShack()
    else:
        print("You can not go there!")
    continueKey()


def OutsideShack():
    global currentLocation
    currentLocation = "Outside the Shack"
    currentLocationText = "You are standing outside of a shack, it seems like it is abandoned.."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east" or "enter shack":
        InsideShack()
    elif cmd == "north":
        Tree()
    else:
        print("You can not go there!")
    continueKey()


def InsideShack():
    global currentLocation
    currentLocation = "Inside the Shack"
    currentLocationText = "You are inside the abandoned shack, in the back there is a storage room."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "east" or "enter storage room":
        StorageRoom()
    elif cmd == "west" or "leave shack" or "exit shack":
        OutsideShack()
    else:
        print("You can not go there!")
    continueKey()


def StorageRoom():
    global currentLocation
    currentLocation = "Inside the Storage Room"
    currentLocationText = "You are inside the storage room of the abandoned shack."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "west" or "leave storage room" or "exit storage room":
        InsideShack()
    else:
        print("You can not go there!")
    continueKey()



def Berries():
    global currentLocation
    currentLocation = "At the Berries"
    currentLocationText = "You are in front of a bush with berries, they seem delicious."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "south":
        Bear()
    elif cmd == "east":
        River()
    else:
        print("You can not go there!")
    continueKey()


def Bear():
    global currentLocation
    currentLocation = "At the Bear"
    currentLocationText = "Woah! A wild bear, but it seems that it is hungry and not harmful."
    cmd = commands(currentLocation, currentLocationText)
    if cmd == "north":
        Berries()
    else:
        print("You can not go there!")
    continueKey()

#hal