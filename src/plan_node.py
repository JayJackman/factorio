"""
Filename: plan_node.py
Date Created: 5/31/2021
"""
from item import Item
from plan import Plan
from recipe import Recipe
from tree_graph import Node
from ingredient_list import IngredientList
from ingredient import Ingredient

from typing import List


class PlanNode(Node):
    def __init__(self, parent=None, plan: Plan = None):
        Node.__init__(self, plan, parent)
        self.plan = plan  # This is the same as obj, but makes more sense to call it a plan here

        self.children: List[PlanNode] = self.children

        self.labelText = self.plan.desiredIngredient.name

    def getTotalInputsAndOutputs(self):
        def recursiveCall(node: PlanNode, returnList: IngredientList):
            # Add the outputs to the return list
            outputs = node.plan.calculateTotalOutputsProduced()
            for ingredient in outputs.getIngredients():
                if ingredient.name in returnList.keys():
                    newAmount = ingredient.amount + returnList[ingredient.name].amount
                    returnList[ingredient.name] = Ingredient(ingredient.name, newAmount)
                else:
                    returnList.addIngredient(ingredient)
                if abs(returnList[ingredient.name].amount) < 0.00001:
                    del returnList[ingredient.name]

            # Subtract the inputs from the return list
            if node.isLeaf():
                ingredient = node.plan.desiredIngredient
                if ingredient.name in returnList.keys():
                    newAmount = returnList[ingredient.name].amount - ingredient.amount
                    returnList[ingredient.name] = Ingredient(ingredient.name, newAmount)
                else:
                    returnList.addIngredient(Ingredient(ingredient.name, -ingredient.amount))
            else:
                inputs = node.plan.calculateRequiredInputsForDesiredOutput()
                for ingredient in inputs.getIngredients():
                    if ingredient.name in returnList.keys():
                        newAmount = returnList[ingredient.name].amount - ingredient.amount
                        returnList[ingredient.name] = Ingredient(ingredient.name, newAmount)
                    else:
                        returnList.addIngredient(Ingredient(ingredient.name, -ingredient.amount))
                    if abs(returnList[ingredient.name].amount) < 0.00001:
                        del returnList[ingredient.name]

            # Go through the children
            for child in node.children:
                returnList = recursiveCall(child, returnList)

            return returnList

        return recursiveCall(self, IngredientList())

    def applyRawIngredient(self, ingredient: Item):
        def recursiveCall(node: PlanNode):
            # if the node is the item to turn into raw, delete children and change recipe to raw
            if node.plan.desiredIngredient.name == ingredient.name:
                while len(node.children) > 0:
                    node.children[0].delete()
                node.plan.recipe = Recipe.getEmptyRecipe(node.plan.desiredIngredient)
                return
            # otherwise, look through all children to see if we find the raw item
            for child in node.children:
                recursiveCall(child)

        recursiveCall(self)

    def __str__(self):
        return str(self.plan.desiredIngredient.amount) + 'x ' + self.plan.desiredIngredient.name
