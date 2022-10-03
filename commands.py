import inventory
import globalmethods
import os
from colorama import init
from termcolor import colored


def commands(currentLocation, currentLocationText):
    while True:
        os.system('cls')
        print(
            colored(f"Holding current item: {inventory.holdingCurrentItem}", "red"))
        print(colored(f"Location: {currentLocation}", "green"))
        print(colored(currentLocationText, "yellow"))

        command = input("> ").lower().strip()

        # navigation returns
        if command == "north":
            return "north"
        elif command == "east":
            return "east"
        elif command == "south":
            return "south"
        elif command == "west":
            return "west"

        # locations returns
        elif command == "enter cave":
            return "enter cave"

        elif command == "exit cave":
            return "exit cave"

        elif command == "leave cave":
            return "leave cave"

        elif command == "enter shack":
            return "enter shack"

        elif command == "enter storage room":
            return "enter storage room"

        elif command == "leave shack":
            return "leave shack"

        elif command == "exit shack":
            return "exit shack"

        elif command == "leave storage room":
            return "leave storage room"

        elif command == "exit storage room":
            return "exit storage room"

        elif command == "open backpack" or command == "enter backpack" or command == "backpack":
            inventory.backpack()

        elif command == "use knife" or command == "hit bear" or command == "kill bear" or command == "stab bear":
            if inventory.holdingCurrentItem == "Knife":
                if currentLocation == "At the Bear":
                    print(
                        colored("The bear looks scared! Why would you hurt it? Do you even like bear meat?!", "red"))
                else:
                    print(colored("You can not use the knife here.", "red"))
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
            globalmethods.continueKey()

        elif command == "get berries" or command == "take berries":
            if currentLocation == "At the Berries":
                if globalmethods.hasBerries == False and globalmethods.bearFed == False:
                    print(
                        colored("You have taken the berries and put them in your backpack.", "green"))
                    globalmethods.hasBerries = True
                else:
                    print(colored("You already took the berries!", "red"))
                globalmethods.continueKey()
            else:
                print(colored("There are no berries here!", "red"))
                globalmethods.continueKey()

        elif command == "use berries" or command == "give berries" or command == "feed berries" or command == "feed bear" or command == "give food":
            if inventory.holdingCurrentItem == "Berries":
                if currentLocation == "At the Bear":
                    print(
                        colored("The bear ate your berries and is very happy now!", "green"))
                    globalmethods.bearFed = True
                    globalmethods.hasBerries = False
                    inventory.holdingCurrentItem = "Nothing"
                else:
                    print(colored("You can not use the berries here.", "red"))
                globalmethods.continueKey()
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
                globalmethods.continueKey()
            else:
                print(colored("You have no berries in your hand!", "red"))
                globalmethods.continueKey()

        elif command == "cut wood" or command == "chop wood" or command == "chop tree" or command == "cut tree":
            if inventory.holdingCurrentItem == "Mini axe":
                if currentLocation == "Tree":
                    if globalmethods.treeChopped == False:
                        print(colored(
                            "You have chopped the tree and took the wood in your backpack!", "green"))
                        globalmethods.hasWood = True
                        globalmethods.treeChopped = True
                    else:
                        print(colored(
                            "You have already chopped the tree and have enough wood already!", "red"))
                else:
                    print(colored("You can not use the mini axe here.", "red"))
                globalmethods.continueKey()
            elif inventory.holdingCurrentItem == "Nothing":
                print(colored(
                    "AH! That hurt, you should know that you can not chop wood with your hand!", "red"))
                globalmethods.continueKey()
            elif inventory.holdingCurrentItem != "Nothing" and inventory.holdingCurrentItem != "Mini axe":
                print(colored(
                    "You can not chop the tree with this item!", "red"))
                globalmethods.continueKey()

        elif command == "use wood" or command == "place wood":
            if globalmethods.hasWood == True:
                if inventory.holdingCurrentItem == "Wood":
                    if currentLocation == "Inside Cave":
                        print(
                            colored("The wood has been placed on the floor.", "green"))
                        globalmethods.woodPlaced = True
                        globalmethods.hasWood = False
                    else:
                        print(
                            colored("Maybe it is better to place it somewhere more safe.", "red"))
                    globalmethods.continueKey()
                elif inventory.holdingCurrentItem == "Nothing":
                    globalmethods.emptyHand()
                    globalmethods.continueKey()
                elif inventory.holdingCurrentItem != "Nothing" and inventory.holdingCurrentItem != "Wood":
                    print(
                        colored("You must first take out the wood from your backpack!", "red"))

        # elif command == "place survival book" or command == "use ripped survival book" or command == "place ripped survival book":
        #     if inventory.holdingCurrentItem == "survival book":
        #         if globalmethods.rippedSurvivalBook == True:
        #             if globalmethods.woodPlaced == True:
        #                 print(
        #                     colored("The survival book has been placed on the wood.", "green"))
        #                 globalmethods.survivalBookOnWood = True
        #             else:
        #                 print(colored(
        #                     "Maybe you should first place wood where you can start the fire on.", "red"))
        #         else:
        #             print(colored(
        #                 "Maybe you should first rip the survival book to place it on the log to start a fire.", "red"))
        #     elif inventory.holdingCurrentItem == "Nothing":
        #         globalmethods.emptyHand()

        # elif command == "use matches" or command == "start matches" or command == "fire matches":
            # if inventory.holdingCurrentItem == "matches":
            # if globalmethods.
