from locations import *
from inventory import *

while True:
    input()
    if input() == "open backpack":
        backpack()
    if input() == "use knife":
        if holdingCurrentItem == "knife":
            print("You can not use that here!")
