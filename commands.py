import inventory
import globalmethods
import os
from colorama import init
from termcolor import colored


def commands(currentLocation):
    while True:
        os.system('cls')
        print(colored(f"You are now at: {currentLocation}", "green"))
        command = input("> ").lower().strip()

        if command == "north":
            return "north"
        elif command == "east":
            return "east"
        elif command == "south":
            return "south"
        elif command == "west":
            return "west"

        if command == "open backpack":
            inventory.backpack()
        elif command == "use knife":
            if inventory.holdingCurrentItem == "knife":
                print(colored("You can not use that here!", "red"))
                globalmethods.continueKey()
