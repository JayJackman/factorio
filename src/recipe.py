"""
Filename: recipe.py
Date Created: 1/6/2021
A Recipe describes the process by which things are crafted in Factorio. It has two IngredientLists: one for the inputs
required and one for the outputs produced
"""

from ingredient_list import IngredientList
from ingredient import Ingredient
from dictionaries.items import itemDict


class Recipe:
    def __init__(self, name, time, allowsProd: bool, inputs: IngredientList, outputs: IngredientList,
                 buildingList=None, imageFilePath=None):
        if buildingList is None:
            buildingList = ['Assembling Machine 3']
        self.name = name
        self.craftingTime = time
        self.inputs = inputs
        self.outputs = outputs
        self.allowsProd = allowsProd
        self.buildings = buildingList
        self.imageFile = imageFilePath

    def __eq__(self, otherRecipe):
        return True if self.name == otherRecipe.name else False

    def __str__(self):
        if self.craftingTime == 1:
            toReturn = "Recipe: " + self.name + " (" + str(self.craftingTime) + " sec)" + "\n"
        else:
            toReturn = "Recipe: " + self.name + " (" + str(self.craftingTime) + " secs)" + "\n"
        if self.allowsProd:
            toReturn += "Allows Prod: Yes\n"
        else:
            toReturn += "Allows Prod: No\n"
        toReturn += "Inputs:\n" + self.inputs.getStringOfIngredients()
        toReturn += "\n"
        toReturn += "Outputs:\n" + self.outputs.getStringOfIngredients()

        return toReturn

    def getInputs(self):
        return self.inputs.getIngredients()

    def getOutputs(self):
        return self.outputs.getIngredients()

    def __eq__(self, otherRecipe):
        return True if otherRecipe.name == self.name else False

    @classmethod
    def getEmptyRecipe(cls, output: Ingredient):
        outputList = IngredientList()
        outputList.addIngredient(output)

        name = 'Treat As Raw'
        time = 1
        allowsProd = False
        inputs = IngredientList()
        outputs = outputList
        buildingList = None
        imageFilePath = itemDict[output.name].imageFile
        return Recipe(name, time, allowsProd, inputs, outputs, buildingList, imageFilePath)

    @classmethod
    def getAlwaysRawEmptyRecipe(cls, output: Ingredient):
        outputList = IngredientList()
        outputList.addIngredient(output)

        name = 'Treat As Raw (Always)'
        time = 1
        allowsProd = False
        inputs = IngredientList()
        outputs = outputList
        buildingList = None
        imageFilePath = itemDict[output.name].imageFile
        return Recipe(name, time, allowsProd, inputs, outputs, buildingList, imageFilePath)



if __name__ == "__main__":
    from ingredient import Ingredient
    from item import Item

    item1 = Item("Rocks", 100)
    item2 = Item("Dogs", 10)
    item3 = Item("Beds", 50)

    ingredient1 = Ingredient(item1, 30)
    ingredient2 = Ingredient(item2, 40)
    ingredient3 = Ingredient(item3, 1)
    ingredient4 = Ingredient(item1, 20)

    inputList = IngredientList()
    inputList.addIngredient(ingredient1)
    inputList.addIngredient(ingredient3)

    outputList = IngredientList()
    outputList.addIngredient(ingredient2)
    outputList.addIngredient(ingredient4)

    myRecipe = Recipe("Making dogs", 1, True, inputList, outputList)
    print(myRecipe)
