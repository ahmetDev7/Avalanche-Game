from colorama import init
from termcolor import colored

# Map data
treeChopped = False

# Attainable Items
hasBerries = False
hasWood = False
hasFishingRod = False
hasJacket = False
hasBoots = False
hasFish = False

# Conditions for cooking food & water
woodPlaced = False
rippedSurvivalBook = False
survivalBookOnWood = False
matchesUsed = False
steelPanHasWater = False
steelPanPlaced = False
fishPlaced = False

# Achievement
bearFed = False

# Ending variables
eatFish = False
drinkWater = False


def continueKey():
    input("Press a key to continue..")


def emptyHand():
    print(colored("You have nothing in your hand.", "red"))
