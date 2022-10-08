"""
Filename: recipe_dictionary_vanilla.py
Date Created: 9/25/2022
"""
from recipe import Recipe
from ingredient_list import IngredientList
from ingredient import Ingredient

assembling_all = ['Assembling Machine 2', 'Assembling Machine 1', 'Assembling Machine 3']
assembling_with_fluid = ['Assembling Machine 2', 'Assembling Machine 3']
assembling_space = ['Rocket Silo']
chemistry = ['Chemical Plant']
oil = ['Oil Refinery']
basic_smelting = ['Stone Furnace', 'Steel Furnace', 'Electric Furnace']
mining = ['Electric Mining Drill', 'Burner Mining Drill']
pumping = ['Offshore Pump']
drilling = ['Pumpjack']

imageFolder_Tiered = '../resources/images/tiered/'
imageFolder_Single_64x64 = '../resources/images/single_64x64/'

recipeDict = {}

name = "Treat As Raw"
time = 1
allowsProd = False
buildings = ['Assembling Machine 3']

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
imageFilePath = imageFolder_Tiered + 'water-wube.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Treat As Raw (Always)"
time = 1
allowsProd = False
buildings = ['Assembling Machihne 3']

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
imageFilePath = imageFolder_Tiered + 'water-wube.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Raw Materials
"""
name = "Iron Ore"
time = 1
allowsProd = True
buildings = mining

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Iron Ore", 1))
imageFilePath = imageFolder_Tiered + 'iron-ore.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Coal"
time = 1
allowsProd = True
buildings = mining

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Coal", 1))
imageFilePath = imageFolder_Tiered + 'coal.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Stone"
time = 1
allowsProd = True
buildings = mining

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Stone", 1))
imageFilePath = imageFolder_Tiered + 'stone.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Copper Ore"
time = 1
allowsProd = True
buildings = mining

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Copper Ore", 1))
imageFilePath = imageFolder_Tiered + 'copper-ore.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Fluids
"""
name = '1200x Water'
time = 1
allowsProd = False
buildings = pumping

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Water", 1200))
imageFilePath = imageFolder_Tiered + 'water.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Crude Oil"
time = 1
allowsProd = True
buildings = drilling

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Crude Oil", 1))
imageFilePath = imageFolder_Tiered + 'crude-oil.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Smelted Goods
"""
name = "Iron Plate"
time = 3.2
allowsProd = True
buildings = basic_smelting

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Ore", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
imageFilePath = imageFolder_Tiered + 'iron-plate.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Copper Plate"
time = 3.2
allowsProd = True
buildings = basic_smelting

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Ore", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Copper Plate", 1))
imageFilePath = imageFolder_Tiered + 'copper-plate.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Stone Brick"
time = 3.2
allowsProd = True
buildings = basic_smelting

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Stone Brick", 1))
imageFilePath = imageFolder_Tiered + 'stone-brick.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Steel Plate"
time = 16
allowsProd = True
buildings = basic_smelting

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Steel Plate", 1))
imageFilePath = imageFolder_Tiered + 'steel-plate.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Plastic Bar"
time = 1
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Coal", 1))
inputIngredientList.addIngredient(Ingredient("Petroleum Gas", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Plastic Bar", 2))
imageFilePath = imageFolder_Tiered + 'plastic-bar.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Sulfur"
time = 1
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 30))
inputIngredientList.addIngredient(Ingredient("Petroleum Gas", 30))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Sulfur", 2))
imageFilePath = imageFolder_Tiered + 'sulfur.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Fluids
"""
name = "90x Petroleum Gas"
time = 5
allowsProd = True
buildings = oil

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 50))
inputIngredientList.addIngredient(Ingredient("Crude Oil", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 90))
imageFilePath = imageFolder_Tiered + 'petroleum-gas.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Basic Oil Processing"
time = 5
allowsProd = True
buildings = oil

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Crude Oil", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 45))
imageFilePath = imageFolder_Tiered + 'basic-oil-processing.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Advanced Oil Processing"
time = 5
allowsProd = True
buildings = oil

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 50))
inputIngredientList.addIngredient(Ingredient("Crude Oil", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Heavy Oil", 25))
outputIngredientList.addIngredient(Ingredient("Light Oil", 45))
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 55))
imageFilePath = imageFolder_Tiered + 'advanced-oil-processing.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Coal Liquefaction"
time = 5
allowsProd = True
buildings = oil

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Coal", 10))
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 25))
inputIngredientList.addIngredient(Ingredient("Steam", 50))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Heavy Oil", 90))
outputIngredientList.addIngredient(Ingredient("Light Oil", 20))
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 10))
imageFilePath = imageFolder_Tiered + 'coal-liquefaction.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Heavy Oil Cracking to Light Oil"
time = 2
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 30))
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 40))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Light Oil", 30))
imageFilePath = imageFolder_Tiered + 'heavy-oil-cracking.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Light Oil Cracking to Petroleum Gas"
time = 2
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 30))
inputIngredientList.addIngredient(Ingredient("Light Oil", 30))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 20))
imageFilePath = imageFolder_Tiered + 'light-oil-cracking.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "10x Lubricant"
time = 1
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Lubricant", 10))
imageFilePath = imageFolder_Tiered + 'lubricant.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "50x Sulfuric Acid"
time = 1
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Sulfur", 5))
inputIngredientList.addIngredient(Ingredient("Water", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Sulfuric Acid", 50))
imageFilePath = imageFolder_Tiered + 'sulfuric-acid.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Intermediates
"""
name = "Iron Gear Wheel"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))
imageFilePath = imageFolder_Tiered + 'iron-gear-wheel.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Iron Stick"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Iron Stick", 2))
imageFilePath = imageFolder_Tiered + 'iron-stick.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Copper Cable"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Copper Cable", 2))
imageFilePath = imageFolder_Tiered + 'copper-cable.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electronic Circuit"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Copper Cable", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electronic Circuit", 1))
imageFilePath = imageFolder_Tiered + 'electronic-circuit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Advanced Circuit"
time = 6
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Cable", 4))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 2))
inputIngredientList.addIngredient(Ingredient("Plastic Bar", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Advanced Circuit", 1))
imageFilePath = imageFolder_Tiered + 'advanced-circuit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Processing Unit"
time = 10
allowsProd = True
buildings = assembling_with_fluid

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 20))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 2))
inputIngredientList.addIngredient(Ingredient("Sulfuric Acid", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Processing Unit", 1))
imageFilePath = imageFolder_Tiered + 'processing-unit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Engine Unit"
time = 10
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))
inputIngredientList.addIngredient(Ingredient("Pipe", 2))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Engine Unit", 1))
imageFilePath = imageFolder_Tiered + 'engine-unit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electric Engine Unit"
time = 10
allowsProd = True
buildings = assembling_with_fluid

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 2))
inputIngredientList.addIngredient(Ingredient("Engine Unit", 1))
inputIngredientList.addIngredient(Ingredient("Lubricant", 15))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 1))
imageFilePath = imageFolder_Tiered + 'electric-engine-unit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Flying Robot Frame"
time = 20
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 3))
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 1))
inputIngredientList.addIngredient(Ingredient("Battery", 2))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Flying Robot Frame", 1))
imageFilePath = imageFolder_Tiered + 'flying-robot-frame.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Battery"
time = 4
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 1))
inputIngredientList.addIngredient(Ingredient("Sulfuric Acid", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Battery", 1))
imageFilePath = imageFolder_Tiered + 'battery.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Low Density Structure"
time = 20
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Plate", 20))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 2))
inputIngredientList.addIngredient(Ingredient("Plastic Bar", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Low Density Structure", 1))
imageFilePath = imageFolder_Tiered + 'low-density-structure.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Rocket Control Unit"
time = 30
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 1))
inputIngredientList.addIngredient(Ingredient("Speed Module 1", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rocket Control Unit", 1))
imageFilePath = imageFolder_Tiered + 'rocket-control-unit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Empty Barrel"
time = 1
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Empty Barrel", 1))
imageFilePath = imageFolder_Tiered + 'barrel-empty.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Rocket Fuel"
time = 30
allowsProd = True
buildings = assembling_with_fluid

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Solid Fuel", 10))
inputIngredientList.addIngredient(Ingredient("Light Oil", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rocket Fuel", 1))
imageFilePath = imageFolder_Tiered + 'rocket-fuel.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Solid Fuel From Light Oil"
time = 2
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Light Oil", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Fuel", 1))
imageFilePath = imageFolder_Tiered + 'solid-fuel-from-light-oil.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Solid Fuel From Petroleum"
time = 2
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Petroleum Gas", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Fuel", 1))
imageFilePath = imageFolder_Tiered + 'solid-fuel-from-petroleum-gas.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Solid Fuel From Heavy Oil"
time = 0.5
allowsProd = True
buildings = chemistry

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Fuel", 1))
imageFilePath = imageFolder_Tiered + 'solid-fuel-from-heavy-oil.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Logistics Items
"""
name = "Pipe"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Pipe", 1))
imageFilePath = imageFolder_Tiered + 'pipe.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Rail"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Stick", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))
inputIngredientList.addIngredient((Ingredient("Stone", 1)))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rail", 2))
imageFilePath = imageFolder_Tiered + 'rail.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Transport Belt"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Transport Belt", 2))
imageFilePath = imageFolder_Tiered + 'transport-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Underground Belt"
time = 1
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Transport Belt", 5))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Underground Belt", 2))
imageFilePath = imageFolder_Tiered + 'underground-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Splitter"
time = 1
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Transport Belt", 4))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Splitter", 1))
imageFilePath = imageFolder_Tiered + 'splitter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Fast Transport Belt"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Transport Belt", 1))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Fast Transport Belt", 1))
imageFilePath = imageFolder_Tiered + 'fast-transport-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Fast Underground Belt"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Underground Belt", 2))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 40))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Fast Underground Belt", 2))
imageFilePath = imageFolder_Tiered + 'fast-underground-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Fast Splitter"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Splitter", 1))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 10))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Fast Splitter", 1))
imageFilePath = imageFolder_Tiered + 'fast-splitter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Express Transport Belt"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Fast Transport Belt", 1))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 10))
inputIngredientList.addIngredient(Ingredient("Lubricant", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Express Transport Belt", 1))
imageFilePath = imageFolder_Tiered + 'express-transport-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Express Underground Belt"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Fast Underground Belt", 2))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 80))
inputIngredientList.addIngredient(Ingredient("Lubricant", 40))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Express Underground Belt", 2))
imageFilePath = imageFolder_Tiered + 'express-underground-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Express Splitter"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 10))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 10))
inputIngredientList.addIngredient(Ingredient("Lubricant", 80))
inputIngredientList.addIngredient(Ingredient("Fast Splitter", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Express Splitter", 1))
imageFilePath = imageFolder_Tiered + 'express-splitter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Burner Inserter"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Burner Inserter", 1))
imageFilePath = imageFolder_Tiered + 'burner-inserter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Inserter"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Inserter", 1))
imageFilePath = imageFolder_Tiered + 'inserter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Fast Inserter"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 2))
inputIngredientList.addIngredient(Ingredient("Inserter", 1))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Fast Inserter", 1))
imageFilePath = imageFolder_Tiered + 'fast-inserter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "10x Concrete"
time = 10
allowsProd = False
buildings = assembling_with_fluid

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Ore", 2))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 5))
inputIngredientList.addIngredient(Ingredient("Water", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Concrete", 10))
imageFilePath = imageFolder_Tiered + 'concrete.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Military Stuff
"""
name = "Grenade"
time = 8
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 5))
inputIngredientList.addIngredient(Ingredient("Coal", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Grenade", 1))
imageFilePath = imageFolder_Tiered + 'grenade.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Wall"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone Brick", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Wall", 1))
imageFilePath = imageFolder_Tiered + 'wall.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Firearm Magazine"
time = 1
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Firearm Magazine", 1))
imageFilePath = imageFolder_Tiered + 'firearm-magazine.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Piercing Rounds Magazine"
time = 3
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Plate", 5))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))
inputIngredientList.addIngredient(Ingredient("Firearm Magazine", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Piercing Rounds Magazine", 1))
imageFilePath = imageFolder_Tiered + 'piercing-rounds-magazine.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Radar"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 10))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Radar", 1))
imageFilePath = imageFolder_Tiered + 'radar.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
TODO: Energy stuffs
"""

name = "Solar Panel"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 15))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 5))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solar Panel", 1))
imageFilePath = imageFolder_Tiered + 'solar-panel.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Accumulator"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 2))
inputIngredientList.addIngredient(Ingredient("Battery", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Accumulator", 1))
imageFilePath = imageFolder_Tiered + 'accumulator.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Production Buildings
"""
name = "Stone Furnace"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Stone Furnace", 1))
imageFilePath = imageFolder_Tiered + 'stone-furnace.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Steel Furnace"
time = 3
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone Brick", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 6))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Steel Furnace", 1))
imageFilePath = imageFolder_Tiered + 'steel-furnace.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electric Furnace"
time = 5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Furnace", 1))
imageFilePath = imageFolder_Tiered + 'electric-furnace.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Assembling Machine 1"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 5))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 3))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 9))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Assembling Machine 1", 1))
imageFilePath = imageFolder_Tiered + 'assembling-machine-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Assembling Machine 2"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 3))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 5))
inputIngredientList.addIngredient(Ingredient("Assembling Machine 1", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Assembling Machine 2", 1))
imageFilePath = imageFolder_Tiered + 'assembling-machine-2.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Assembling Machine 3"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Assembling Machine 2", 2))
inputIngredientList.addIngredient(Ingredient("Speed Module 1", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Assembling Machine 3", 1))
imageFilePath = imageFolder_Tiered + 'assembling-machine-3.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Oil Refinery"
time = 8
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Steel Plate", 15))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 10))
inputIngredientList.addIngredient(Ingredient("Pipe", 10))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 10))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Oil Refinery", 1))
imageFilePath = imageFolder_Tiered + 'oil-refinery.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Chemical Plant"
time = 5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Pipe", 5))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 5))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Chemical Plant", 1))
imageFilePath = imageFolder_Tiered + 'chemical-plant.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Rocket Silo"
time = 30
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1000))
inputIngredientList.addIngredient(Ingredient("Processing Unit", 200))
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 200))
inputIngredientList.addIngredient(Ingredient("Pipe", 100))
inputIngredientList.addIngredient(Ingredient("Concrete", 1000))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rocket Silo", 1))
imageFilePath = imageFolder_Tiered + 'rocket-silo.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Burner Mining Drill"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone Furnace", 1))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 3))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Burner Mining Drill", 1))
imageFilePath = imageFolder_Tiered + 'burner-mining-drill.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electric Mining Drill"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 5))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 3))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Mining Drill", 1))
imageFilePath = imageFolder_Tiered + 'electric-mining-drill.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Offshore Pump"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 2))
inputIngredientList.addIngredient(Ingredient("Pipe", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Offshore Pump", 1))
imageFilePath = imageFolder_Tiered + 'offshore-pump.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Boiler"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Pipe", 2))
inputIngredientList.addIngredient(Ingredient("Stone Furnace", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Boiler", 1))
imageFilePath = imageFolder_Tiered + 'boiler.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Pumpjack"
time = 5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 10))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Pipe", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Offshore Pump", 1))
imageFilePath = imageFolder_Tiered + 'pumpjack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Beacon"
time = 15
allowsProd = False
buildings = assembling_all
inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 20))
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 20))
inputIngredientList.addIngredient(Ingredient("Copper Cable", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Beacon", 1))
imageFilePath = imageFolder_Tiered + 'basic-beacon.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Sciences
"""
name = "Automation Science Pack"
time = 5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Automation Science Pack", 1))
imageFilePath = imageFolder_Tiered + 'automation-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Logistic Science Pack"
time = 6
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Transport Belt", 1))
inputIngredientList.addIngredient(Ingredient("Inserter", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Logistic Science Pack", 2))
imageFilePath = imageFolder_Tiered + 'logistic-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Military Science Pack"
time = 10
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Grenade", 1))
inputIngredientList.addIngredient(Ingredient("Piercing Rounds Magazine", 1))
inputIngredientList.addIngredient(Ingredient("Wall", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Military Science Pack", 2))
imageFilePath = imageFolder_Tiered + 'military-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Chemical Science Pack"
time = 24
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 3))
inputIngredientList.addIngredient(Ingredient("Engine Unit", 2))
inputIngredientList.addIngredient(Ingredient("Sulfur", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Chemical Science Pack", 2))
imageFilePath = imageFolder_Tiered + 'chemical-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "3x Production Science Pack"
time = 21
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Rail", 30))
inputIngredientList.addIngredient(Ingredient("Electric Furnace", 1))
inputIngredientList.addIngredient(Ingredient("Productivity Module 1", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Production Science Pack", 3))
imageFilePath = imageFolder_Tiered + 'production-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "3x Utility Science Pack"
time = 21
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 2))
inputIngredientList.addIngredient(Ingredient("Flying Robot Frame", 1))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Utility Science Pack", 3))
imageFilePath = imageFolder_Tiered + 'utility-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Satellite"
time = 5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 100))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 100))
inputIngredientList.addIngredient(Ingredient("Rocket Fuel", 50))
inputIngredientList.addIngredient(Ingredient("Solar Panel", 100))
inputIngredientList.addIngredient(Ingredient("Accumulator", 100))
inputIngredientList.addIngredient(Ingredient("Radar", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Satellite", 1))
imageFilePath = imageFolder_Tiered + 'satellite.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Rocket Part"
time = 3
allowsProd = True
buildings = assembling_space

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Rocket Control Unit", 10))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 10))
inputIngredientList.addIngredient(Ingredient("Rocket Fuel", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rocket Part", 1))
imageFilePath = imageFolder_Tiered + 'rocket-part.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "1000x Space Science Pack"
time = 3
allowsProd = False
buildings = assembling_space

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Rocket Part", 100))
inputIngredientList.addIngredient(Ingredient("Satellite", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Space Science Pack", 1000))
imageFilePath = imageFolder_Tiered + 'rocket-science.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)



"""
Modules
"""
name = "Speed Module 1"
time = 15
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Speed Module 1", 1))
imageFilePath = imageFolder_Single_64x64 + 'speed-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Speed Module 2"
time = 30
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Processing Unit", 1))
inputIngredientList.addIngredient(Ingredient("Speed Module 1", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Speed Module 2", 1))
imageFilePath = imageFolder_Single_64x64 + 'speed-2.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Speed Module 3"
time = 60
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 5))
inputIngredientList.addIngredient(Ingredient("Battery", 1))
inputIngredientList.addIngredient(Ingredient("Speed Module 2", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Speed Module 3", 1))
imageFilePath = imageFolder_Single_64x64 + 'speed-3.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Productivity Module 1"
time = 15
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Productivity Module 1", 1))
imageFilePath = imageFolder_Single_64x64 + 'productivity-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Productivity Module 2"
time = 30
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Processing Unit", 1))
inputIngredientList.addIngredient(Ingredient("Productivity Module 1", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Productivity Module 2", 1))
imageFilePath = imageFolder_Single_64x64 + 'productivity-2.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Productivity Module 3"
time = 60
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 5))
inputIngredientList.addIngredient(Ingredient("Battery", 1))
inputIngredientList.addIngredient(Ingredient("Productivity Module 2", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Productivity Module 3", 1))
imageFilePath = imageFolder_Single_64x64 + 'productivity-3.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Efficiency Module 1"
time = 15
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Efficiency Module 1", 1))
imageFilePath = imageFolder_Single_64x64 + 'effectivity-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Efficiency Module 2"
time = 30
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Processing Unit", 1))
inputIngredientList.addIngredient(Ingredient("Efficiency Module 1", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Efficiency Module 2", 1))
imageFilePath = imageFolder_Single_64x64 + 'effectivity-2.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Efficiency Module 3"
time = 60
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 5))
inputIngredientList.addIngredient(Ingredient("Battery", 1))
inputIngredientList.addIngredient(Ingredient("Efficiency Module 2", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Efficiency Module 3", 1))
imageFilePath = imageFolder_Single_64x64 + 'effectivity-3.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)
