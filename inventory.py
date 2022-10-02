from colorama import init
from termcolor import colored
import os
from globalmethods import continueKey

holdingCurrentItem = "Nothing"
isBackpackOpen = False


def backpack():
    global holdingCurrentItem

    isBackpackOpen = True
    while isBackpackOpen == True:
        os.system('cls')
        print(colored("---------------------------", "blue"))
        print(colored("Items in backpack:", "green"))
        print(colored(
            "\n- Knife\n- Survival Book\n- Mini axe\n- Mini steelpan\n- Matches", "green"))
        print(colored("---------------------------", "blue"))
        backpackinput = input("> ")
        if backpackinput == "close backpack" or backpackinput == "exit backpack":
            isBackpackOpen = False
            return holdingCurrentItem
        elif backpackinput == "take knife":
            print(colored("You are now holding your knife in your hand.", "green"))
            holdingCurrentItem = "knife"
            continueKey()
        elif backpackinput == "take survival book":
            print(colored("You are now holding your surival book in your hand.", "green"))
            holdingCurrentItem = "Survival Book"
            continueKey()
        elif backpackinput == "take mini axe":
            print(colored("You are now holding your mini axe in your hand.", "green"))
            holdingCurrentItem = "Mini axe"
            continueKey()
        elif backpackinput == "take mini steelpan":
            print(colored("You are now holding your mini steelpan in your hand.", "green"))
            holdingCurrentItem = "Mini steelpan"
            continueKey()
        elif backpackinput == "take matches":
            print(colored("You are now holding your matches in your hand.", "green"))
            holdingCurrentItem = "Matches"
            continueKey()
        else:
            print("wrong")
