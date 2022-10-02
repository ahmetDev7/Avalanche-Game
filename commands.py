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
                print(colored("You can not use that here!", "red"))
                globalmethods.continueKey()
