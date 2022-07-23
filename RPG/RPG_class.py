import random as rn
import RPG_items as loot

class Item:
    def __init__(self, name, AD, Def, HP, Equipped, LvL, type, rarity):
        #Name of the item
        self.name = name
        #Various stats
        self.AD = AD
        self.Def = Def
        self.HP = HP
        #Boolean value tracking whether or not the item is in use
        self.Equipped = Equipped
        #The required level to use the item
        self.Lvl = LvL
        #The type of the item: weapon (AD), helmet, gauntlets, chestpiece, boots (all Def and a little HP), and banner (HP and a little Def)
        #Only one of each type may be equipped at a time. 
        self.type = type
        # Rarity. Higher rarity items drop less frequently, but have better stats. In addition,
        # higher rarity items will give more types of stats (To be implemented in a later version) 
        self.rarity = rarity
    
    #equip/unequip an item
    def Equip(self):
        self.Equipped = 1
    
    def Unequip(self):
        self.Equipped = 0

class Character:
    #Core stats. Wallet will not be used in this version. 
    Wallet = 0
    AD = 5
    Max_HP = 100
    Curr_HP = 100
    Def = 5
    Inventory = [Item]
    Level = 1
    XP = 0
    XP_needed = 100

    #Role to be implemented later
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    #For now, XP needs scale linearly with level. May change to exponential in the future.
    def levelUp(self):
        self.Level += 1
        self.XP_needed += self.Level * 100

    #simple fxn for gaining xp. Checks for a level-up.
    def addXP(self, XP):
        if self.XP + XP >= self.XP_needed:
            self.levelUp()
            self.XP = self.XP + XP - self.XP_needed
        else:
            self.XP += XP
    
    #adds an item to the inventory.
    def getItem(self, item: Item):
        self.Inventory.append(item)

    #Equips an item. Has returns for if the item is already equipped or if level is insufficient.
    #If another item of the same type (ex: weapon, helmet) is already equipped, unequips it and
    #equips the selected item.
    def equipItem(self, item: Item):
        if item.Equipped == 1:
            print("Item is already equipped!")
        elif item.Lvl <= self.Level:
            for i in self.Inventory:
                if i.Equipped == 1 and i.type == item.type:
                    i.Unequip()
                    self.AD -= i.AD
                    self.Def -= i.Def 
                    self.Max_HP -= i.HP
                    self.Curr_HP -= i.HP
            item.Equip()
            self.AD += item.AD
            self.Def += item.Def 
            self.Max_HP += item.HP
            self.Curr_HP += item.HP
        else:
            print("You are not a high enough level to equip this item!")

class Enemy:
    lootTable = [tuple]
    def __init__(self, name, b_AD, b_Def, b_HP, level, XP):
        self.name = name
        self.AD = b_AD * level
        self.Def = b_Def * level
        self.HP = b_HP * level
        #the XP a monster gives out when it dies
        self.XP = XP * level
    
    #every enemy has a Loot Table, a list of items paired with odds. How it works is that 
    #all the odds values total to 1. When defeated, a random number 0-1 is generated. If it
    #is greater than lootable[0][0] (the odds of the first item), then the odds of that item
    #are subtracted from that number and we move on to loottable[1][0] until the random number
    #is reduced to less than the odds of something. Then, that item is given. 
    #As an example, if the three values are [.8, nothing], [.1, bronze sword], [.1, bronze helmet],
    #rolling below .8 gives nothing. rolling a .8-.899999... gives sword, .9-1 gives helmet.
    def addLoot(self, item: Item, odds):
        self.lootTable.append([odds, item])

#in V 0.0.1 (the first version), there are five enemy types. Generator fxns are below. 
#Each fxn has a short lore comment that I will hopefully expand upon!

#The Surge are the grunts of the Ashen. They are reanimated corpses filled with carefully enchanted
#electrical magic that pilots the body automatically. Easy to make and unfailingly loyal, they are the footsoldiers
#of the Ashen King. Their name comes from the fact that, when they die, they occasionally release a small surge of electricity,
#disorienting nearby Surge and shocking anyone touching them slightly. Clearly, the spell is not perfect...
def makeSurge(lvl):
    surge = Enemy("Surge", 7, 10, 48 + rn.randint(-3, 2), lvl, 20)
    surge.addLoot(None, .90)
    surge.addLoot(loot.bronze_sword, .05)
    surge.addLoot(loot.bronze_boots, .01)
    surge.addLoot(loot.bronze_gauntlets, .01)
    surge.addLoot(loot.bronze_helmet, .01)
    surge.addLoot(loot.bronze_chest, .01)
    surge.addLoot(loot.bronzed_banner, .01)
    return surge

#The Null are what make the Ashen a dominant invasion force. Whenever the Ashen arrive in an area, they are preceded by
#a magically-induced cloud of ash. One purpose of this is to intimidate, another is to hide their movements, but the most 
#important is to deploy the Null. Shapeless and ruthless, the Null are a shadowy race who are literally one with the ash,
#sinking into it and disappearing completely, only to pop out again in a nearby soot pile. They are master assassins who are 
#impossible to follow, since their unique ability means they can teleport up to 10 miles between ash clouds. When an ash cloud
#rolls in, the Null are counted on to quickly eliminate unaware targets, no matter how dangerous.
def makeNull(lvl):
    null = Enemy("Null", 300 + rn.randint(-50, 80), 700, 900 + rn.randint(-30, 60), lvl, 2000)
    return     