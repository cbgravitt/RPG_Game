import RPG_class as c

#This file functions as an item list so I don't have to make them on the fly.
#This file should not be tampered with if the game is to be played legit. More 
#items added every version! As of now, every piece will always be the same, even across 
#duplicates. This will not be the case in later versions, where multiple copies of
#the same items may have slightly different core or auxilliary stats (to be implemented)
#Another feature to be added is set bonuses. Items grouped together below
#encompass a set, and when used all at once will give percent bonuses to the wearer.

stick = c.Item("Stick", 5, 0, 0, False, 1, "Weapon", "Common")
cloth_cap = c.Item("Cloth Cap", 0, 2, 0, False, 1, "Helmet", "Common")
cloth_shirt = c.Item("Cloth Shirt", 0, 3, 0, False, 1, "Chest", "Common")
cloth_shoes = c.Item("Cloth Shoes", 0, 2, 0, False, 1, "Boots", "Common")
cloth_gloves = c.Item("Cloth Gloves", 0, 5, 0, False, 1, "Gauntlets", "Common")
cloth_banner = c.Item("Cloth Banner", 0, 0, 10, False, 1, "Banner", "Common")

bronze_sword = c.Item("Bronze Sword", 15, 0, 0, False, 5, "Weapon", "Common")
bronze_helmet = c.Item("Bronze Helmet", 0, 5, 0, False, 5, "Helmet", "Common")
bronze_chest = c.Item("Bronze Helmet", 0, 7, 0, False, 5, "Chest", "Common")
bronze_boots = c.Item("Bronze Helmet", 0, 5, 0, False, 5, "Boots", "Common")
bronze_gauntlets = c.Item("Bronze Helmet", 0, 3, 0, False, 5, "Gauntlets", "Common")
bronzed_banner = c.Item("Bronzed Banner", 0, 0, 30, False, 5, "Banner", "Common")