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

        if command == "north":
            return "north"
        elif command == "east":
            return "east"
        elif command == "south":
            return "south"
        elif command == "west":
            return "west"
        elif command == "open backpack":
            inventory.backpack()
        elif command == "use knife":
            if inventory.holdingCurrentItem == "knife":
                if currentLocation == "Bear":
                    print(
                        colored("The bear looks scared! Why would you hurt it?", "red"))
                else:
                    print(colored("You can not use the knife here.", "red"))
                globalmethods.continueKey()
        elif command == "use berries" or command == "give berries" or command == "feed berries":
            if inventory.holdingCurrentItem == "berries":
                if currentLocation == "Bear":
                    print(
                        colored("The bear ate your berries and is very happy now!", "green"))
                    globalmethods.bearFed = True
                else:
                    print(colored("You can not use the berries here.", "red"))
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
        elif command == "use wood" or "place wood":
            if inventory.holdingCurrentItem == "wood":
                if currentLocation == "Inside Cave":
                    print(colored("The wood has been placed on the floor.", "green"))
                    globalmethods.woodPlaced = True
                else:
                    print(colored("You can not use or place the wood here.", "red"))
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
        elif command == "use survival book" or command == "place survival book" or command == "use ripped survival book" or command == "place ripped survival book":
            if inventory.holdingCurrentItem == "survival book":
                if globalmethods.rippedSurvivalBook == True:
                    if globalmethods.woodPlaced == True:
                        print(
                            colored("The survival book has been placed on the log.", "green"))
                        globalmethods.survivalBookOnLog = True
                else:
                    print(colored("The survival book has not been ripped "))
