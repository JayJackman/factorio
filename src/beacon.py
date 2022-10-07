"""
Filename: beacon.py
Date Created: 9/29/2022
"""

from item import Item


class Beacon(Item):
    def __init__(self, name, stackSize, moduleSlots, powerConsumption, stackable, recipes, imageFilePath=None):
        super(Beacon, self).__init__(name, stackSize, recipes, imageFilePath)
        self.moduleSlots = moduleSlots
        self.stackable: bool = stackable
        self.consumption = powerConsumption

    def __str__(self):
        toReturn = "Building: " + self.name + "\n"
        toReturn += "Stack Size: " + str(self.stackSize) + "\n"
        toReturn += "Module Slots: " + str(self.moduleSlots) + "\n"
        toReturn += "Stackable: " + str(self.stackable)
        toReturn += "Power Consumption: " + str(self.consumption) + " KW\n"
        return toReturn


if __name__ == "__main__":
    myBeacon = Beacon("School", 100, 4, 1.2, 300)
    print(myBeacon)
