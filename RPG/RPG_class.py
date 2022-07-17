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
    Wallet = 0
    AD = 5
    Max_HP = 100
    Curr_HP = 100
    Def = 5
    Inventory = [Item]
    Level = 1
    XP = 0
    XP_needed = 100

    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def levelUp(self):
        self.Level += 1
        self.XP_needed += self.Level * 100

    def addXP(self, XP):
        if self.XP + XP >= self.XP_needed:
            self.levelUp()
            self.XP = self.XP + XP - self.XP_needed
        else:
            self.XP += XP
    
    def getItem(self, item: Item):
        self.Inventory.append(item)

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
    def __init__(self, name, b_AD, b_Def, b_HP, level, scaling):
        self.name = name
        self.AD = b_AD + level*scaling
        self.Def = b_Def + level*scaling
        self.HP = b_HP + level*scaling


            
    

    

    