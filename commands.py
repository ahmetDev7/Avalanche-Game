import inventory
import survivalbook
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

        elif command == "open survival book" or command == "open survivalbook" or command == "read survival book" or command == "read survivalbook" or command == "open book" or command == "read book":
            if globalmethods.rippedSurvivalBook == True:
                print(colored(
                    "You have ripped the Survival Book, you can no longer open it!", "red"))
                globalmethods.continueKey()
            else:
                if inventory.holdingCurrentItem == "Survival Book":
                    survivalbook.OpenSurvivalBook()
                elif inventory.holdingCurrentItem == "Nothing":
                    globalmethods.emptyHand()
                    globalmethods.continueKey()

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
                    return 0
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
                    return 0
                else:
                    print(colored("You can not use the berries here.", "red"))
                    globalmethods.continueKey()
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
                globalmethods.continueKey()
            else:
                print(colored("You have no berries in your hand!", "red"))
                globalmethods.continueKey()

        elif command == "cut wood" or command == "chop wood" or command == "chop tree" or command == "cut tree" or command == "use axe" or command == "use mini axe":
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

        elif command == "take fishing rod":
            if currentLocation == "Inside the Storage Room":
                if globalmethods.hasFishingRod == False:
                    print(colored(
                        "You have collected the fishing rod and put it in your backpack!", "green"))
                    globalmethods.hasFishingRod = True
                    return 0
                else:
                    print(colored("You have already collected the fishing rod!", "red"))
                    globalmethods.continueKey()

        elif command == "take jacket":
            if currentLocation == "Inside the Storage Room":
                if globalmethods.hasJacket == False:
                    print(colored(
                        "There is no space in your backpack for the jacket! Try putting it on.", "red"))
                else:
                    print(colored("You have already collected the jacket!", "red"))
                globalmethods.continueKey()

        elif command == "put jacket on" or command == "put the jacket on" or command == "put on jacket":
            if currentLocation == "Inside the Storage Room":
                if globalmethods.hasJacket == False:
                    print(colored(
                        "You have put the jacket on! Feels warm doesn't it?", "green"))
                    globalmethods.hasJacket = True
                    return 0
                else:
                    print(colored("You have already put your jacket on!", "red"))
                    globalmethods.continueKey()

        elif command == "take boots":
            if currentLocation == "Inside the Storage Room":
                if globalmethods.hasBoots == False:
                    print(colored(
                        "There is no space in your backpack for the boots! Try putting it on.", "red"))
                else:
                    print(colored("You have already collected the boots!", "red"))
                globalmethods.continueKey()

        elif command == "put boots on" or command == "put the boots on" or command == "put on boots":
            if currentLocation == "Inside the Storage Room":
                if globalmethods.hasBoots == False:
                    print(colored(
                        "You have put the boots on! Feels way better!", "green"))
                    globalmethods.hasBoots = True
                    return 0
                else:
                    print(colored("You have already put your boots on!", "red"))
                    globalmethods.continueKey()

        elif command == "use wood" or command == "place wood" or command == "set wood" or command == "put wood":
            if globalmethods.hasWood == True:
                if inventory.holdingCurrentItem == "Wood":
                    if currentLocation == "Inside the Cave":
                        print(
                            colored("The wood has been placed on the floor.", "green"))
                        globalmethods.woodPlaced = True
                        globalmethods.hasWood = False
                        inventory.holdingCurrentItem = "Nothing"
                        return 0
                    else:
                        print(
                            colored("Maybe it is better to place it somewhere more safe.", "red"))
                elif inventory.holdingCurrentItem == "Nothing":
                    globalmethods.emptyHand()
                elif inventory.holdingCurrentItem != "Nothing" and inventory.holdingCurrentItem != "Wood":
                    print(
                        colored("You must first take out the wood from your backpack!", "red"))
                globalmethods.continueKey()

        elif command == "rip survival book" or command == "rip book" or command == "rip the book" or command == "rip the survival book":
            if inventory.holdingCurrentItem == "Survival Book":
                globalmethods.rippedSurvivalBook = True
                print(
                    colored("The survival book has been ripped in pieces.", "green"))
                inventory.holdingCurrentItem = "Ripped Survival Book"
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
            elif inventory.holdingCurrentItem != "Nothing" and inventory.holdingCurrentItem != "Survival Book":
                print(
                    colored("You must first take out the survival book from your backpack!", "red"))
            globalmethods.continueKey()

        elif command == "place survival book" or command == "place book" or command == "place book on wood" or command == "place survival book on wood":
            if currentLocation == "Inside the Cave" and globalmethods.rippedSurvivalBook == False:
                print(colored(
                    "WOW! Easy there, you should first rip it into pieces.", "red"))
                globalmethods.continueKey()

        elif command == "use ripped survival book" or command == "place paper" or command == "place ripped survival book" or command == "place ripped survival book on fire":
            if inventory.holdingCurrentItem == "Ripped Survival Book":
                if globalmethods.rippedSurvivalBook == True:
                    if globalmethods.woodPlaced == True:
                        print(
                            colored("The ripped survival book has been placed on the wood.", "green"))
                        globalmethods.survivalBookOnWood = True
                        inventory.holdingCurrentItem = "Nothing"
                        return 0
                    else:
                        print(colored(
                            "Maybe you should first place wood where you can put the paper on.", "red"))
                else:
                    print(colored(
                        "Maybe you should first rip the survival book to place it on the log to start a fire.", "red"))
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
            elif inventory.holdingCurrentItem != "Nothing" and inventory.holdingCurrentItem != "Ripped Survival Book":
                print(
                    colored("You must first take out the ripped survival book from your backpack!", "red"))
            globalmethods.continueKey()

        elif command == "use matches" or command == "start matches" or command == "fire matches":
            if inventory.holdingCurrentItem == "Matches":
                if globalmethods.woodPlaced == True and globalmethods.survivalBookOnWood == True:
                    print(
                        colored("The matches have been fired! Woah, the paper is starting to burn!", "green"))
                    globalmethods.matchesUsed = True
                    inventory.holdingCurrentItem = "Nothing"
                    return 0
                else:
                    print(colored(
                        "You should use your matches later.", "red"))
                globalmethods.continueKey()
            elif inventory.holdingCurrentItem == "Nothing":
                globalmethods.emptyHand()
                globalmethods.continueKey()
            elif inventory.holdingCurrentItem != "Nothing" and inventory.holdingCurrentItem != "Matches":
                print(
                    colored("You must first take out the matches from your backpack!", "red"))
            globalmethods.continueKey()

        elif command == "use steelpan" or command == "place steelpan" or command == "use mini steelpan" or command == "place mini steelpan" or command == "use pan" or command == "place pan":
            if inventory.holdingCurrentItem == "Mini steelpan" or inventory.holdingCurrentItem == "Mini steelpan (with water)":
                if currentLocation == "Inside the Cave" and globalmethods.woodPlaced == True and globalmethods.survivalBookOnWood == True and globalmethods.matchesUsed == True:
                    if globalmethods.steelPanHasWater == False:
                        print(
                            colored("There is nothing in the pan, what you do want to boil?! Air?!", "red"))
                    else:
                        print(
                            colored("The water is boiling.. and ready! You can now consume the water, it is safe to drink. Drink it slowly!.", "green"))
                        globalmethods.steelPanPlaced = True
                        return 0
                elif currentLocation == "River":
                    if globalmethods.steelPanHasWater == False:
                        print(
                            colored("You have collected water in your steelpan!", "green"))
                        globalmethods.steelPanHasWater = True
                        inventory.holdingCurrentItem = "Mini steelpan (with water)"
                        return 0
                    else:
                        print(
                            colored("You have already collected water in your steelpan!", "red"))
                else:
                    print(colored(
                        "You should use your pan later or somewhere else.", "red"))
                globalmethods.continueKey()
