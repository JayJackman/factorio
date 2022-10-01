"""
Filename: ingredient.py
Date Created: 1/6/2021

An Ingredient is an Item along with an amount. A decimal amount corresponds to a percentage chance of spawning an item.
This is useful for recipes that might only return a waste material X percent of the time.
"""
from item import Item
from item_dictionary import itemDict

class Ingredient():
    def __init__(self, name, amount):
        self.item = itemDict[name]
        self.amount = amount
        self.name = name

    def __str__(self):
        return "Ingredient: " + self.item.name + "\n" + "Amount: " + str(self.amount)



if __name__ == "__main__":
    myItem = Item("Rocks", 100)
    myIngredient = Ingredient(myItem, 43)
    print(myIngredient)
