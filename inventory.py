# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:06:46 2024

@author: danre
"""

import copy

# import item
from item import Item
from item import TYPE_GOLD
from item import TYPE_WEAPON
from item import TYPE_ARMOR
from item import TYPE_RING
from item import TYPE_KEY
from item import TYPE_TROPHY
from item import TYPE_SPELL_PORT_HOME
from item import TYPE_SPELL_DISARM
from item import TYPE_SPELL_FIREBALL
from item import TYPE_SPELL_LIGHTNING_BOLT
from item import TYPE_SPELL_WRATH_OF_NATURE
from item import TYPE_HEALTH_POTION
from item import TYPE_POWER_POTION


from item import RING_LUCKY
from item import RING_POWER
from item import RING_DEFENSE
from item import RING_INVISIBILITY


from config import verbosity


class Inventory:
    name = ""
    items = { }

    def __init__(self, name):
        # verbosity = verbosity
        self.name = name
        self.items = { }

    def take(self, item, count = -1):
        if count > item.count or count == -1:
            count = item.count
        # new_count = item.count - count
        
        if item.name in self.items:
            print("adding {} more {} item{} to {}".format(count, item.name, "s" if count != 1 else "", self.name))
            self.items[item.name].count += count
        else:
            print("adding {} {} item{} to {}".format(count, item.name, "s" if count != 1 else "", self.name))
            self.items[item.name] = copy.deepcopy(item)
            self.items[item.name].count = count
    
    def drop(self, name, count = -1):
        if not name in self.items:
            print("drop: '{}' not found in {}".format(name, self.name))
        else:
            item = self.items[name]
            if count > item.count or count == -1:
                count = item.count
            print("dropping {} {} item{} from {}".format(count, name, "s" if count != 1 else "", self.name))
            item.count -= count
            if item.count < 1:
                print("last {} removed from {}".format(name, self.name))
                del self.items[name]
    
    def move(self, name, dest, count = -1):
        if not name in self.items:
            print("drop: '{}' not found in {}".format(name, self.name))
        else:
            sCount = "{}".format(count if count > -1 else "all")
            print("moving {} {} item{} from {} to {}".format(sCount, name, "s" if count != 1 else "", self.name, dest.name))
            
            item = self.items[name]
            if count > item.count or count == -1:
                count = item.count
        
            if name in dest.items:
                print("adding {} more {} item{} to {}".format(count, item.name, "s" if count > 1 else "", dest.name))
                dest.items[item.name].count += count
            else:
                print("adding {} {} item{} to {}".format(count, item.name, "s" if count != 1 else "", dest.name))
                dest.items[item.name] = copy.deepcopy(item)
                dest.items[item.name].count = count

            print("dropping {} {} item{} from {}".format(count, name, "s" if count != 1 else "", self.name))
            item.count -= count
            if item.count < 1:
                print("last {} removed from {}".format(name, self.name))
                del self.items[name]
        
        
    def list_inventory(self):
        if len(self.items) < 1:
            print("no items found in {}".format(self.name))
        for name in self.items:
            item = self.items[name]
            if item.count == 1:
                print("{}: '{}'".format(self.name, item.name))
            else:
                print("{}: '{}'  ({})".format(self.name, item.name, item.count))
            
        
def main():
    
    pile = Inventory("Pile")
    inventory = Inventory("Pack")

    pile.list_inventory()
    inventory.list_inventory()
    
    itm = Item(name="Sword", itemType=TYPE_WEAPON, tier=1, count=1, limit=1, cost=50, nValue=0, fValue=1.5)
    # itm.show_item()
    pile.take(itm)
    itm = Item("Baseball Cap", TYPE_ARMOR, 0, 2, 2, 15, 8, 0.0)
    # itm.show_item()
    pile.take(itm)
    itm = Item("Baseball Cap", TYPE_ARMOR, 0, 3, 2, 15, 8, 0.0)
    # itm.show_item()
    pile.take(itm)
    itm = Item("Lucky Ring", TYPE_RING, RING_LUCKY, 1, 1, 350, 10, 0.0)
    # itm.show_item()
    pile.take(itm)
    itm = Item("Disarm", TYPE_SPELL_DISARM, 1, 4, 5, 20, 0, 0.0)
    # itm.show_item()
    pile.take(itm)
    itm = Item("Poison-2", TYPE_POWER_POTION, 2, 3, 5, 25, 120, 1.8)
    # itm.show_item()
    pile.take(itm)
    itm = Item("Elixir-3", TYPE_HEALTH_POTION, 3, 2, 5, 50, 20, 0.0)
    # itm.show_item()
    pile.take(itm)
    
    # print("Pile:")
    print()
    pile.list_inventory()
    inventory.list_inventory()
    print()

    itm = pile.items["Sword"]
    inventory.take(itm)
    pile.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    

    itm = pile.items["Baseball Cap"]
    inventory.take(itm, 1)
    pile.drop(itm.name, 1)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    itm = pile.items["Baseball Cap"]
    inventory.take(itm)
    pile.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    
    itm = pile.items["Lucky Ring"]
    inventory.take(itm)
    pile.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    
    itm = pile.items["Disarm"]
    inventory.take(itm)
    pile.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    
    itm = pile.items["Poison-2"]
    inventory.take(itm)
    pile.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    
    itm = pile.items["Elixir-3"]
    inventory.take(itm)
    pile.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()


    itm = inventory.items["Sword"]
    pile.take(itm)
    inventory.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    itm = inventory.items["Baseball Cap"]
    pile.take(itm)
    inventory.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    itm = inventory.items["Lucky Ring"]
    pile.take(itm)
    inventory.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    itm = inventory.items["Disarm"]
    pile.take(itm)
    inventory.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    itm = inventory.items["Poison-2"]
    pile.take(itm)
    inventory.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    itm = inventory.items["Elixir-3"]
    pile.take(itm)
    inventory.drop(itm.name)
    pile.list_inventory()
    inventory.list_inventory()
    print()
    
    
    pile.move("Sword", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Baseball Cap", inventory, 1)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Baseball Cap", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Lucky Ring", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Disarm", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Poison-2", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Elixir-3", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    pile.move("Bogus Item", inventory)
    pile.list_inventory()
    inventory.list_inventory()
    print()

    
    
    


if __name__ == '__main__':
    # title_screen()

    # print()
    main()


    if verbosity > 5:
        print("Done.")
