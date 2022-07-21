import random as rn
import RPG_class as c
from time import sleep

#takes in a name, retuns the new character to play as
def makeNewCharacter():
    name = str(input("\nEnter your character's name: "))
    return c.Character(name, None)

def getSave():
    return

#returns a semi-random list of enemies depending on the area. Each area of 
#the game has an ID, 1 being the starting area and incrementing up in the order
#they are unlocked. This first version has one area and five enemy types within it.
def generate_enemies(area):
    
    return

#The main gameplay loop!
def play(hero: c.Character):
    print("You, ", hero.name,", are the hero of our story.", sep="")
    return

def main():
    print("Welcome to Ashen Conquest. Enjoy!")
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