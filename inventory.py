from colorama import init
from termcolor import colored
import os
import globalmethods

holdingCurrentItem = "Nothing"
isBackpackOpen = False


def backpack():
    global holdingCurrentItem

    isBackpackOpen = True
    while isBackpackOpen == True:
        os.system('cls')
        print(colored("---------------------------", "blue"))
        print(colored("Items in backpack:", "green"))
        print(colored("\n- Knife", "green"))
        print(colored("- Survival Book", "green"))
        print(colored("- Mini axe", "green"))
        print(colored("- Mini steelpan", "green"))
        print(colored("- Matches", "green"))
        if globalmethods.hasBerries == True:
            print(colored("- Berries", "green"))
        if globalmethods.hasWood == True:
            print(colored("- Wood", "green"))
        print(colored("---------------------------", "blue"))
        backpackinput = input("> ")
        if backpackinput == "close backpack" or backpackinput == "exit backpack" or backpackinput == "exit" or backpackinput == "leave backpack":
            isBackpackOpen = False
            return holdingCurrentItem
        elif backpackinput == "take knife":
            print(colored("You are now holding your knife in your hand.", "green"))
            holdingCurrentItem = "Knife"
            globalmethods.continueKey()
        elif backpackinput == "take survival book":
            print(colored("You are now holding your surival book in your hand.", "green"))
            holdingCurrentItem = "Survival Book"
            globalmethods.continueKey()
        elif backpackinput == "take mini axe":
            print(colored("You are now holding your mini axe in your hand.", "green"))
            holdingCurrentItem = "Mini axe"
            globalmethods.continueKey()
        elif backpackinput == "take mini steelpan":
            print(
                colored("You are now holding your mini steelpan in your hand.", "green"))
            holdingCurrentItem = "Mini steelpan"
            globalmethods.continueKey()
        elif backpackinput == "take matches":
            print(colored("You are now holding your matches in your hand.", "green"))
            holdingCurrentItem = "Matches"
            globalmethods.continueKey()
        elif backpackinput == "take berries":
            print(colored("You are now holding your berries in your hand.", "green"))
            holdingCurrentItem = "Berries"
            globalmethods.continueKey()
