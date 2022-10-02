"""
Filename: statistics_frame.py
Date Created: 6/26/2021
"""

import tkinter as tk

from plan import Plan
from frames.ingredient_frame import IngredientFrame
from ingredient import Ingredient

class StatisticsFrame(tk.Frame):
    def __init__(self, parent, plan: Plan):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.plan = plan

        """
        Set up the frame that tracks the total amounts of inputs required to produce the deisred ingredient
        """
        self.inputFrame = tk.Frame(self, borderwidth=1, relief='groove')
        self.inputFrame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.inputFrame.columnconfigure(0, weight=1)

        # Label that simply says "Required Inputs"
        self.inputLabel = tk.Label(self.inputFrame, text="Required Inputs:")
        self.inputLabel.grid(row=0, column=0)

        # Need to make an icon/label pair for each ingredient of the recipe
        self.inputIngredientFrames = []

        """
        Set up the frame that tracks the total amounts of outputs produced
        """
        self.outputFrame = tk.Frame(self, borderwidth=1, relief='groove')
        self.outputFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.outputFrame.columnconfigure(0, weight=1)

        # Label that simply says "Produced Outputs"
        self.outputLabel = tk.Label(self.outputFrame, text='Produced Outputs:')
        self.outputLabel.grid(row=0, column=0)

        # Need to make an icon/label for each ingredient
        self.outputIngredientFrames = []

        """
        Set up the frame that tracks the amount of machines needed
        """
        self.numBuildingsFrame = tk.Frame(self, borderwidth=1, relief='groove')
        self.numBuildingsFrame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.numBuildingsFrame.columnconfigure(0, weight=1)

        # Label that simply says "Required Buildings"
        self.numBuildingsLabel = tk.Label(self.numBuildingsFrame, text="Required Buildings")
        self.numBuildingsLabel.grid(row=0, column=0)

        self.numBuildingsSubFrame = IngredientFrame(self.numBuildingsFrame, Ingredient(self.plan.building.name, self.plan.calculateRequiredBuildingsForDesiredOutput()), asRate=False)

        self.refresh(self.plan)

    def refresh(self, plan: Plan):
        """
        Refreshes all of our display labels with a new plan
        :param plan: the new Plan
        """
        self.plan = plan

        # Delete old labels
        for frame in self.inputIngredientFrames:
            frame.destroy()
        for frame in self.outputIngredientFrames:
            frame.destroy()

        # Refresh inputs
        self.inputIngredientFrames = []
        for i, ingredient in enumerate(self.plan.calculateRequiredInputsForDesiredOutput().getIngredients()):
            self.inputIngredientFrames.append(IngredientFrame(self.inputFrame, ingredient))
            self.inputIngredientFrames[i].grid(row=i + 1, column=0, padx=5, pady=5)

        # Refresh outputs
        self.outputIngredientFrames = []
        for i, ingredient in enumerate(self.plan.calculateTotalOutputsProduced().getIngredients()):
            self.outputIngredientFrames.append(IngredientFrame(self.outputFrame, ingredient))
            self.outputIngredientFrames[i].grid(row=i + 1, column=0, padx=5, pady=5)

        # Refresh num buildings
        self.numBuildingsSubFrame.refresh(Ingredient(self.plan.building.name, self.plan.calculateRequiredBuildingsForDesiredOutput()))
        self.numBuildingsSubFrame.grid(row=1, column=0)
