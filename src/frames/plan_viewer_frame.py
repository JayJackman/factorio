"""
Filename: plan_viewer_frame.py
Date Created: 6/4/2021
"""

import tkinter as tk

from planner_tree import PlanNode
import utils
from plan import Plan
from building import Building

# Import the subframe classes
from frames.recipe_selector_frame import RecipeSelectorFrame
from frames.statistics_frame import StatisticsFrame
from frames.beacon_selector_frame import BeaconSelectorFrame as BeaconFrame
from frames.building_selector_frame import BuildingSelectorFrame as BuildingFrame
from frames.desired_ingredient_frame import DesiredIngredientFrame


class PlanViewerFrame(tk.Frame):
    def __init__(self, parent, planNode: PlanNode):
        tk.Frame.__init__(self, parent)

        self.saveCallbackFunction = utils.emptyCallback

        # self.configure(bg='black')

        self.planNode = planNode
        self.newPlan = Plan.copy(self.planNode.plan)

        """
        Set up the Configurator Frame
        """
        self.configuratorFrame = tk.Frame(self)
        self.configuratorFrame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        """
        Set up the Desired Ingredient Frame
        """
        isRoot = True if self.planNode.parent is None else False
        self.desiredIngredientFrame = DesiredIngredientFrame(self.configuratorFrame,
                                                             self.planNode.plan.desiredIngredient, isRoot)
        self.desiredIngredientFrame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.desiredIngredientFrame.configureCallback(self.onDesiredIngredientChanged)

        """
        Set up the Recipe Selector Frame
        """
        self.recipeSelectorFrame = RecipeSelectorFrame(self.configuratorFrame, self.planNode.plan)
        self.recipeSelectorFrame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.recipeSelectorFrame.configureCallback(self.onRecipeChanged)

        """
        Set up the Building Selector Frame
        """
        self.buildingFrame = BuildingFrame(self.configuratorFrame, self.planNode.plan)
        self.buildingFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.buildingFrame.configureCallback(self.onBuildingChanged)

        """
        Set up the Beacon Frame
        """
        self.beaconFrame = BeaconFrame(self.configuratorFrame, self.planNode.plan)
        self.beaconFrame.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
        self.beaconFrame.configureCallback(self.onBeaconModuleChanged)

        """
        Set up the Statistics Viewer Frame
        """
        self.statisticsFrame = StatisticsFrame(self, self.planNode.plan)
        self.statisticsFrame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        """
        Set up the Save/Cancel Frame
        """
        self.saveFrame = tk.Frame(self, borderwidth=1, relief='groove')
        self.saveFrame.grid(row=2, column=1, padx=5, pady=5, sticky='se')
        self.saveFrame.columnconfigure([0, 1], weight=1)

        # Add the save button
        self.saveButton = tk.Button(self.saveFrame, text="Save", command=self.onSaveButtonClicked)
        self.saveButton.grid(row=0, column=1, padx=5, pady=5, sticky='se')

        # Add the cancel button
        self.cancelButton = tk.Button(self.saveFrame, text="Cancel", command=self.onCancelButtonClicked)
        self.cancelButton.grid(row=0, column=0, padx=5, pady=5, sticky='se')

    """
    Event Handlers
    """

    def onDesiredIngredientChanged(self, ingredient):
        self.newPlan = Plan(desired=ingredient)

        self.recipeSelectorFrame.refresh(self.newPlan)
        self.buildingFrame.refresh(self.newPlan)
        self.beaconFrame.refresh(self.newPlan)
        self.refreshStatisticsFrame()

    def onRecipeChanged(self, recipe):
        self.newPlan.recipe = recipe

        self.refreshStatisticsFrame()

    def onBuildingChanged(self, building: Building, modules: list):
        self.newPlan.building = building
        self.newPlan.buildingModules = modules.copy()

        self.refreshStatisticsFrame()

    def onBeaconModuleChanged(self, modules):
        self.newPlan.beaconModules = modules.copy()

        self.refreshStatisticsFrame()

    def onSaveButtonClicked(self):
        if self.isDirty():
            self.planNode = self.saveCallbackFunction(self.planNode, self.newPlan)
            self.newPlan = Plan.copy(self.planNode.plan)
        else:
            self.saveCallbackFunction(self.planNode, None)

        # print(self.planNode.getTotalInputsAndOutputs())

    def onCancelButtonClicked(self):
        self.newPlan = Plan.copy(self.planNode.plan)
        # print(self.newPlan)
        self.desiredIngredientFrame.refresh(self.planNode.plan)
        self.recipeSelectorFrame.refresh(self.planNode.plan)
        self.buildingFrame.refresh(self.planNode.plan)
        self.beaconFrame.refresh(self.planNode.plan)
        self.statisticsFrame.refresh(self.planNode.plan)

    def refreshStatisticsFrame(self):
        self.statisticsFrame.refresh(self.newPlan)

    """
    Utility Functions
    """

    def getMinWidth(self):
        self.configuratorFrame.update_idletasks()
        self.saveFrame.update_idletasks()
        self.beaconFrame.update_idletasks()
        self.buildingFrame.update_idletasks()
        self.statisticsFrame.update_idletasks()
        self.desiredIngredientFrame.update_idletasks()
        self.recipeSelectorFrame.update_idletasks()

        return self.desiredIngredientFrame.winfo_width() + self.recipeSelectorFrame.winfo_width() + self.statisticsFrame.winfo_width()

    def configureSaveCallback(self, callbackFunction):
        self.saveCallbackFunction = callbackFunction

    def isDirty(self):
        if self.newPlan.recipe != self.planNode.plan.recipe:
            return True
        if self.newPlan.building != self.planNode.plan.building:
            return True
        if self.newPlan.desiredIngredient.amount != self.planNode.plan.desiredIngredient.amount:
            return True
        if len(self.newPlan.beaconModules) != len(self.planNode.plan.beaconModules):
            return True
        for m1, m2 in zip(self.newPlan.beaconModules, self.planNode.plan.beaconModules):
            if m1 != m2:
                return True
        for m1, m2 in zip(self.newPlan.buildingModules, self.planNode.plan.buildingModules):
            if m1 != m2:
                return True
        return False


if __name__ == '__main__':
    from ingredient import Ingredient
    from planner_tree import PlannerTree

    root = tk.Tk()
    myIngredient = Ingredient('Iron Gear Wheel', 5)
    myTree = PlannerTree(myIngredient)

    planViewerFrame = PlanViewerFrame(root, myTree.root)
    planViewerFrame.grid(row=0, column=0)

    root.mainloop()
