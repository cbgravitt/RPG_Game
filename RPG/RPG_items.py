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
bronze_chest = c.Item("Bronze Chestpiece", 0, 7, 0, False, 5, "Chest", "Common")
bronze_boots = c.Item("Bronze Boots", 0, 5, 0, False, 5, "Boots", "Common")
bronze_gauntlets = c.Item("Bronze Gauntlets", 0, 3, 0, False, 5, "Gauntlets", "Common")
bronzed_banner = c.Item("Bronzed Banner", 0, 0, 30, False, 5, "Banner", "Common")

iron_sword = c.Item("Iron Sword", 40, 0, 0, False, 15, "Weapon", "Common")
iron_helmet = c.Item("Iron Helmet", 0, 18, 0, False, 15, "Helmet", "Common")
iron_chest = c.Item("Iron Mail", 0, 25, 0, False, 15, "Chest", "Common")
iron_boots = c.Item("Iron Greaves", 0, 18, 0, False, 15, "Boots", "Common")
iron_gauntlets = c.Item("Iron Gauntlets", 0, 15, 0, False, 15, "Gauntlets", "Common")
iron_banner = c.Item("Ironclad Banner", 0, 0, 90, False, 15, "Banner", "Common")

steel_sword = c.Item("Steel Sword", 100, 0, 0, False, 30, "Weapon", "Common")
steel_helmet = c.Item("Steel Helmet", 0, 35, 0, False, 30, "Helmet", "Common")
steel_chest = c.Item("Steel Chestplate", 0, 45, 0, False, 30, "Chest", "Common")
steel_boots = c.Item("Steel Greaves", 0, 35, 0, False, 30, "Boots", "Common")
steel_gauntlets = c.Item("Steel Gauntlets", 0, 30, 0, False, 30, "Gauntlets", "Common")
steel_banner = c.Item("Steel-Tipped Banner", 0, 0, 200, False, 30, "Banner", "Common")

gilded_sword = c.Item("Gilded Sword", 180, 0, 0, False, 50, "Weapon", "Common")
gilded_helmet = c.Item("Gilded Helmet", 0, 50, 0, False, 50, "Helmet", "Common")
gilded_chest = c.Item("Gilded Mail", 0, 65, 0, False, 50, "Chest", "Common")
gilded_boots = c.Item("Gilded Greaves", 0, 50, 0, False, 50, "Boots", "Common")
gilded_gauntlets = c.Item("Gilded Gauntlets", 0, 45, 0, False, 50, "Gauntlets", "Common")
gilded_banner = c.Item("Gilded Banner", 0, 0, 350, False, 50, "Banner", "Common")

#The ashen and divine sets are somewhat special and are mainly in here as a shot at
#adding some item variety, since I plan to overhaul the item system in a later version
#(probably 0.0.5/4). These ones focus more on one attribute each, the ashen giving bonus attack
#but the divine giving more health and defense. An end-game character would mix and match.

ashen_sword = c.Item("Ashen Sickle", 400, 0, 0, False, 80, "Weapon", "Common")
ashen_helmet = c.Item("Ashen Helmet", 30, 75, 0, False, 80, "Helmet", "Common")
ashen_chest = c.Item("Ashen Chestplate", 60, 90, 0, False, 80, "Chest", "Common")
ashen_boots = c.Item("Ashen Greaves", 30, 75, 0, False, 80, "Boots", "Common")
ashen_gauntlets = c.Item("Ashen Gauntlets", 20, 70, 0, False, 80, "Gauntlets", "Common")
ashen_banner = c.Item("Ashen Banner", 100, 0, 500, False, 80, "Banner", "Common")

divine_sword = c.Item("Divine War Hammer", 325, 30, 100, False, 80, "Weapon", "Common")
divine_helmet = c.Item("Divine Helmet", 0, 90, 75, False, 80, "Helmet", "Common")
divine_chest = c.Item("Divine Chestplate", 0, 120, 100, False, 80, "Chest", "Common")
divine_boots = c.Item("Divine Greaves", 0, 90, 75, False, 80, "Boots", "Common")
divine_gauntlets = c.Item("Divine Gauntlets", 0, 80, 50, False, 80, "Gauntlets", "Common")
divine_banner = c.Item("Blessed Banner", 0, 50, 700, False, 80, "Banner", "Common")