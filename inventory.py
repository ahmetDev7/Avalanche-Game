from colorama import init
from termcolor import colored
import os

holdingCurrentItem = ""
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
            input("Press a key to continue..")
        elif backpackinput == "take survival book":
            print("You are now holding your surival book in your hand.")
            holdingCurrentItem = "Survival Book"
        elif backpackinput == "take mini axe":
            print("You are now holding your mini axe in your hand.")
            holdingCurrentItem = "Mini axe"
        elif backpackinput == "take mini steelpan":
            print("You are now holding your mini steelpan in your hand.")
            holdingCurrentItem = "Mini steelpan"
        elif backpackinput == "take matches":
            print("You are now holding your matches in your hand.")
            holdingCurrentItem = "Matches"
        else:
            print("wrong")
