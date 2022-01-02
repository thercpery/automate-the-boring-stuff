# inventory.py
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(item_total)

# def addToInventory(inventory, add_items):
#     for k, v in inventory.items():
#         for item in range(len(add_items)):
#             if add_items[item] == k:
#                 v += v.get()
#             else:
#                 inventory.setdefault(add_items[item], 1)
#     return inventory

def addToInventory(inv, loot):
    for loot_item in loot:
        inv[loot_item] = inv.get(loot_item, 0) + 1
    return inv

addToInventory(stuff, dragon_loot)
displayInventory(stuff)