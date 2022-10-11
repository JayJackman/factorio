"""
Filename: configurator_frame.py
Date Created: 10/10/2022
"""

"""
Ideas:
1. apply module to all buildings that can accept it
2. remove all modules
3. apply building type to all recipes that accept it
4. add X number of beacon modules to all recipes
5. clear all beacon modules
"""


import tkinter as tk
from functools import partial

from planner_tree import PlanNode
import utils
from plan import Plan
from building import Building
from dictionaries.items import BUILDINGS, itemDict

# Import the subframe classes
from frames.recipe_selector_frame import RecipeSelectorFrame
from frames.statistics_frame import StatisticsFrame
from frames.beacon_selector_frame import BeaconSelectorFrame as BeaconFrame
from frames.building_selector_frame import BuildingSelectorFrame as BuildingFrame
from frames.desired_ingredient_frame import DesiredIngredientFrame


class ConfiguratorFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # self.configure(bg='black')
        self.label = tk.Label(self, text='Global Configuration')
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        """
        Set up the Building Selector Button
        """
        self.buildingSelectorFrame = tk.Frame(self, borderwidth=1, relief='raised')
        self.buildingSelectorFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        # Holds the building icon and the optionMenu
        self.buildingDropdownFrame = tk.Frame(self.buildingSelectorFrame)
        self.buildingDropdownFrame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        # Set up the icon for the building
        self.buildingIcon = utils.getEmptyImageIcon()
        self.buildingLabel = tk.Label(self.buildingDropdownFrame, image=self.buildingIcon)
        self.buildingLabel.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        # Set up the Option menu
        self.selectedBuildingStringVar = tk.StringVar(self.buildingSelectorFrame)
        self.selectedBuildingStringVar.set('Select Building')
        self.buildingOptionMenu = tk.OptionMenu(self.buildingDropdownFrame, self.selectedBuildingStringVar, *BUILDINGS,
                                                command = self.onBuildingSelected)
        self.buildingOptionMenu.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        # Set up the apply button
        self.applyBuildingButton = tk.Button(self.buildingSelectorFrame, text='Apply Building', command=self.onApplyBuilding)
        self.applyBuildingButton.grid(row=0, column=1, padx=5, pady=5)
        self.buildingChangedCallback = utils.emptyCallback

    def onBuildingSelected(self, buildingName):
        building = itemDict[buildingName]
        self.buildingIcon = utils.getIcon(building.imageFile)
        self.buildingLabel.configure(image=self.buildingIcon)

    def configureBuildingCallback(self, callback):
        self.buildingChangedCallback = callback

    def onApplyBuilding(self):
        if self.selectedBuildingStringVar.get() == 'Select Building':
            return

        building = itemDict[self.selectedBuildingStringVar.get()]
        self.buildingChangedCallback(building)