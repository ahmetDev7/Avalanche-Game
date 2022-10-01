currentLocation = None


def startpoint():
    print("You are standing in front of the mountain at the place you woke up.")
    global currentLocation
    currentLocation = "startpoint"


def outsideCave():
    print("You are standing in front of a cave, whill you enter it?")
    global currentLocation
    currentLocation = "outsideCave"


def insideCave():
    print("You are inside the cave, it seems that it is safe here and there is no wind.")
    global currentLocation
    currentLocation = "insideCave"


def tree():
    print("You are standing in front a tree, there is a log next to it")
    global currentLocation
    currentLocation = "tree"


def outsideShack():
    print("You are standing outside of a shack, it seems like it is abandoned..")
    global currentLocation
    currentLocation = "outsideShack"


def insideShack():
    print("You are inside the abandoned shack, in the back there is a storage room.")
    global currentLocation
    currentLocation = "insideShack"


def storageRoom():
    print("You are inside the storage room of the abandoned shack.")
    global currentLocation
    currentLocation = "storageRoom"


def berries():
    print("You are in front of a bush with berries, they seem delicious.")
    global currentLocation
    currentLocation = "berries"


def bear():
    print("Woah! A wild bear, but it seems that it is hungry and not harmful.")
    global currentLocation
    currentLocation = "bear"
