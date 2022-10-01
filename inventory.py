holdingCurrentItem = ""
isBackpackOpen = False


def backpack():
    isBackpackOpen = True
    while isBackpackOpen == True:
        print("---------------------------")
        print("Items in backpack:")
        print("\n- Knife\n- Survival Book\n- Mini axe\n- Mini steelpan\n- Matches")
        print("---------------------------")
        backpackinput = input("Wat wil je pakken\n")
        if backpackinput == "close backpack" or backpackinput == "exit backpack":
            isBackpackOpen = False
            break
        elif backpackinput == "take knife":
            print("You are now holding your knife in your hand.")
            holdingCurrentItem = "Knife"
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
