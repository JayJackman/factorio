"""
Filename: beacon_selector_frame_vanilla.py
Date Created: 9/29/2022
"""

import tkinter as tk
from functools import partial

import utils
from plan import Plan
from module import Module
from item_dictionary import itemDict

class ModuleEditorFrame(tk.Frame):
    def __init__(self, parent, module: Module, num: int = 1):
        tk.Frame.__init__(self, parent, borderwidth=1)

        self.amount = num
        self.module = module

        self.changed_callback_function = utils.emptyCallback()

        self.icon = utils.getIcon(module.imageFile)
        self.iconLabel = tk.Label(self, image=self.icon)
        self.iconLabel.grid(row=0, column=0, padx=5, pady=5)

        self.textField = tk.Entry(self)
        self.textField.insert(0, self.amount)
        self.textField.grid(row=0, column=1, padx=5, pady=5)
        self.textField.bind('<Return>', self.handleEnter)

        self.deleteButton = tk.Button(self, text='X', bg='red', command=self.handleDelete)
        self.deleteButton.grid(row=0, column=2, padx=5, pady=5)

    def configureChangedCallback(self, callback):
        self.changed_callback_function = callback

    def handleEnter(self, event):
        amount = self.textField.get()
        self.amount = int(amount) if amount.isnumeric() else 0
        self.textField.delete(0, 'end')
        self.textField.insert(0, self.amount)
        self.changed_callback_function(self.module.name, self.amount)

    def handleDelete(self):
        self.amount = -1
        self.changed_callback_function(self.module.name, -1)


class BeaconSelectorFrame(tk.Frame):
    def __init__(self, parent, plan: Plan):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.module_changed_callback_function = utils.emptyCallback

        # Stretch horizontally
        self.columnconfigure(0, weight=1)

        # This frame lets you select the kind of beacon you're using
        self.beaconSelectorFrame = tk.Frame(self)
        self.beaconSelectorFrame.grid(row=0, column=0, padx=5, pady=5)

        # Set up the Beacon Icon Label
        self.beaconIcon = utils.getIcon(itemDict['Beacon'].imageFile)
        self.beaconIconLabel = tk.Label(self.beaconSelectorFrame, image=self.beaconIcon)
        self.beaconIconLabel.grid(row=0, column=0, padx=5, pady=5)

        # Set up the Beacon Dropdown Menu
        self.beaconLabel = tk.Label(self.beaconSelectorFrame, text="Beacon ")
        self.beaconLabel.grid(row=0, column=1, padx=5, pady=5)

        # This frame will be populated with selectors for all the modules
        self.beaconModuleFrame = tk.Frame(self)
        self.beaconModuleFrame.grid(row=1, column=0, padx=5, pady=5)

        # Create a module configurator for each module slot
        self.moduleFrames = []

        # TODO: Make this not hardcoded
        self.moduleOptions = ['Efficiency Module 1',
                              'Efficiency Module 2',
                              'Efficiency Module 3',
                              'Speed Module 1',
                              'Speed Module 2',
                              'Speed Module 3']
        self.usedOptions = []

        self.selectedModule = tk.StringVar(self)
        self.selectedModule.set('Add Module')
        self.moduleOptionMenu = tk.OptionMenu(self, self.selectedModule, *self.moduleOptions,
                                         command=self.handleAddModule)

        self.moduleOptionMenu.grid(row=len(self.moduleFrames)+1, column=0, padx=5, pady=5)

        beaconModules = plan.beaconModules.copy()

        self.moduleDict = {}
        for module in beaconModules:
            if module.name not in self.moduleDict.keys():
                self.moduleDict[module.name] = 1
            else:
                self.moduleDict[module.name] += 1

        # Add in each module frame
        for moduleName in self.moduleDict:
            self.handleAddModule(moduleName, self.moduleDict[moduleName])

        self.refreshTextLabel()

    def onModuleChanged(self, moduleName: str, num: int):
        if num < 0:
            del(self.moduleDict[moduleName])
            for i, moduleFrame in enumerate(self.moduleFrames):
                if moduleFrame.module.name == moduleName:
                    moduleFrame.destroy()
                    del self.moduleFrames[i]

                    self.moduleOptions.append(moduleName)
                    self.usedOptions.remove(moduleName)
                    self.moduleOptions.sort()
                    self.refreshOptionMenu()
                    break
        else:
            self.moduleDict[moduleName] = num

        self.refreshTextLabel()
        self.module_changed_callback_function(self.beaconModules())

    def beaconModules(self):
        beaconModules = []
        for name in self.moduleDict:
            for i in range(self.moduleDict[name]):
                beaconModules.append(itemDict[name])
        return beaconModules

    def numModules(self):
        count = 0
        for name in self.moduleDict:
            count += self.moduleDict[name]
        return count

    def configureCallback(self, callbackFunction):
        self.module_changed_callback_function = callbackFunction

    def handleAddModule(self, moduleName: str, num=1):
        self.moduleOptions.remove(moduleName)
        self.usedOptions.append(moduleName)

        self.refreshOptionMenu()

        # Create a new Module Editor Frame
        self.moduleDict[moduleName] = num
        moduleFrame = ModuleEditorFrame(self, itemDict[moduleName], num)
        moduleFrame.configureChangedCallback(self.onModuleChanged)
        self.moduleFrames.append(moduleFrame)

        moduleFrame.grid(row=len(self.moduleFrames), column=0, padx=5, pady=5)

        # update the position of our add module selector
        self.moduleOptionMenu.grid(row=len(self.moduleFrames) + 1, column=0, padx=5, pady=5)
        self.selectedModule.set("Add Module")

        self.refreshTextLabel()
        self.module_changed_callback_function(self.beaconModules())

    def refreshOptionMenu(self):
        # create the new options in our option menu
        menu = self.moduleOptionMenu['menu']
        menu.delete(0, 'end')
        for module in self.moduleOptions:
            menu.add_command(label=module, command=tk._setit(self.selectedModule, module, self.handleAddModule))

    def refreshTextLabel(self):
        num = self.numModules()
        if num == 0:
            txt = "Beacon"
        else:
            txt = "Beacon: " + str(-(-num//2))
        self.beaconLabel.configure(text=txt)

    def refresh(self, plan: Plan):
        while len(self.moduleFrames) > 0:
            self.moduleFrames[0].destroy()
            del self.moduleFrames[0]

        # TODO: Make this not hardcoded
        self.moduleOptions = ['Efficiency Module 1',
                              'Efficiency Module 2',
                              'Efficiency Module 3',
                              'Speed Module 1',
                              'Speed Module 2',
                              'Speed Module 3']
        self.usedOptions = []

        self.selectedModule.set('Add Module')

        beaconModules = plan.beaconModules.copy()
        self.moduleDict = {}
        for module in beaconModules:
            if module.name not in self.moduleDict.keys():
                self.moduleDict[module.name] = 1
            else:
                self.moduleDict[module.name] += 1

        # Add in each module frame
        for moduleName in self.moduleDict:
            self.handleAddModule(moduleName, self.moduleDict[moduleName])

        self.refreshTextLabel()
