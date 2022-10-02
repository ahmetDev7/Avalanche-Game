from colorama import init
from termcolor import colored

# Attainable Items
# undone
hasBerries = False
# done
hasWood = False
# undone
hasFishingRod = False
# undone
hasJacket = False
# undone
hasBoots = False

# Conditions for cooking food & water
woodPlaced = False
rippedSurvivalBook = False
survivalBookOnWood = False
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
