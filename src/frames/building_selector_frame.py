"""
Filename: building_selector_frame.py
Date Created: 6/26/2021
"""

import tkinter as tk
from functools import partial

import utils as utils
from plan import Plan
from module import Module
from dictionaries.items import itemDict

class BuildingSelectorFrame(tk.Frame):
    def __init__(self, parent, plan: Plan):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.changed_callback_function = utils.emptyCallback

        self.recipe = plan.recipe
        self.building = plan.building
        self.modules = plan.buildingModules.copy()

        # Set up the Frame that lets you choose building type
        self.buildingTypeFrame = tk.Frame(self)
        self.buildingTypeFrame.grid(row=0, column=0, padx=5, pady=5)

        # Set up the Building Icon Label
        self.buildingIcon = utils.getIcon(self.building.imageFile)
        self.buildingIconLabel = tk.Label(self.buildingTypeFrame, image=self.buildingIcon)
        self.buildingIconLabel.grid(row=0, column=0, padx=5, pady=5)

        # Set up the Building Dropdown Menu
        buildingOptions = plan.recipe.buildings
        self.selectedBuilding = tk.StringVar(self)
        self.selectedBuilding.set(plan.building.name)
        self.buildingOptionMenu = tk.OptionMenu(self.buildingTypeFrame, self.selectedBuilding, *buildingOptions, command=self.onBuildingChanged)
        self.buildingOptionMenu.grid(row=0, column=1, padx=5, pady=5)

        # Set up the Building Module configurators
        self.mainModuleFrame = tk.Frame(self)
        self.mainModuleFrame.grid(row=1, column=0, padx=5, pady=5)

        self.moduleIcons = []
        self.moduleIconLabels = []
        self.moduleOptionMenus = []
        self.moduleFrames = []
        self.createModuleFrame(self.building)

    def configureCallback(self, callbackFunction):
        self.changed_callback_function = callbackFunction

    def createModuleFrame(self, building):
        for frame in self.moduleFrames:
            frame.destroy()
        self.moduleIcons = []
        self.moduleIconLabels = []
        self.moduleOptionMenus = []
        self.moduleFrames = []
        for i in range(building.moduleSlots):
            moduleFrame = tk.Frame(self.mainModuleFrame)
            moduleFrame.grid(row=0, column=i, padx=5, pady=5)
            self.moduleFrames.append(moduleFrame)

            # Set up the icon for the module
            moduleIcon = utils.getIcon(self.modules[i].imageFile)
            self.moduleIcons.append(moduleIcon)
            moduleIconLabel = tk.Label(moduleFrame, image=moduleIcon)
            moduleIconLabel.grid(row=0, column=0, padx=5, pady=5)
            self.moduleIconLabels.append(moduleIconLabel)

            # Set up the dropdown menu for the module
            moduleOptions = ['None', 'E-1', 'E-2', 'E-3', 'S-1', 'S-2', 'S-3']
            if self.recipe.allowsProd:
                moduleOptions += ['P-1', 'P-2', 'P-3']
            selectedModule = tk.StringVar(moduleFrame)
            selectedModule.set(Module.moduleName2moduleType(self.modules[i].name))
            moduleOptionMenu = tk.OptionMenu(moduleFrame, selectedModule, *moduleOptions,
                                             command=partial(self.onBuildingModuleChanged, i))
            moduleOptionMenu.grid(row=1, column=0, padx=5, pady=5)
            self.moduleOptionMenus.append(moduleOptionMenu)

    def onBuildingChanged(self, buildingName):
        if itemDict[buildingName] == self.building:
            return
        # Recreate the module frame to adapt for changing number of modules allowed
        self.mainModuleFrame.destroy()
        self.mainModuleFrame = tk.Frame(self)
        self.mainModuleFrame.grid(row=1, column=0, padx=5, pady=5)

        self.building = itemDict[buildingName]

        # Reset the modules
        self.modules = Plan.makeEmptyModuleList(self.building.moduleSlots)

        # Recreate the module frame
        self.createModuleFrame(self.building)

        self.buildingIcon = utils.getIcon(self.building.imageFile)
        self.buildingIconLabel.configure(image=self.buildingIcon)

        self.changed_callback_function(self.building, self.modules)

    def onBuildingModuleChanged(self, index: int, moduleType: str):
        moduleName = Module.moduleType2moduleName(moduleType)
        module = itemDict[moduleName]
        self.modules[index] = module
        self.moduleIcons[index] = utils.getIcon(module.imageFile)
        self.moduleIconLabels[index].configure(image=self.moduleIcons[index])

        self.changed_callback_function(self.building, self.modules)

    def refresh(self, plan: Plan):
        # self._refresh(plan.building, plan.buildingModules.copy())
        self.building = plan.building
        self.modules = plan.buildingModules.copy()

        self.buildingIcon = utils.getIcon(plan.building.imageFile)
        self.buildingIconLabel.configure(image=self.buildingIcon)

        self.createModuleFrame(self.building)

        buildingOptions = plan.recipe.buildings
        self.selectedBuilding.set(self.building.name)
        self.buildingOptionMenu.destroy()
        self.buildingOptionMenu = tk.OptionMenu(self.buildingTypeFrame, self.selectedBuilding, *buildingOptions, command=self.onBuildingChanged)
        self.buildingOptionMenu.grid(row=0, column=1, padx=5, pady=5)