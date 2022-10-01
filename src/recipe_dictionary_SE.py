"""
Filename: recipe_dictionary_SE.py
Date Created: 1/9/2021
Here we hold a dictionary of all the recipes we have
"""

""" TODO: Need to filter out what is different than the basic game and then override those/add new things """

from recipe import Recipe
from ingredient_list import IngredientList
from ingredient import Ingredient

assembling_all = ['Assembling Machine 3', 'Burner Assembling Machine', 'Assembling Machine 1', 'Assembling Machine 2', 'Space Assembling Machine', 'Space Manufactory']
assembling_with_fluid = ['Assembling Machine 3', 'Assembling Machine 2', 'Space Assembling Machine', 'Space Manufactory']
assembling_space = ['Space Manufactory']
chemistry = ['Chemical Plant', 'Biochemical Facility']
fuel = ['Fuel Refinery']
oil = ['Oil Refinery', 'Biochemical Facility']
basic_smelting = ['Stone Furnace', 'Steel Furnace', 'Electric Furnace', 'Industrial Furnace']
advanced_smelting = ['Industrial Furnace']
decontamination = ['Decontamination Facility']
mechanical = ['Pulveriser']
computation = ['Supercomputer']
mining = ['Electric Mining Drill', 'Burner Mining Drill', 'Big Mining Drill']
pumping = ['Offshore Pump']
drilling = ['Pumpjack']

imageFolder_Tiered = 'resources/images/tiered/'
imageFolder_Single_64x64 = 'resources/images/single_64x64/'

recipeDict = {}

name = "Treat As Raw"
time = 1
allowsProd = False
buildings = ['Assembling Machine 3']

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

name = "Vulcanite"
time = 1
allowsProd = True
buildings = mining

inputIngredientList = IngredientList()

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Vulcanite", 1))
imageFilePath = imageFolder_Single_64x64 + 'vulcanite.png'
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

name = "60x Steam (165) - Boiler from Coal"
time = 1
allowsProd = False
buildings = ['Boiler']

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 60))
inputIngredientList.addIngredient(Ingredient("Coal", 0.45))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Steam (165)", 60))
imageFilePath = imageFolder_Tiered + 'coal.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "10x Cosmic Water"
time = 1
allowsProd = False
buildings = decontamination

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 99))
inputIngredientList.addIngredient(Ingredient("Lubricant", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Cosmic Water", 10))
imageFilePath = imageFolder_Tiered + 'space-water.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "20x Chemical Gel"
time = 10
allowsProd = False
buildings = assembling_space

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Cosmic Water", 10))
inputIngredientList.addIngredient(Ingredient("Petroleum Gas", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Chemical Gel", 20))
imageFilePath = imageFolder_Tiered + 'chemical-gel.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "10x Thermofluid (25)"
time = 5
allowsProd = False
buildings = None # TODO

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 2))
inputIngredientList.addIngredient(Ingredient("Sulfur", 1))
inputIngredientList.addIngredient(Ingredient("Cosmic Water", 1))
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Thermofluid (25)", 10))
imageFilePath = imageFolder_Tiered + 'space-coolant-hot.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "49x Cooling Thermofluid To -10"
time = 10
allowsProd = False
buildings = None # TODO

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Thermofluid (25)", 50))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Cool Thermofluid (-10)", 49))
imageFilePath = imageFolder_Tiered + 'space-coolant-warm.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "5x Hypercooling Thermofluid To -100"
time = 1
allowsProd = False
buildings = None # TODO

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Cool Thermofluid (-10)", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Cold Thermofluid (-100)", 5))
outputIngredientList.addIngredient(Ingredient("Thermofluid (25)", 5))
imageFilePath = imageFolder_Tiered + 'space-coolant-cold.png'
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

name = "Glass"
time = 4
allowsProd = True
buildings = basic_smelting

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Sand", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Glass", 1))
imageFilePath = imageFolder_Single_64x64 + 'glass.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Crushed Vulcanite"
time = 0.5
allowsProd = True
buildings = mechanical

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Vulcanite", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Crushed Vulcanite", 1))
imageFilePath = imageFolder_Single_64x64 + 'vulcanite-crushed.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Washed Vulcanite"
time = 1
allowsProd = True
buildings = ['Chemical Plant', 'Decontamination Facility']

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Crushed Vulcanite", 2))
inputIngredientList.addIngredient(Ingredient("Water", 6))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Washed Vulcanite", 2))
outputIngredientList.addIngredient(Ingredient("Stone", 0.25))
outputIngredientList.addIngredient(Ingredient("Steam (165)", 3))
imageFilePath = imageFolder_Single_64x64 + 'vulcanite-washed.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Vulcanite Block"
time = 1
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Washed Vulcanite", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Vulcanite Block", 1))
imageFilePath = imageFolder_Single_64x64 + 'vulcanite-block.png'
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

name = "Crude Oil Processing"
time = 2
allowsProd = True
buildings = oil

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Water", 10))
inputIngredientList.addIngredient(Ingredient("Crude Oil", 100))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Heavy Oil", 60))
outputIngredientList.addIngredient(Ingredient("Light Oil", 40))
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 20))
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
outputIngredientList.addIngredient(Ingredient("Heavy Oil", 20))
outputIngredientList.addIngredient(Ingredient("Light Oil", 50))
outputIngredientList.addIngredient(Ingredient("Petroleum Gas", 50))
imageFilePath = imageFolder_Tiered + 'advanced-oil-processing.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Coal Liquefaction"
time = 5
allowsProd = True
buildings = oil

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Coal", 10))
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 25))
inputIngredientList.addIngredient(Ingredient("Steam (165)", 100))

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
time = 0.2
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
time = 0.2
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Copper Cable", 2))
imageFilePath = imageFolder_Tiered + 'copper-cable.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "4x Stone Tablet"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone Brick", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Stone Tablet", 4))
imageFilePath = imageFolder_Single_64x64 + 'stone-tablet.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "2x Sand"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Sand", 2))
imageFilePath = imageFolder_Single_64x64 + 'sand.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Motor"
time = 0.3
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Motor", 1))
imageFilePath = imageFolder_Single_64x64 + 'motor.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electric Motor"
time = 0.4
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Cable", 6))
inputIngredientList.addIngredient(Ingredient("Motor", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Motor", 1))
imageFilePath = imageFolder_Single_64x64 + 'electric-motor.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electronic Circuit"
time = 0.5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Cable", 3))
inputIngredientList.addIngredient(Ingredient("Stone Tablet", 1))

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
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 2))
inputIngredientList.addIngredient(Ingredient("Motor", 1))
inputIngredientList.addIngredient(Ingredient("Pipe", 2))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Engine Unit", 1))
imageFilePath = imageFolder_Tiered + 'engine-unit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electric Engine Unit"
time = 10
allowsProd = True
buildings = assembling_with_fluid

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 1))
inputIngredientList.addIngredient(Ingredient("Electric Motor", 1))
inputIngredientList.addIngredient(Ingredient("Engine Unit", 1))
inputIngredientList.addIngredient(Ingredient("Lubricant", 40))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 1))
imageFilePath = imageFolder_Tiered + 'electric-engine-unit.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Heat Shielding"
time = 10
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone Tablet", 20))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 2))
inputIngredientList.addIngredient(Ingredient("Sulfur", 8))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Heat Shielding", 1))
imageFilePath = imageFolder_Single_64x64 + 'heat-shielding.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Flying Robot Frame"
time = 20
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 4))
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 4))
inputIngredientList.addIngredient(Ingredient("Battery", 4))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 4))

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
inputIngredientList.addIngredient(Ingredient("Glass", 10))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))
inputIngredientList.addIngredient(Ingredient("Plastic Bar", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Low Density Structure", 1))
imageFilePath = imageFolder_Tiered + 'low-density-structure.png'
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

name = "Solid Rocket Fuel"
time = 1
allowsProd = True
buildings = fuel

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Solid Fuel", 10))
inputIngredientList.addIngredient(Ingredient("Light Oil", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Rocket Fuel", 1))
imageFilePath = imageFolder_Tiered + 'rocket-fuel.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Solid Fuel From Light Oil"
time = 0.5
allowsProd = True
buildings = fuel

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Light Oil", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Fuel", 1))
imageFilePath = imageFolder_Tiered + 'solid-fuel-from-light-oil.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Solid Fuel From Petroleum"
time = 0.5
allowsProd = True
buildings = fuel

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Petroleum Gas", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Fuel", 1))
imageFilePath = imageFolder_Tiered + 'solid-fuel-from-petroleum-gas.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Solid Fuel From Heavy Oil"
time = 0.5
allowsProd = True
buildings = fuel

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Heavy Oil", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solid Fuel", 1))
imageFilePath = imageFolder_Tiered + 'solid-fuel-from-heavy-oil.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Machine Learning Data"
time = 10
allowsProd = True
buildings = computation

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 1))
inputIngredientList.addIngredient(Ingredient("Blank Data Card", 1))
inputIngredientList.addIngredient(Ingredient("Cool Thermofluid (-10)", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Machine Learning Data", 1))
outputIngredientList.addIngredient(Ingredient("Scrap", 1))
outputIngredientList.addIngredient(Ingredient("Thermofluid (25)", 5))
imageFilePath = imageFolder_Single_64x64 + 'machine-learning.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Blank Data Card"
time = 10
allowsProd = False
buildings = assembling_space

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 3))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 6))
inputIngredientList.addIngredient(Ingredient("Polished Data Storage Substrate", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Blank Data Card", 1))
imageFilePath = imageFolder_Single_64x64 + 'blank.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Polished Data Storage Substrate From Cosmic Water"
time = 2.5
allowsProd = False
buildings = decontamination

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Rough Data Storage Substrate", 1))
inputIngredientList.addIngredient(Ingredient("Cosmic Water", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Polished Data Storage Substrate", 1))
outputIngredientList.addIngredient(Ingredient("Scrap", 0.01))
outputIngredientList.addIngredient(Ingredient("Contaminated Cosmic Water", 5))
imageFilePath = imageFolder_Single_64x64 + 'data-storage-substrate-cleaned.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Polished Data Storage Substrate From Chemical Gel"
time = 2.5
allowsProd = False
buildings = decontamination

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Rough Data Storage Substrate", 1))
inputIngredientList.addIngredient(Ingredient("Chemical Gel", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Polished Data Storage Substrate", 1))
imageFilePath = imageFolder_Single_64x64 + 'data-storage-substrate-cleaned.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Rough Data Storage Substrate"
time = 5
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Glass", 2))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rough Data Storage Substrate", 1))
outputIngredientList.addIngredient(Ingredient("Scrap", 0.5))
imageFilePath = imageFolder_Single_64x64 + 'data-storage-substrate.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Data Formatting"
time = 1.5
allowsProd = False
buildings = computation

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Junk Data Card", 1))
inputIngredientList.addIngredient(Ingredient("Cold Thermofluid (-100)", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Blank Data Card", 0.7))
outputIngredientList.addIngredient(Ingredient("Broken Data Card", 0.2899))
outputIngredientList.addIngredient(Ingredient("Thermofluid (25)", 1))
imageFilePath = imageFolder_Single_64x64 + 'blank.png'
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

name = "Space Pipe"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Copper Cable", 2))
inputIngredientList.addIngredient(Ingredient("Glass", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))
inputIngredientList.addIngredient((Ingredient("Plastic Bar", 1)))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Space Pipe", 2))
imageFilePath = imageFolder_Single_64x64 + 'space-pipe.png'
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
inputIngredientList.addIngredient(Ingredient("Motor", 1))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Transport Belt", 2))
imageFilePath = imageFolder_Tiered + 'transport-belt.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Burner Inserter"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Stick", 2))
inputIngredientList.addIngredient(Ingredient("Motor", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Burner Inserter", 1))
imageFilePath = imageFolder_Tiered + 'burner-inserter.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Inserter"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Motor", 1))
inputIngredientList.addIngredient(Ingredient("Burner Inserter", 1))

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

name = "Space Platform Scaffold"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Heat Shielding", 1))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Space Platform Scaffold", 1))
imageFilePath = imageFolder_Single_64x64 + 'space-platform-scaffold.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "10x Concrete"
time = 10
allowsProd = False
buildings = assembling_with_fluid

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Stick", 2))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 5))
inputIngredientList.addIngredient(Ingredient("Sand", 10))
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

name = "Stone Wall"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Stone Brick", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Stone Wall", 1))
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

"""
TODO: Energy stuffs
"""

name = "Solar Panel"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 15))
inputIngredientList.addIngredient(Ingredient("Glass", 5))
inputIngredientList.addIngredient(Ingredient("Copper Plate", 5))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Solar Panel", 1))
imageFilePath = imageFolder_Tiered + 'solar-panel.png'
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
inputIngredientList.addIngredient(Ingredient("Stone Brick", 6))
inputIngredientList.addIngredient(Ingredient("Stone Furnace", 1))
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
inputIngredientList.addIngredient(Ingredient("Heat Shielding", 2))
inputIngredientList.addIngredient(Ingredient("Steel Furnace", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Furnace", 1))
imageFilePath = imageFolder_Tiered + 'electric-furnace.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Industrial Furnace"
time = 7
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 4))
inputIngredientList.addIngredient(Ingredient("Heat Shielding", 4))
inputIngredientList.addIngredient(Ingredient("Concrete", 8))
inputIngredientList.addIngredient(Ingredient("Electric Furnace", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 16))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Industrial Furnace", 1))
imageFilePath = imageFolder_Single_64x64 + 'industrial-furnace.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Burner Assembling Machine"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Motor", 1))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 4))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 8))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Burner Assembling Machine", 1))
imageFilePath = imageFolder_Single_64x64 + 'burner-assembling-machine.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Assembling Machine 1"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 4))
inputIngredientList.addIngredient(Ingredient("Electric Motor", 1))
inputIngredientList.addIngredient(Ingredient("Burner Assembling Machine", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Assembling Machine 1", 1))
imageFilePath = imageFolder_Tiered + 'assembling-machine-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Assembling Machine 2"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 2))
inputIngredientList.addIngredient(Ingredient("Electric Motor", 2))
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
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 8))
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 4))
inputIngredientList.addIngredient(Ingredient("Concrete", 8))
inputIngredientList.addIngredient(Ingredient("Assembling Machine 2", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 8))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Assembling Machine 3", 1))
imageFilePath = imageFolder_Tiered + 'assembling-machine-3.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Space Assembling Machine"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 4))
inputIngredientList.addIngredient(Ingredient("Processing Unit", 4))
inputIngredientList.addIngredient(Ingredient("Heat Shielding", 4))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 4))
inputIngredientList.addIngredient(Ingredient("Assembling Machine 2", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Space Assembling Machine", 1))
imageFilePath = imageFolder_Single_64x64 + 'space-assembling-machine.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Space Manufactory"
time = 10
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 32))
inputIngredientList.addIngredient(Ingredient("Heat Shielding", 8))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 80))
inputIngredientList.addIngredient(Ingredient("Fast Inserter", 8))
inputIngredientList.addIngredient(Ingredient("Space Assembling Machine", 4))
inputIngredientList.addIngredient(Ingredient("Cosmic Water", 8))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Space Manufactory", 1))
imageFilePath = imageFolder_Single_64x64 + 'space-manufactory.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Supercomputer"
time = 10
allowsProd = False
buildings = assembling_space

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 100))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 40))
inputIngredientList.addIngredient(Ingredient("Space Assembling Machine", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient((Ingredient("Supercomputer", 1)))
imageFilePath = imageFolder_Single_64x64 + 'Supercomputer-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Pulveriser"
time = 30
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Pipe", 15))
inputIngredientList.addIngredient(Ingredient("Concrete", 15))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 15))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 15))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Pulveriser", 1))
imageFilePath = imageFolder_Single_64x64 + 'pulveriser.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Oil Refinery"
time = 8
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Motor", 15))
inputIngredientList.addIngredient(Ingredient("Pipe", 15))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 15))
inputIngredientList.addIngredient(Ingredient("Glass", 15))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 15))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Oil Refinery", 1))
imageFilePath = imageFolder_Tiered + 'oil-refinery.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Chemical Plant"
time = 5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Motor", 5))
inputIngredientList.addIngredient(Ingredient("Pipe", 5))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 5))
inputIngredientList.addIngredient(Ingredient("Glass", 5))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 5))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Chemical Plant", 1))
imageFilePath = imageFolder_Tiered + 'chemical-plant.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Decontamination Facility"
time = 10
allowsProd = False
buildings = ['Space Assembling Machine', 'Space Manufactory']

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 32))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 40))
inputIngredientList.addIngredient(Ingredient("Space Pipe", 10))
inputIngredientList.addIngredient(Ingredient("Chemical Plant", 1))
inputIngredientList.addIngredient(Ingredient("Vulcanite Block", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Decontamination Facility", 1))
imageFilePath = imageFolder_Single_64x64 + 'decontamination-facility.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Fuel Refinery"
time = 30
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Motor", 20))
inputIngredientList.addIngredient(Ingredient("Pipe", 20))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 20))
inputIngredientList.addIngredient(Ingredient("Glass", 20))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Fuel Refinery", 1))
imageFilePath = imageFolder_Tiered + 'oil-refinery.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Burner Mining Drill"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Motor", 1))
inputIngredientList.addIngredient(Ingredient("Stone Brick", 4))
inputIngredientList.addIngredient(Ingredient("Iron Plate", 4))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Burner Mining Drill", 1))
imageFilePath = imageFolder_Tiered + 'burner-mining-drill.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Electric Mining Drill"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Iron Gear Wheel", 4))
inputIngredientList.addIngredient(Ingredient("Electric Motor", 4))
inputIngredientList.addIngredient(Ingredient("Burner Mining Drill", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Electric Mining Drill", 1))
imageFilePath = imageFolder_Tiered + 'electric-mining-drill.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Big Mining Drill"
time = 4
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Engine Unit", 8))
inputIngredientList.addIngredient(Ingredient("Processing Unit", 4))
inputIngredientList.addIngredient(Ingredient("Electric Mining Drill", 1))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 20))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Big Mining Drill", 1))
imageFilePath = imageFolder_Single_64x64 + 'big-mining-drill.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Offshore Pump"
time = 0.5
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electric Motor", 2))
inputIngredientList.addIngredient(Ingredient("Pipe", 4))

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
inputIngredientList.addIngredient(Ingredient("Electric Motor", 10))
inputIngredientList.addIngredient(Ingredient("Pipe", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 15))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Offshore Pump", 1))
imageFilePath = imageFolder_Tiered + 'pumpjack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Basic Beacon"
time = 15
allowsProd = False
buildings = assembling_all
inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 20))
inputIngredientList.addIngredient(Ingredient("Electric Motor", 10))
inputIngredientList.addIngredient(Ingredient("Concrete", 10))
inputIngredientList.addIngredient(Ingredient("Steel Plate", 10))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Basic Beacon", 1))
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
time = 10
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Transport Belt", 2))
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
inputIngredientList.addIngredient(Ingredient("Stone Wall", 2))

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

name = "5x Utility Science Pack"
time = 35
allowsProd = True
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Processing Unit", 3))
inputIngredientList.addIngredient(Ingredient("Flying Robot Frame", 1))
inputIngredientList.addIngredient(Ingredient("Low Density Structure", 3))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Utility Science Pack", 5))
imageFilePath = imageFolder_Tiered + 'utility-science-pack.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "10x Rocket Science Pack"
time = 80
allowsProd = False
buildings = assembling_space
# TODO: Add satellite telemetry!
inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Empty Barrel", 1))
inputIngredientList.addIngredient(Ingredient("Solid Rocket Fuel", 1))
inputIngredientList.addIngredient(Ingredient("Space Platform Scaffold", 1))
inputIngredientList.addIngredient(Ingredient("Solar Panel", 1))
inputIngredientList.addIngredient(Ingredient("Vulcanite Block", 1))
inputIngredientList.addIngredient(Ingredient("Machine Learning Data", 1))
inputIngredientList.addIngredient(Ingredient("Chemical Gel", 2))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Rocket Science Pack", 10))
outputIngredientList.addIngredient(Ingredient("Junk Data Card", 1))
imageFilePath = imageFolder_Tiered + 'rocket-science.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

"""
Modules
"""
name = "Speed Module 1"
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Speed Module 1", 1))
imageFilePath = imageFolder_Single_64x64 + 'speed-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Speed Module 2"
time = 4
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
time = 8
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
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Productivity Module 1", 1))
imageFilePath = imageFolder_Single_64x64 + 'productivity-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Productivity Module 2"
time = 4
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
time = 8
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
time = 2
allowsProd = False
buildings = assembling_all

inputIngredientList = IngredientList()
inputIngredientList.addIngredient(Ingredient("Electronic Circuit", 5))
inputIngredientList.addIngredient(Ingredient("Advanced Circuit", 1))

outputIngredientList = IngredientList()
outputIngredientList.addIngredient(Ingredient("Efficiency Module 1", 1))
imageFilePath = imageFolder_Single_64x64 + 'effectivity-1.png'
recipeDict[name] = Recipe(name, time, allowsProd, inputIngredientList, outputIngredientList, buildings, imageFilePath)

name = "Efficiency Module 2"
time = 4
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
time = 8
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
