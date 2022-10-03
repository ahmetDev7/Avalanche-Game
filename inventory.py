from turtle import back
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
        if globalmethods.rippedSurvivalBook == False:
            print(colored("- Survival Book", "green"))
        else:
            print(colored("- Ripped Survival Book", "green"))
        print(colored("- Mini axe", "green"))
        if globalmethods.steelPanHasWater == False:
            print(colored("- Mini steelpan", "green"))
        else:
            print(colored("- Mini steelpan (with water)", "green"))
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
        elif backpackinput == "take survival book" or backpackinput == "take book":
            print(colored("You are now holding your surival book in your hand.", "green"))
            holdingCurrentItem = "Survival Book"
            globalmethods.continueKey()
        elif backpackinput == "take mini axe":
            print(colored("You are now holding your mini axe in your hand.", "green"))
            holdingCurrentItem = "Mini axe"
            globalmethods.continueKey()
        elif backpackinput == "take mini steelpan" or backpackinput == "take steelpan" or backpackinput == "take pan":
            if globalmethods.steelPanHasWater == False:
                print(
                    colored("You are now holding your mini steelpan in your hand.", "green"))
                holdingCurrentItem = "Mini steelpan"
            else:
                print(
                    colored("You are now holding your mini steelpan (with water) in your hand.", "green"))
                holdingCurrentItem = "Mini steelpan (with water)"
            globalmethods.continueKey()
        elif backpackinput == "take matches":
            print(colored("You are now holding your matches in your hand.", "green"))
            holdingCurrentItem = "Matches"
            globalmethods.continueKey()
        elif backpackinput == "take berries":
            print(colored("You are now holding your berries in your hand.", "green"))
            holdingCurrentItem = "Berries"
            globalmethods.continueKey()
        elif backpackinput == "take wood":
            if globalmethods.hasWood == True:
                print(colored("You are now holding your wood in your hand.", "green"))
                holdingCurrentItem = "Wood"
                globalmethods.continueKey()
        elif backpackinput == "take ripped survival book":
            if globalmethods.rippedSurvivalBook == True:
                print(colored(
                    "You are now holding the ripped survival book pieces in your hand.", "green"))
                holdingCurrentItem = "Ripped Survival Book"
                globalmethods.continueKey()
