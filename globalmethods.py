from colorama import init
from termcolor import colored

# Map data
treeChopped = True

# Attainable Items
hasBerries = False
hasWood = True
hasFishingRod = False
hasJacket = False
hasBoots = False

# Conditions for cooking food & water
woodPlaced = True
rippedSurvivalBook = False
survivalBookOnWood = False
matchesUsed = False
steelPanHasWater = False
steelPanPlaced = False
fishPlaced = False

# Achievement
bearFed = False


def continueKey():
    input("Press a key to continue..")


def emptyHand():
    print(colored("You have nothing in your hand.", "red"))
