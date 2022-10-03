# imports
from typewriter import *
from pyfiglet import figlet_format
import os
from locations import *

typewriterEff("""It is a cold, misty day in the Himalaya Mountains and you are trying to hike to the peak of Mount Everest, the highest mountain in the world.
You are with your companions Peter and Maxwell.""")

typewriterEff("""

Peter: 'Wait.. """)
sleep(0.75)
typewriterEff("""what is that sound from the distance?'""")
sleep(0.5)

typewriterEff("""

Maxwell: 'I have no idea! But it does not sound good.'""")
sleep(0.5)

typewriterEff("""

You're looking up in the distance and you see... """)
sleep(1)

print("AN AVALANCHE!")
sleep(0.5)

typewriterEff("""
Suddenly everything turns white... """)
sleep(0.5)
typewriterEff("""and you only hear Peter and Maxwell yelling!""")
sleep(0.5)

typewriterEff("""

Then..""")
sleep(1)
typewriterEff(""" everything turns dark for a few seconds...""")
sleep(0.5)

typewriterEff("""

You open your eyes and see a bright light, the sun is shining and you realise that you've been out cold for a very long time.""")
sleep(0.5)

os.system('cls')

typewriterEffTitle(figlet_format("The Avalanche", font="big"))

typewriterEff("""
Your mouth is dry and you are hungry.
The backpack you took with you is with you, it survived the avalanche.
Maybe there is something in your backpack which might be useful.
""")

print(colored("---------------------------", "blue"))
print(colored("CONTROLS:", "green"))
print(colored("north", "red"))
print(colored("east", "red"))
print(colored("south", "red"))
print(colored("west", "red"))
print(colored("also commands like: take and use.\n", "red"))
print(colored("You need to find the other commands out by yourself.\n", "red"))
print(colored("Your backpack is always with you.\n", "red"))
print(colored("Good luck! -Ahmet & Koray.", "yellow"))
print(colored("---------------------------", "blue"))

input(colored("Press a key to start the game..", "green"))

Startpoint()
