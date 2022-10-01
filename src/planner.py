"""
Filename: planner.py
Date Created: 1/10/2021
A Planner holds many Plans. It accepts multiple desired Ingredients to produce, then recursively creates plans for each
required input Ingredient. It consolidates all the required input Ingredients and the final output Ingredients
"""
import numpy as np

from plan import Plan
from ingredient_list import IngredientList

class Planner():
    def __init__(self, desiredIngredients: IngredientList = []):
        self.desiredIngredientList = desiredIngredients
        self.plans = []
        self.createPlans(self.desiredIngredientList)

    def createPlans(self, ingredientList):
        """
        Recursively creates plans for a list of ingredients. Adds the plans to a master list as it goes
        :param ingredientList: a list of desired ingredients
        :return:
        """
        for ingredient in ingredientList.getIngredients():
            finish = input("Create plan for " + ingredient.name + " ? (y/n):")
            if finish is not 'y':
                continue
            plan = Plan(ingredient)
            plan.promptUser(ingredient)
            self.plans.append(plan)
            requiredInputs = plan.calculateRequiredInputsForDesiredOutput()
            self.createPlans(requiredInputs)

    def getTotalInputIngredientList(self):
        """
        Calculates the total amount of raw ingredients needed to produce the desired outputs. Note that "raw ingredient"
        can be defined by the user by when they stop making plans. Intermediate ingredients are not included in this
        list
        :return: IngredientList that holds the total raw ingredients needed to produce the desired outputs
        """
        totalIngredientList = IngredientList()
        for ingredient in self.desiredIngredientList.getIngredients():
            if ingredient.name in totalIngredientList:
                totalIngredientList[ingredient.name].amount += ingredient.amount
            else:
                totalIngredientList.addIngredient(ingredient)
        for plan in self.plans:
            inputIngredientList = plan.calculateRequiredInputsForDesiredOutput()
            for ingredient in inputIngredientList.getIngredients():
                if ingredient.name in totalIngredientList:
                    totalIngredientList[ingredient.name].amount += ingredient.amount
                else:
                    totalIngredientList.addIngredient(ingredient)

            outputIngredientList = plan.calculateTotalOutputsProduced()
            for ingredient in outputIngredientList.getIngredients():
                if ingredient.name in totalIngredientList:
                    totalIngredientList[ingredient.name].amount -= ingredient.amount
                else:
                    totalIngredientList.addIngredient(Ingredient(ingredient.name, -ingredient.amount))

        # Prune the ingredients that are near 0
        for ingredient in totalIngredientList.getIngredients():
            if np.abs(ingredient.amount) < 0.0000000001:
                del totalIngredientList[ingredient.name]
        return totalIngredientList


if __name__ == "__main__":
    from ingredient import Ingredient
    ingredientList = IngredientList()
    ingredientList.addIngredient(Ingredient("Plastic Bar", 1))

    planner = Planner(ingredientList)
    print(planner.getTotalInputIngredientList())
