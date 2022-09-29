import sys
from time import sleep

def typewriterEff(words):
    for character in words:
        sleep(0.05)
        sys.stdout.write(character)
        sys.stdout.flush()