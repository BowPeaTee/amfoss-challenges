def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

# inventory.py
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total+=v
    print("Total number of items: " + str(item_total))
displayInventory(inv)