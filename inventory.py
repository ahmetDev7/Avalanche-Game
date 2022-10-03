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
        print(colored("Items in backpack:\n", "green"))
        if holdingCurrentItem != "Knife":
            print(colored("- Knife", "green"))

        if globalmethods.rippedSurvivalBook == False:
            if holdingCurrentItem != "Survival Book":
                print(colored("- Survival Book", "green"))
        elif globalmethods.rippedSurvivalBook == True and globalmethods.survivalBookOnWood == False:
            if holdingCurrentItem != "Ripped Survival Book":
                print(colored("- Ripped Survival Book", "green"))
        if holdingCurrentItem != "Mini axe":
            print(colored("- Mini axe", "green"))
        if globalmethods.steelPanHasWater == False and globalmethods.steelPanPlaced == False:
            if holdingCurrentItem != "Mini steelpan":
                print(colored("- Mini steelpan", "green"))
        elif globalmethods.steelPanHasWater == True and globalmethods.steelPanPlaced == False:
            if holdingCurrentItem != "Mini steelpan (with water)":
                print(colored("- Mini steelpan (with water)", "green"))
        if globalmethods.matchesUsed == False:
            if holdingCurrentItem != "Matches":
                print(colored("- Matches", "green"))
        if globalmethods.hasBerries == True:
            if holdingCurrentItem != "Berries":
                print(colored("- Berries", "green"))
        if globalmethods.hasWood == True:
            if holdingCurrentItem != "Wood":
                print(colored("- Wood", "green"))
        if globalmethods.hasFishingRod == True:
            if holdingCurrentItem != "Fishing rod":
                print(colored("- Fishing rod", "green"))
        if globalmethods.hasFish == True:
            if holdingCurrentItem != "Fish":
                print(colored("- Fish", "green"))
        print(colored("---------------------------", "blue"))

        backpackinput = input("> ").lower()

        if backpackinput == "close backpack" or backpackinput == "exit backpack" or backpackinput == "exit" or backpackinput == "leave backpack":
            isBackpackOpen = False
            return holdingCurrentItem
        elif backpackinput == "take knife":
            print(colored("You are now holding your knife in your hand.", "green"))
            holdingCurrentItem = "Knife"
            globalmethods.continueKey()
        elif backpackinput == "take survival book" or backpackinput == "take book" or backpackinput == "take survivalbook":
            print(colored("You are now holding your surival book in your hand.", "green"))
            holdingCurrentItem = "Survival Book"
            globalmethods.continueKey()
        elif backpackinput == "take mini axe" or backpackinput == "take axe" or backpackinput == "take miniaxe":
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
        elif backpackinput == "take ripped survival book" or backpackinput == "take ripped book":
            if globalmethods.rippedSurvivalBook == True:
                print(colored(
                    "You are now holding the ripped survival book pieces in your hand.", "green"))
                holdingCurrentItem = "Ripped Survival Book"
                globalmethods.continueKey()
        elif backpackinput == "take fishing rod":
            if globalmethods.hasFishingRod == True:
                print(colored(
                    "You are now holding the fishing rod in your hand.", "green"))
                holdingCurrentItem = "Fishing rod"
                globalmethods.continueKey()
        elif backpackinput == "take fish":
            if globalmethods.hasFish == True:
                print(colored("You are now holding your fish in your hand.", "green"))
                holdingCurrentItem = "Fish"
                globalmethods.continueKey()
