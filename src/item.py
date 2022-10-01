"""
Filename: item.py
Date Created: 1/6/2021

An Item is the most basic type of thing in Factorio. At its most basic level, an item is only a thing with a stack size.
"""

class Item:
    def __init__(self, name, stackSize, recipeList=None, imageFile=None):
        if recipeList is None:
            recipeList = ['DEFAULT']
        self.name = name
        self.stackSize = stackSize
        self.recipes = recipeList
        self.imageFile = imageFile

    def __str__(self):
        return "Item: " + self.name + "\n" + "Stack Size: " + str(self.stackSize)

    def __eq__(self, otherItem):
        return True if otherItem.name == self.name else False



if __name__ == "__main__":
    myItem = Item("rocks", 100)
    print(myItem)