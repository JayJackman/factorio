"""
Filename: total_statistics_frame.py
Date Created: 6/27/2021
"""

import tkinter as tk

from plan_node import PlanNode
from frames.ingredient_frame import IngredientFrame
from ingredient import Ingredient

class TotalStatisticsFrame(tk.Frame):
    def __init__(self, parent, planNode: PlanNode):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.planNode = planNode

        """
        Set up the frame that tracks the total amount of inputs for the plan 
        """
        self.inputSubFrame = tk.Frame(self, borderwidth=1, relief='groove')
        self.inputSubFrame.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.inputSubFrame.columnconfigure(0, weight=1)

        # Label that simply says "Total Inputs"
        self.inputLabel = tk.Label(self.inputSubFrame, text="Total Inputs:")
        self.inputLabel.grid(row=0, column=0)

        # Need to make an icon/label pair for each ingredient of the recipe
        self.inputIngredientFrames = []

        """
        Set up the frame that tracks the total amount of outputs for the plan
        """
        self.outputSubFrame = tk.Frame(self, borderwidth=1, relief='groove')
        self.outputSubFrame.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.outputSubFrame.columnconfigure(0, weight=1)

        # Label that simply says "Total Outputs"
        self.outputLabel = tk.Label(self.outputSubFrame, text="Total Outputs:")
        self.outputLabel.grid(row=0, column=0)

        # Need to make an icon/label pair for each ingredient of the recipe
        self.outputIngredientFrames = []

        self.refresh(self.planNode)

    def refresh(self, planNode: PlanNode):
        self.planNode = planNode
        for frame in self.inputIngredientFrames:
            frame.destroy()
        for frame in self.outputIngredientFrames:
            frame.destroy()

        ingredients = self.planNode.getTotalInputsAndOutputs()

        self.inputIngredientFrames = []
        self.outputIngredientFrames = []
        numInputs = 0
        numOutputs = 0
        for ingredient in ingredients.getIngredients():
            if ingredient.amount < 0:
                # Here, we have an input
                ingredientFrame = IngredientFrame(self.inputSubFrame, Ingredient(ingredient.name, -ingredient.amount))
                ingredientFrame.grid(row=(numInputs//7), column=numInputs % 7 + 1, padx=5, pady=5)
                self.inputIngredientFrames.append(ingredientFrame)
                numInputs += 1
            else:
                # Here, we have an output
                ingredientFrame = IngredientFrame(self.outputSubFrame, ingredient)
                ingredientFrame.grid(row=(numOutputs//7), column=numOutputs % 7 + 1, padx=5, pady=5)
                self.outputIngredientFrames.append(ingredientFrame)
                numOutputs += 1
