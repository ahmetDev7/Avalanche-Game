import os
import globalmethods
from colorama import init
from termcolor import colored

currentChapter = None


def checkChapter(chapterSelection):
    if chapterSelection.lower() == "chapter 2":
        SurvivalBookCh2()

    elif chapterSelection.lower() == "chapter 3":
        SurvivalBookCh3()

    elif chapterSelection.lower() == "chapter 4":
        SurvivalBookCh4()

    elif chapterSelection.lower() == "chapter 5":
        SurvivalBookCh5()
    elif chapterSelection.lower() == "exit" or chapterSelection.lower() == "exit book" or chapterSelection.lower() == "exit survival book" or chapterSelection.lower() == "leave book" or chapterSelection.lower() == "leave survival book" or chapterSelection.lower() == "stop reading":
        return 0

    else:
        print("Dat is geen optie.")
        if currentChapter == 1:
            OpenSurvivalBook()
        elif currentChapter == 2:
            SurvivalBookCh2()
        elif currentChapter == 3:
            SurvivalBookCh3()
        elif currentChapter == 4:
            SurvivalBookCh4()
        elif currentChapter == 5:
            SurvivalBookCh5()


def OpenSurvivalBook():
    os.system('cls')
    global currentChapter
    currentChapter = 1
    print(colored("------------------------------------------------", "blue"))
    print(colored("""'Chapter 1. Basic Survival Guide'
The most important thing when surviving is
food and water. If you find a running water
source you can use the water and boil it to kill
the bacteria in it so the water will be purified.
You must avoid food from plants because
these can be poisonous, rather you should try
to hunt herbivorous animals like deer or cattle
or aquatic animals like fish.""", "green"))
    print(colored("-------------------------------------------------", "blue"))

    bookInput = input("> ")
    if bookInput.lower() == "next page" or bookInput.lower() == "next":
        SurvivalBookCh2()
    elif bookInput.lower() == "previous page" or bookInput.lower() == "previous":
        print(colored("There are no previous pages.", "red"))
        globalmethods.continueKey()
        OpenSurvivalBook()
    else:
        chapterSelection = bookInput
        checkChapter(chapterSelection)


def SurvivalBookCh2():
    os.system('cls')
    global currentChapter
    currentChapter = 2
    print(colored("------------------------------------------------", "blue"))
    print(colored("""'Chapter 2. Find shelter'
"Look for a place where you will be kept warm
and safe from predators or extreme weather
conditions. If there are any caves nearby
these can work well for this purpose.
Caves are very handy for cooking food,
because wildlife might get attracted if you do
it openly in the wild. Also there is no wind
inside so your fire will stay put.""", "green"))
    print(colored("------------------------------------------------", "blue"))
    bookInput = input("> ")
    if bookInput.lower() == "next page" or bookInput.lower() == "next":
        SurvivalBookCh3()
    elif bookInput.lower() == "previous page" or bookInput.lower() == "previous":
        OpenSurvivalBook()
    else:
        chapterSelection = bookInput
        checkChapter(chapterSelection)


def SurvivalBookCh3():
    os.system('cls')
    global currentChapter
    currentChapter = 3
    print(colored("----------------------------------------------------------", "blue"))
    print(colored("""'Chapter 3. Resources'
Use what you have in your reach. A knife can be used
as a weapon or a tool to cut things that might come in
your way. Tools like axes, shovels and saws can be
used for different purposes like cutting a tree, digging a
hole or splitting a piece of wood.
Also tools like a fishing rod might come in handy if
there is a running water source nearby, with this you
can catch aquatic animals to consume and stay free
from hunger.""", "green"))
    print(colored("----------------------------------------------------------", "blue"))
    bookInput = input("> ")
    if bookInput.lower() == "next page" or bookInput.lower() == "next":
        SurvivalBookCh4()
    elif bookInput.lower() == "previous page" or bookInput.lower() == "previous":
        SurvivalBookCh2()
    else:
        chapterSelection = bookInput
        checkChapter(chapterSelection)


def SurvivalBookCh4():
    os.system('cls')
    global currentChapter
    currentChapter = 4
    print(colored("------------------------------------------------------------", "blue"))
    print(colored("""'Chapter 4. Start a fire'
Starting a fire is very important when trying to survive. It
can prevent you from getting hypothermia and can be
used for cooking and boiling your food and water.
To start a fire you need tinder and wood.
Tinder: Easily flammable material, like paper, dry grass,
and hair.
Wood: You can get this by cutting a tree or look around
if you can find a dry log.
When you have all of these materials you have the
tools to start a fire, now you only need a fire source.""", "green"))
    print(colored("------------------------------------------------------------", "blue"))
    bookInput = input("> ")
    if bookInput.lower() == "next page" or bookInput.lower() == "next":
        SurvivalBookCh5()
    elif bookInput.lower() == "previous page" or bookInput.lower() == "previous":
        SurvivalBookCh3()
    else:
        chapterSelection = bookInput
        checkChapter(chapterSelection)


def SurvivalBookCh5():
    os.system('cls')
    global currentChapter
    currentChapter = 5
    print(colored("--------------------------------------------------", "blue"))
    print(colored("""'Chapter 5. Wild animals'
Be careful of wild animals. Wild animals can be
dangerous but you can tame them by using food like
berries.""", "green"))
    print(colored("--------------------------------------------------", "blue"))
    bookInput = input("> ")
    if bookInput.lower() == "next page" or bookInput.lower() == "next":
        print(colored("There are no pages left.", "red"))
        globalmethods.continueKey()
        SurvivalBookCh5()
    elif bookInput.lower() == "previous page" or bookInput.lower() == "previous":
        SurvivalBookCh4()
    else:
        chapterSelection = bookInput
        checkChapter(chapterSelection)
