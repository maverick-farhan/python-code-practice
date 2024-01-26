#!/usr/bin/env python3
"""
This is comment
And nothing more now
"""
inventory_items = {'wood':13,'fuel':3,'food':30,'rope':3,'gold_coins':10,'arrow':10,'axe':20}
dragon_loot = ['gold_coins','dagger','gold_coins','ruby']
def display_intentory(inv_items):
    total = 0
    print('Inventory:')
    for k,v in inv_items.items():
        total += inv_items.get(k,0)
        print(str(v) + ' '+ k)
    print('total items: '+ str(total))

#addToInventory return dictionary {}
def addToInventory(inv_items,lootList):
    for loot in lootList:
        inv_items.setdefault(loot,0)
        inv_items[loot]+=1
    return inv_items
inventory_items = addToInventory(inventory_items,dragon_loot)
display_intentory(inventory_items)
