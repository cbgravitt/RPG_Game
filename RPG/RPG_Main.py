import random as rn
import RPG_class as c
from time import sleep

def makeNewCharacter():
    name = str(input("\nEnter your character's name: "))
    return c.Character(name, None)

def getSave():
    return

def play(hero: c.Character):
    print("You, ", hero.name,", are the hero of our story.", sep="")
    return

def main():
    print("Welcome to... well I don't have a title yet. Enjoy!")
    while(1):
        i = int(input("\nPress 1 to start a new game, or press 2 to load a save file: "))
        if i==1 or i==2:
            break
        else:
            print("Enter a valid number....\n")
    if i == 1:
        hero = makeNewCharacter()
        play(hero)
    if i == 2:
        hero = getSave()
        play(hero)

if __name__ == '__main__':
    main()