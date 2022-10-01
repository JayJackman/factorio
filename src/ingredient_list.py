"""
Filename: ingredient_list.py
Date Created: 1/6/2021

An IngredientList is simply a container for multiple Ingredients. These can be used to consolidate different ingredients
to be used in Recipes or otherwise.
"""
import warnings


class IngredientList(dict):
    def __init__(self, *args, **kw):
        super(IngredientList, self).__init__(*args, **kw)
        self.ingredients = super(IngredientList, self).keys()

    def __str__(self):
        toReturn = "IngredientList:\n"
        toReturn += self.getStringOfIngredients()
        return toReturn

    def getStringOfIngredients(self):
        toReturn = ""
        for key in self:
            ingredient = self[key]
            toReturn += "- " + ingredient.name + " (" + str(ingredient.amount) + ")\n"
        return toReturn

    def addIngredient(self, ingredient):
        # If the ingredient already exists, throw a warning
        if ingredient.name in self.keys():
            warnings.warn("Ingredient \"" + ingredient.name + "\" already exists in this IngredientList. Overwriting.")

        self.__setitem__(ingredient.name, ingredient)

    def getIngredients(self):
        return [self[key] for key in self]


if __name__ == "__main__":
    from ingredient import Ingredient
    from item import Item

    item1 = Item("Pipe", 100)
    item2 = Item("Rail", 10)
    item3 = Item("Transport Belt", 50)

    ingredient1 = Ingredient("Pipe", 30)
    ingredient2 = Ingredient("Rail", 40)
    ingredient3 = Ingredient("Transport Belt", 1)

    ingredient4 = Ingredient("Pipe", 20)

    myIngredientList = IngredientList()
    print(myIngredientList)
    myIngredientList.addIngredient(ingredient1)
    print(myIngredientList)
    myIngredientList.addIngredient(ingredient3)
    print(myIngredientList)
    myIngredientList.addIngredient(ingredient2)
    print(myIngredientList)
    myIngredientList.addIngredient(ingredient4)
    print(myIngredientList)

    for i in myIngredientList.getIngredients():
        print(i)


