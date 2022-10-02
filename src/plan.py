"""
Filename: plan.py
Date Created: 1/7/2021
A plan calculates the required inputs to produce a desired item at a specified rate. In order to do this, a Recipe needs
to be specified as well as a building that produces that recipe. Modules can be inserted into that building to give
bonuses, as well as bonuses from beacons can be specified.
"""
import warnings

from ingredient import Ingredient
from recipe import Recipe
from building import Building
from module import Module
from ingredient_list import IngredientList
from dictionaries.items import itemDict
from dictionaries.recipes import recipeDict


class Plan():
    def __init__(self, desired: Ingredient, recipe: Recipe = None, building: Building = None, buildingModules = None, beaconModules = None):
        self.desiredIngredient: Ingredient = desired
        if recipe is None:
            # print(desired.item.name)
            self.recipe = recipeDict[desired.item.recipes[0]]
        else:
            self.recipe = recipe

        if building is None:
            self.building = itemDict[self.recipe.buildings[0]]
        else:
            self.building = building

        if buildingModules is None:
            self.buildingModules = Plan.makeEmptyModuleList(self.building.moduleSlots)
        else:
            self.buildingModules = buildingModules

        if beaconModules is None:
            # self.beaconModules = Plan.makeEmptyModuleList(8) # THIS IS LEGACY FOR SE. IF ITS BROKEN, THIS IS PROBABLY WHY
            self.beaconModules = []
        else:
            self.beaconModules = beaconModules

    @classmethod
    def copy(cls, plan):
        desired = plan.desiredIngredient
        recipe = plan.recipe
        building = plan.building
        buildingModules = plan.buildingModules.copy()
        beaconModules = plan.beaconModules.copy()
        return Plan(desired, recipe, building, buildingModules, beaconModules)

    @classmethod
    def makeEmptyModuleList(cls, numModules):
        toReturn = []
        for i in range(numModules):
            toReturn.append(itemDict['Empty Module'])
        return toReturn

    def __str__(self):
        toReturn = ""
        toReturn += "Plan: " + str(self.desiredIngredient.amount) + " " + self.desiredIngredient.name + " per sec\n"
        toReturn += "  Using Recipe: " + self.recipe.name + "\n"
        toReturn += "  Using Building: " + self.building.name + "\n"
        for module in self.buildingModules:
            toReturn += "  - " + module.name + "\n"
        if len(self.beaconModules) > 0:
            toReturn += "  Beacon Modules:\n"
            for module in self.beaconModules:
                toReturn += "  - " + module.name + "\n"
        toReturn += "  Inputs for one building:\n"
        inputIngredientList = self.calculateInputsForOneBuilding()
        for ingredient in inputIngredientList.getIngredients():
            toReturn += "  - " + ingredient.name + " (" + str(ingredient.amount) + ")\n"
        toReturn += "  Outputs from one building:\n"
        outputIngredientList = self.calculateOutputsFromOneBuilding()
        for ingredient in outputIngredientList.getIngredients():
            toReturn += "  - " + ingredient.name + " (" + str(ingredient.amount) + ")\n"
        numBuildings = self.calculateRequiredBuildingsForDesiredOutput()
        toReturn += "\n"
        toReturn += "  Required number of buildings: " + str(numBuildings) + "\n"
        toReturn += "  Total inputs required for " + str(self.desiredIngredient.amount) + " " + self.desiredIngredient.name + " per second:\n"
        inputIngredientList = self.calculateRequiredInputsForDesiredOutput()
        for ingredient in inputIngredientList.getIngredients():
            toReturn += "  - " + ingredient.name + " (" + str(ingredient.amount) + ")\n"
        toReturn += "  Total outputs produced with " + str(numBuildings) + " buildings:\n"
        outputIngredientList = self.calculateTotalOutputsProduced()
        for ingredient in outputIngredientList.getIngredients():
            toReturn += "  - " + ingredient.name + " (" + str(ingredient.amount) + ")\n"
        return toReturn

    def promptUser(self, desiredIngredient=None):
        if desiredIngredient is None:
            desiredItem = input("Enter the desired Item: " )
            while desiredItem not in itemDict:
                desiredItem = input("Invalid Item. Please enter the desired Item: ")
            desiredAmount = int(input("Enter the desired amount (Hz): "))
            desiredIngredient = Ingredient(desiredItem, desiredAmount)
        self.desiredIngredient = desiredIngredient

        userRecipe = input("Enter the desired Recipe for making " + self.desiredIngredient.name + ": ")
        while userRecipe not in recipeDict:
            userRecipe = input("Invalid Recipe. Please enter the desired Recipe for making " + self.desiredIngredient.name + ": ")
        self.recipe = recipeDict[userRecipe]

        userBuilding = input("Enter the desired Building for making " + self.recipe.name + ": ")
        if userBuilding is "a":
            userBuilding = "Assembling Machine 3"
        elif userBuilding is "s":
            userBuilding = "Space Manufactory"
        while userBuilding not in itemDict: # TODO: This check could be stronger (restricted to just buildings)
            userBuilding = input("Invalid Building. Please enter the desired Building for making " + self.recipe.name + ": ")
        self.building = itemDict[userBuilding]

        while len(self.buildingModules) < self.building.moduleSlots:
            numRemaining = self.building.moduleSlots - len(self.buildingModules)
            userModule = input("Enter Module for Building (" + str(numRemaining) + " slots left) (f to finish): ")
            if userModule is 'f':
                break
            num = userModule[0]
            if not num.isnumeric():
                print(num + " is not numeric. Try Again")
                continue
            num = int(num)
            if num > numRemaining:
                print(str(num) + " modules is more than the remaining slots. Try again.")
                continue
            moduleType = userModule[1]
            if moduleType not in Module.moduleTypes:
                print(moduleType + " is not recognized. Try again.")
                continue
            level = int(userModule[2])

            moduleName = Module.type2name(moduleType) + " Module " + str(level)
            for d in range(num):
                self.addBuildingModule(itemDict[moduleName])

        while True:
            userModule = input("Enter Module for Beacon (f to finish): ")
            if userModule is 'f':
                break
            num = int(userModule[0])
            moduleType = userModule[1]
            if moduleType not in Module.moduleTypes:
                print(moduleType + " is not recognized. Try again.")
                continue
            level = int(userModule[2])

            moduleName = Module.type2name(moduleType) + " Module " + str(level)
            for d in range(num):
                self.addBeaconModule(itemDict[moduleName])

    def addBuildingModule(self, module: Module):
        if not self.recipe.allowsProd and module.productivityEffect != 0:
            warnings.warn("This recipe does not allow productivity modules.")
            return False
        if len(self.buildingModules) < self.building.moduleSlots:
            self.buildingModules.append(module)
        else:
            warnings.warn("Building is already full of modules")
            return False

        return True

    def addBeaconModule(self, module: Module):
        if module.productivityEffect == 0:
            self.beaconModules.append(module)
        else:
            warnings.warn("Cannot add productivity to beacons")
            return False

        return True

    def removeBeaconModule(self, module: Module):
        name = module.name
        found = False
        for mod in self.buildingModules:
            n = mod.name
            if name == n:
                self.buildingModules.remove(module)
                found = True
                break
        if not found:
            warnings.warn("Specified module was not found")
            return False

        return True

    def removeBuildingModule(self, module: Module):
        name = module.name
        found = False
        for mod in self.beaconModules:
            n = mod.name
            if name == n:
                self.beaconModules.remove(module)
                found = True
                break
        if not found:
            warnings.warn("Specified module was not found")

    def calculateTotalProductivityBonus(self):
        bonus = 0
        for module in self.buildingModules:
            bonus += module.productivityEffect
        return bonus


    def calculateTotalSpeedBonus(self):
        bonus = 0
        for module in self.beaconModules:
            bonus += module.speedEffect/2
        for module in self.buildingModules:
            bonus += module.speedEffect
        return bonus

    def calculateTotalPowerBonus(self):
        bonus = 0
        for module in self.beaconModules:
            bonus += module.powerEffect/2
        for module in self.buildingModules:
            bonus += module.powerEffect
        return bonus

    def calculateInputsForOneBuilding(self):
        """
        This calculates the amount of inputs required to keep one machine working fully
        Q = B(N/T)(1+S)
        Q = Number of inputs required per second (Hz)
        B = base crafting time of the building (s)
        N = Number of items required by the recipe (unitless)
        T = time of the recipe (s)
        S + speed bonus (unitless)
        :return: IngredientList containing Q for every item in the input ingredientList of the recipe
        """
        B = self.building.craftingSpeed
        T = self.recipe.craftingTime
        S = self.calculateTotalSpeedBonus()
        inputIngredientList = IngredientList()
        for ingredient in self.recipe.getInputs():
            name = ingredient.name
            N = ingredient.amount
            Q = B*N/T*(1+S)
            inputIngredientList.addIngredient(Ingredient(name, Q))
        return inputIngredientList

    def calculateOutputsFromOneBuilding(self):
        """
        This calculates the amount of outputs produced per second, assuming 1 machine working.
        Q = B(N/T)(1 + S)(1 + P)
        Q = number of items produced by one machine per second
        B = base crafting time of the building
        N = number of items produced by the recipe
        T = time of recipe
        S = speed bonus
        P = productivity bonus
        :return: IngredientList containing Q for every item in the output ingredientList of the recipe
        """
        T = self.recipe.craftingTime
        B = self.building.craftingSpeed
        S = self.calculateTotalSpeedBonus()
        P = self.calculateTotalProductivityBonus()
        outputIngredientList = IngredientList()
        for key in self.recipe.outputs:
            ingredient = self.recipe.outputs[key]
            name = ingredient.name
            N = ingredient.amount
            Q = B*N/T*(1+S)*(1+P)
            outputIngredientList.addIngredient(Ingredient(name, Q))
        return outputIngredientList

    def calculateRequiredBuildingsForDesiredOutput(self):
        """
        Calculates the amount of machines required to produce the desired ingredient at the desired rate, using the
        modules that are currently installed.
        :return:
        """
        # Calculate the amount of the desired ingredient produced by one building
        ingredientName = self.desiredIngredient.name
        outputsProduced = self.calculateOutputsFromOneBuilding()
        desiredProduced = outputsProduced[ingredientName].amount

        # Grab the desired amount produced
        desiredAmount = self.desiredIngredient.amount

        # Solve for the total number of buildings needed
        numBuildings = desiredAmount/desiredProduced
        return numBuildings

    def calculateRequiredInputsForDesiredOutput(self):
        """
        Calculates the total input IngredientList needed to craft the desired output
        :return:
        """
        inputIngredientList = self.calculateInputsForOneBuilding()
        numBuildings = self.calculateRequiredBuildingsForDesiredOutput()
        for ingredient in inputIngredientList.getIngredients():
            inputIngredientList[ingredient.name].amount *= numBuildings

        return inputIngredientList

    def calculateTotalOutputsProduced(self):
        """
        Calculates the total outputs produced when crafting at the desired rate
        :return:
        """
        outputIngredientList = self.calculateOutputsFromOneBuilding()
        numBuildings = self.calculateRequiredBuildingsForDesiredOutput()
        for ingredient in outputIngredientList.getIngredients():
            outputIngredientList[ingredient.name].amount *= numBuildings
        return outputIngredientList

if __name__ == "__main__":
    # from item import Item
    # from ingredient_list import IngredientList
    # from module import Module
    # from item_dictionary import itemDict
    # from recipe_dictionary import recipeDict

    # Define the Output I want to produce
    desiredIngredient = Ingredient("Logistic Science Pack", 1)

    # Define the recipe we are working with
    myRecipe = recipeDict["2x Logistic Science Pack"]

    # Define the building we are working with
    myBuilding = itemDict["Assembling Machine 3"]

    myPlan = Plan(desiredIngredient, myRecipe, myBuilding)

    for i in range(4):
        myPlan.addBuildingModule(itemDict["Productivity Module 3"])
    for i in range(8):
        myPlan.addBeaconModule(itemDict["Speed Module 3"])
    for i in range(0):
        myPlan.addBeaconModule(itemDict['Efficiency Module 3'])

    # myPlan = Plan(desiredIngredient)
    # myPlan.promptUser()

    print(myPlan)
