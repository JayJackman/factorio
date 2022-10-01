"""
Filename: beacon_selector_frame_SE.py
Date Created: 6/26/2021
"""

import tkinter as tk
from functools import partial

import utils
from plan import Plan
from module import Module
from item_dictionary import itemDict


class BeaconSelectorFrame(tk.Frame):
    def __init__(self, parent, plan: Plan):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.module_changed_callback_function = utils.emptyCallback

        self.beaconModules = plan.beaconModules.copy()

        # This frame lets you select the kind of beacon you're using
        self.beaconSelectorFrame = tk.Frame(self)
        self.beaconSelectorFrame.grid(row=0, column=0, padx=5, pady=5)

        # Set up the Beacon Icon Label
        self.beaconIcon = utils.getIcon('resources/images/tiered/basic-beacon.png') # TODO: This is hardcoded
        self.beaconIconLabel = tk.Label(self.beaconSelectorFrame, image=self.beaconIcon)
        self.beaconIconLabel.grid(row=0, column=0, padx=5, pady=5)

        # Set up the Beacon Dropdown Menu
        beaconOptions = ['Basic Beacon'] # TODO: Hardcoded
        selectedBeacon = tk.StringVar(self)
        selectedBeacon.set('Basic Beacon')
        self.beaconOptionMenu = tk.OptionMenu(self.beaconSelectorFrame, selectedBeacon, *beaconOptions)
        self.beaconOptionMenu.grid(row=0, column=1, padx=5, pady=5)

        # This frame will be populated with selectors for all the modules
        self.beaconModuleFrame = tk.Frame(self)
        self.beaconModuleFrame.grid(row=1, column=0, padx=5, pady=5)

        # Create a module configurator for each module slot
        self.beaconModuleIcons = []
        self.beaconModuleIconLabels = []
        self.beaconModuleOptionMenus = []
        self.selectedModules = []
        self.beaconModuleFrames = []
        for i in range(8): # TODO: Hard coded
            row = i//4
            col = i % 4
            moduleFrame = tk.Frame(self.beaconModuleFrame)
            moduleFrame.grid(row=row, column=col, padx=5, pady=5)
            self.beaconModuleFrames.append(moduleFrame)

            moduleIcon = utils.getIcon(self.beaconModules[i].imageFile)
            self.beaconModuleIcons.append(moduleIcon)
            moduleIconLabel = tk.Label(moduleFrame, image=moduleIcon)
            moduleIconLabel.grid(row=0, column=0, padx=5, pady=5)
            self.beaconModuleIconLabels.append(moduleIconLabel)

            moduleOptions = ['None', 'E-1', 'E-2', 'E-3', 'S-1', 'S-2', 'S-3']
            selectedModule = tk.StringVar(moduleFrame)
            selectedModule.set('None')
            self.selectedModules.append(selectedModule)
            moduleOptionMenu = tk.OptionMenu(moduleFrame, selectedModule, *moduleOptions,
                                             command=partial(self.onBeaconOptionMenuChanged, i))
            moduleOptionMenu.grid(row=1, column=0, padx=5, pady=5)
            self.beaconModuleOptionMenus.append(moduleOptionMenu)

    def onBeaconOptionMenuChanged(self, index: int, moduleType: str):
        moduleName = Module.moduleType2moduleName(moduleType)
        module = itemDict[moduleName]
        self.beaconModules[index] = module
        self.beaconModuleIcons[index] = utils.getIcon(module.imageFile)
        self.beaconModuleIconLabels[index].configure(image=self.beaconModuleIcons[index])

        self.module_changed_callback_function(self.beaconModules)

    def configureCallback(self, callbackFunction):
        self.module_changed_callback_function = callbackFunction

    def refresh(self, plan: Plan):
        # TODO: Eventually we need to add beacon type
        for i, module in enumerate(plan.beaconModules):
            self.beaconModules[i] = module
            self.beaconModuleIcons[i] = utils.getIcon(module.imageFile)
            self.beaconModuleIconLabels[i].configure(image=self.beaconModuleIcons[i])

            self.selectedModules[i].set(Module.moduleName2moduleType(module.name))