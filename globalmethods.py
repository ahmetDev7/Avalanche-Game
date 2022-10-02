from colorama import init
from termcolor import colored

# Attainable Items
hasBerries = False
hasWood = False
hasFishingRod = False
hasJacket = False
hasBoots = False

# Conditions for cooking food & water
woodPlaced = False
rippedSurvivalBook = False
survivalBookOnLog = False
matchesUsed = False
steelPanHasWater = False
steelPanPlaced = False
hasFish = False

# Achievement
bearFed = False


def continueKey():
    input("Press a key to continue..")


def emptyHand():
    print(colored("You have nothing in your hand.", "red"))
