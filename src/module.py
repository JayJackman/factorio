"""
Filename: module.py
Date Created: 1/7/2021
A Module can be inserted into buildings or beacons in order to alter productivity
"""
from item import Item

import warnings

class Module(Item):
    moduleTypes = ['p', 's', 'e', 'n']

    def __init__(self, name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath=None):
        super(Module,self).__init__(name, stackSize, recipes, imageFilePath)
        if moduleType not in Module.moduleTypes:
            warnings.warn("Invalid Module Type")
        self.type = moduleType
        self.productivityEffect = productivityEffect
        self.speedEffect = speedEffect
        self.powerEffect = powerEffect

    def __str__(self):
        toReturn = "Module: " + self.name + "\n"
        toReturn += "Stack Size: " + str(self.stackSize) + "\n"
        toReturn += "Productivity Effect: " + str(self.productivityEffect) + "\n"
        toReturn += "Speed Effect: " + str(self.speedEffect) + "\n"
        toReturn += "Power Effect: " + str(self.powerEffect) + "\n"
        return toReturn

    @staticmethod
    def type2name(moduleType):
        if moduleType not in moduleType:
            warnings.warn("Invalid Module Type")
        if moduleType is 'p':
            return 'Productivity'
        if moduleType is 'e':
            return 'Efficiency'
        if moduleType is 's':
            return 'Speed'
        if moduleType is 'n':
            return 'None'

    @staticmethod
    def moduleName2moduleType(moduleName):
        toReturn = ''
        words = moduleName.split()
        if words[0] == 'Empty':
            return 'None'
        elif words[0] == 'Efficiency':
            toReturn += 'E-'
        elif words[0] == 'Productivity':
            toReturn += 'P-'
        elif words[0] == 'Speed':
            toReturn += 'S-'
        toReturn += words[2]
        return toReturn

    @staticmethod
    def moduleType2moduleName(moduleType):
        """ A module Type is of the Format 'T-#' """
        toReturn = ''
        if moduleType == 'None':
            return "Empty Module"
        elif moduleType[0] == 'E' or moduleType[0] == 'e':
            toReturn += 'Efficiency Module '
        elif moduleType[0] == 'P' or moduleType[0] == 'p':
            toReturn += 'Productivity Module '
        elif moduleType[0] == 'S' or moduleType[0] == 's':
            toReturn += 'Speed Module '

        toReturn += moduleType[2]
        return toReturn


if __name__ == "__main__":
    myModule = Module("Prod mod 1", 100, 1.6, 0.1, 1)
    print(myModule)