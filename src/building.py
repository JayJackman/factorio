"""
Filename: building.py
Date Created: 1/7/2021
A building is a special item that has module slots and a size. It also has crafting speed and power consumption.
"""

from item import Item

class Building(Item):
    def __init__(self, name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath=None):
        super(Building, self).__init__(name, stackSize, recipes, imageFilePath)
        self.moduleSlots = moduleSlots
        self.craftingSpeed = craftingSpeed
        self.consumption = powerConsumption

    def __str__(self):
        toReturn = "Building: " + self.name + "\n"
        toReturn += "Stack Size: " + str(self.stackSize) + "\n"
        toReturn += "Module Slots: " + str(self.moduleSlots) + "\n"
        toReturn += "Crafting Speed: " + str(self.craftingSpeed) + "\n"
        toReturn += "Power Consumption: " + str(self.consumption) + " KW\n"
        return toReturn


if __name__ == "__main__":
    myBuilding = Building("School", 100, 4, 1.2, 300)
    print(myBuilding)