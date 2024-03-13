# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:07:10 2024

@author: danre
"""


from config import verbosity


TYPE_GOLD = 0
TYPE_WEAPON = 1
TYPE_ARMOR = 2
TYPE_RING = 3
TYPE_KEY = 4
TYPE_TROPHY = 5
TYPE_SPELL_PORT_HOME = 64
TYPE_SPELL_DISARM = 65
TYPE_SPELL_FIREBALL = 92
TYPE_SPELL_LIGHTNING_BOLT = 93
TYPE_SPELL_WRATH_OF_NATURE = 94
TYPE_HEALTH_POTION = 128
TYPE_POWER_POTION = 129


RING_LUCKY = 1
RING_POWER = 2
RING_DEFENSE = 3
RING_INVISIBILITY = 4

class Item:
    name = ""
    itemType = TYPE_GOLD
    limit = 0
    count = 0
    cost = 0
    fValue = 0.0
    vValue = 0
    tier = 0
    
    def __init__(self, name, itemType, tier, count, limit, cost, nValue, fValue):
        # verbosity = verbosity
        self.name = name
        self.itemType = itemType
        self.tier = tier
        self.count = count
        self.limit = limit
        self.cost = cost
        self.nValue = nValue
        self.fValue = fValue

    def isPotion(self):
        if self.itemType in (TYPE_HEALTH_POTION, TYPE_POWER_POTION):
            return True
        return False
            
    def isSpell(self):
        if self.itemType in (TYPE_SPELL_PORT_HOME, TYPE_SPELL_DISARM, TYPE_SPELL_FIREBALL, TYPE_SPELL_LIGHTNING_BOLT, TYPE_SPELL_WRATH_OF_NATURE):
            return True
        return False
            
    @staticmethod
    def type2text(itemType):
        if itemType == TYPE_GOLD:
            return "Gold"
        if itemType == TYPE_WEAPON:
            return "Weapon"
        if itemType == TYPE_ARMOR:
            return "Armor"
        if itemType == TYPE_RING:
            return "Ring"
        if itemType == TYPE_KEY:
            return "Key"
        if itemType == TYPE_TROPHY:
            return "Trophy"
        if itemType == TYPE_SPELL_PORT_HOME:
            return "Return to Home Spell"
        if itemType == TYPE_SPELL_DISARM:
            return "Disarm Spell"
        if itemType == TYPE_SPELL_FIREBALL:
            return "Fireball Spell"
        if itemType == TYPE_SPELL_LIGHTNING_BOLT:
            return "Lightning Bolt Spell"
        if itemType == TYPE_SPELL_WRATH_OF_NATURE:
            return "Wrath of Nature Spell"
        if itemType == TYPE_POWER_POTION:
            return "Power Potion"
        if itemType == TYPE_HEALTH_POTION:
            return "Health Potion"
            
    def show_item(self, brief=True):
        if brief:
            if self.count == 1:
                print("{}".format(self.name))
            else:
                print("{}  ({})".format(self.name, self.count))
        else:            
            print("Name:     '{}'".format(self.name))
            print("Type:      {}".format(Item.type2text(self.itemType)))
            print("Tier:      {}".format(self.tier))
            print("Count:     {}".format(self.count))
            print("Limit:     {}".format(self.limit))
            print("Cost:      {}".format(self.cost))
            print("nValue:    {}".format(self.nValue))
            print("fValue:    {}".format(self.fValue))
            print("is spell?  {}".format(self.isSpell()))
            print("is potion? {}".format(self.isPotion()))
            print()



def main():
    sword = Item("Sword", TYPE_WEAPON, 1, 1, 1, 50, 0, 1.5)
    helmet = Item("Baseball Cap", TYPE_ARMOR, 0, 2, 2, 15, 8, 0.0)
    ring = Item("Lucky Ring", TYPE_RING, RING_LUCKY, 1, 1, 350, 10, 0.0)
    disarm = Item("Disarm", TYPE_SPELL_DISARM, 1, 4, 5, 20, 0, 0.0)
    poison = Item("Poison-2", TYPE_POWER_POTION, 2, 3, 5, 25, 120, 1.8)
    elixir = Item("Elixir-3", TYPE_HEALTH_POTION, 3, 2, 5, 50, 20, 0.0)

    sword.show_item(False)
    helmet.show_item(False)
    ring.show_item(False)
    disarm.show_item(False)
    poison.show_item(False)
    elixir.show_item(False)

    print()
    sword.show_item()
    helmet.show_item()
    ring.show_item()
    disarm.show_item()
    poison.show_item()
    elixir.show_item()
    
    
if __name__ == '__main__':
    # title_screen()

    # print()
    main()


    if verbosity > 5:
        print("Done.")
