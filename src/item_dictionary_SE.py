"""
Filename: item_dictionary_SE.py
Date Created: 1/9/2021
Here we hold a dictionary of all the items that we create
"""

""" TODO: Need to filter out what is different than the basic game and then override those/add new things """

from item import Item
from building import Building
from module import Module

imageFolder_Tiered = 'resources/images/tiered/'
imageFolder_Single_64x64 = 'resources/images/single_64x64/'

itemDict = {}

"""
Fluids
"""
name = "Water"
stackSize = None
recipes = ['1200x Water']
imageFilePath = imageFolder_Tiered + 'water.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Crude Oil"
stackSize = None
recipes = ['Crude Oil']
imageFilePath = imageFolder_Tiered + 'crude-oil.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Light Oil"
stackSize = None
recipes = ['Crude Oil Processing', 'Advanced Oil Processing', 'Coal Liquefaction', 'Heavy Oil Cracking to Light Oil']
imageFilePath = imageFolder_Tiered + 'light-oil.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Heavy Oil"
stackSize = None
recipes = ['Crude Oil Processing', 'Advanced Oil Processing', 'Coal Liquefaction']
imageFilePath = imageFolder_Tiered + 'heavy-oil.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Lubricant"
stackSize = None
recipes = ['10x Lubricant']
imageFilePath = imageFolder_Tiered + 'lubricant.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Petroleum Gas"
stackSize = None
recipes = ['90x Petroleum Gas', 'Crude Oil Processing', 'Advanced Oil Processing', 'Coal Liquefaction', 'Light Oil Cracking to Petroleum Gas']
imageFilePath = imageFolder_Tiered + 'petroleum-gas.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Sulfuric Acid"
stackSize = None
recipes = ['50x Sulfuric Acid']
imageFilePath = imageFolder_Tiered + 'sulfuric-acid.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Steam (165)"
stackSize = None
recipes = ['60x Steam (165) - Boiler from Coal', 'Washed Vulcanite']
imageFilePath = imageFolder_Tiered + 'steam.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Thermofluid (25)"
stackSize = None
recipes = ['10x Thermofluid (25)', '5x Hypercooling Thermofluid To -100', 'Machine Learning Data', 'Data Formatting']
imageFilePath = imageFolder_Tiered + 'space-coolant-hot.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Cool Thermofluid (-10)"
stackSize = None
recipes = ['49x Cooling Thermofluid To -10']
imageFilePath = imageFolder_Tiered + 'space-coolant-warm.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Cold Thermofluid (-100)"
stackSize = None
recipes = ['5x Hypercooling Thermofluid To -100']
imageFilePath = imageFolder_Tiered + 'space-coolant-cold.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Cosmic Water"
stackSize = None
recipes = ['10x Cosmic Water']
imageFilePath = imageFolder_Tiered + 'space-water.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Contaminated Cosmic Water"
stackSize = None
recipes = ['Polished Data Storage Substrate From Cosmic Water']
imageFilePath = imageFolder_Tiered + 'contaminated-space-water.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Chemical Gel"
stackSize = None
recipes = ['20x Chemical Gel']
imageFilePath = imageFolder_Tiered + 'chemical-gel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Raw materials
"""
name = "Coal"
stackSize = 50
recipes = ["Coal"]
imageFilePath = imageFolder_Tiered + 'coal.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Iron Ore"
stackSize = 50
recipes = ["Iron Ore"]
imageFilePath = imageFolder_Tiered + 'iron-ore.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Copper Ore"
stackSize = 50
recipes = ["Copper Ore"]
imageFilePath = imageFolder_Tiered + 'copper-ore.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Stone"
stackSize = 50
recipes = ["Stone"]
imageFilePath = imageFolder_Tiered + 'stone.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Uranium Ore"
stackSize = 50
imageFilePath = imageFolder_Tiered + 'uranium-ore.png'
itemDict[name] = Item(name, stackSize, imageFilePath)

name = "Scrap"
stackSize = 50
recipes = ['Machine Learning Data', 'Polished Data Storage Substrate From Cosmic Water, Rough Data Storage Substrate']
imageFilePath = imageFolder_Single_64x64 + 'scrap.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Vulcanite"
stackSize = 50
recipes = ['Vulcanite']
imageFilePath = imageFolder_Single_64x64 + 'vulcanite.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Smelted Goods
"""
name = "Iron Plate"
stackSize = 100
recipes = ['Iron Plate']
imageFilePath = imageFolder_Tiered + 'iron-plate.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Copper Plate"
stackSize = 100
recipes = ['Copper Plate']
imageFilePath = imageFolder_Tiered + 'copper-plate.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Stone Brick"
stackSize = 100
recipes = ['Stone Brick']
imageFilePath = imageFolder_Tiered + 'stone-brick.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Steel Plate"
stackSize = 100
recipes = ['Steel Plate']
imageFilePath = imageFolder_Tiered + 'steel-plate.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Plastic Bar"
stackSize = 100
recipes = ['2x Plastic Bar']
imageFilePath = imageFolder_Tiered + 'plastic-bar.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Glass"
stackSize = 100
recipes = ['Glass']
imageFilePath = imageFolder_Single_64x64 + 'glass.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Crushed Vulcanite"
stackSize = 50
recipes = ['Crushed Vulcanite']
imageFilePath = imageFolder_Single_64x64 + 'vulcanite-crushed.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Washed Vulcanite"
stackSize = 50
recipes = ['Washed Vulcanite']
imageFilePath = imageFolder_Single_64x64 + 'vulcanite-washed.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Vulcanite Block"
stackSize = 100
recipes = ['Vulcanite Block']
imageFilePath = imageFolder_Single_64x64 + 'vulcanite-block.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Sulfur"
stackSize = 50
recipes = ['2x Sulfur']
imageFilePath = imageFolder_Tiered + 'sulfur.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Intermediates
"""
name = "Iron Gear Wheel"
stackSize = 100
recipes = ['Iron Gear Wheel']
imageFilePath = imageFolder_Tiered + 'iron-gear-wheel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Iron Stick"
stackSize = 100
recipes = ['2x Iron Stick']
imageFilePath = imageFolder_Tiered + 'iron-stick.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Copper Cable"
stackSize = 200
recipes = ['2x Copper Cable']
imageFilePath = imageFolder_Tiered + 'copper-cable.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Stone Tablet"
stackSize = 100
recipes = ['4x Stone Tablet']
imageFilePath = imageFolder_Single_64x64 + 'stone-tablet.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Sand"
stackSize = 200
recipes = ['2x Sand']
imageFilePath = imageFolder_Single_64x64 + 'sand.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Motor"
stackSize = 50
recipes = ['Motor']
imageFilePath = imageFolder_Single_64x64 + 'motor.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Electric Motor"
stackSize = 50
recipes = ['Electric Motor']
imageFilePath = imageFolder_Single_64x64 + 'electric-motor.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Electronic Circuit"
stackSize = 200
recipes = ['Electronic Circuit']
imageFilePath = imageFolder_Tiered + 'electronic-circuit.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Advanced Circuit"
stackSize = 200
recipes = ['Advanced Circuit']
imageFilePath = imageFolder_Tiered + 'advanced-circuit.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Processing Unit"
stackSize = 100
recipes = ['Processing Unit']
imageFilePath = imageFolder_Tiered + 'processing-unit.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Engine Unit"
stackSize = 50
recipes = ['Engine Unit']
imageFilePath = imageFolder_Tiered + 'engine-unit.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Electric Engine Unit"
stackSize = 50
recipes = ['Electric Engine Unit']
imageFilePath = imageFolder_Tiered + 'electric-engine-unit.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Heat Shielding"
stackSize = 50
recipes = ['Heat Shielding']
imageFilePath = imageFolder_Single_64x64 + 'heat-shielding.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Flying Robot Frame"
stackSize = 50
recipes = ['Flying Robot Frame']
imageFilePath = imageFolder_Tiered + 'flying-robot-frame.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Battery"
stackSize = 200
recipes = ['Battery']
imageFilePath = imageFolder_Tiered + 'battery.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Low Density Structure"
stackSize = 50
recipes = ['Low Density Structure']
imageFilePath = imageFolder_Tiered + 'low-density-structure.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Empty Barrel"
stackSize = 10
recipes = ['Empty Barrel']
imageFilePath = imageFolder_Tiered + 'barrel-empty.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Solid Rocket Fuel"
stackSize = 10
recipes = ['Solid Rocket Fuel']
imageFilePath = imageFolder_Tiered + 'rocket-fuel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Solid Fuel"
stackSize = 50
recipes = ['Solid Fuel From Light Oil', 'Solid Fuel From Petroleum', 'Solid Fuel From Heavy Oil']
imageFilePath = imageFolder_Tiered + 'solid-fuel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Machine Learning Data"
stackSize = 50
recipes = ['Machine Learning Data']
imageFilePath = imageFolder_Single_64x64 + 'machine-learning.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Blank Data Card"
stackSize = 50
recipes = ['Blank Data Card']
imageFilePath = imageFolder_Single_64x64 + 'blank.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Polished Data Storage Substrate"
stackSize = 100
recipes = ['Polished Data Storage Substrate From Cosmic Water', 'Polished Data Storage Substrate From Chemical Gel']
imageFilePath = imageFolder_Single_64x64 + 'data-storage-substrate-cleaned.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Rough Data Storage Substrate"
stackSize = 50
recipes = ['Rough Data Storage Substrate']
imageFilePath = imageFolder_Single_64x64 + 'data-storage-substrate.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Junk Data Card"
stackSize = 50
recipes = ['10x Rocket Science Pack']
imageFilePath = imageFolder_Single_64x64 + 'junk.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Broken Data Card"
stackSize = 50
recipes = ['Data Formatting']
imageFilePath = imageFolder_Single_64x64 + 'broken.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Logistics Items
"""
name = "Pipe"
stackSize = 100
recipes = ['Pipe']
imageFilePath = imageFolder_Tiered + 'pipe.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Space Pipe"
stackSize = 100
recipes = ["Space Pipe"]
imageFilePath = imageFolder_Single_64x64 + 'space-pipe.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Rail"
stackSize = 100
recipes = ['2x Rail']
imageFilePath = imageFolder_Tiered + 'rail.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Transport Belt"
stackSize = 100
recipes = ['2x Transport Belt']
imageFilePath = imageFolder_Tiered + 'transport-belt.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Burner Inserter"
stackSize = 50
recipes = ['Burner Inserter']
imageFilePath = imageFolder_Tiered + 'burner-inserter.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Inserter"
stackSize = 50
recipes = ['Inserter']
imageFilePath = imageFolder_Tiered + 'inserter.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Fast Inserter"
stackSize = 50
recipes = ['Fast Inserter']
imageFilePath = imageFolder_Tiered + 'fast-inserter.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Space Platform Scaffold"
stackSize = 100
recipes = ['Space Platform Scaffold']
imageFilePath = imageFolder_Single_64x64 + 'space-platform-scaffold.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Concrete"
stackSize = 100
recipes = ['10x Concrete']
imageFilePath = imageFolder_Tiered + 'concrete.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Sciences
"""
name = "Automation Science Pack"
stackSize = 200
recipes = ['Automation Science Pack']
imageFilePath = imageFolder_Tiered + 'automation-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Logistic Science Pack"
stackSize = 200
recipes = ['2x Logistic Science Pack']
imageFilePath = imageFolder_Tiered + 'logistic-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Military Science Pack"
stackSize = 200
recipes = ['2x Military Science Pack']
imageFilePath = imageFolder_Tiered + 'military-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Chemical Science Pack"
stackSize = 200
recipes = ['2x Chemical Science Pack']
imageFilePath = imageFolder_Tiered + 'chemical-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Production Science Pack"
stackSize = 200
recipes = ['3x Production Science Pack']
imageFilePath = imageFolder_Tiered + 'production-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Utility Science Pack"
stackSize = 200
recipes = ['5x Utility Science Pack']
imageFilePath = imageFolder_Tiered + 'utility-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Rocket Science Pack"
stackSize = 200
recipes = ['10x Rocket Science Pack']
imageFilePath = imageFolder_Tiered + 'rocket-science.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Military Stuff
"""
name = "Grenade"
stackSize = 100
recipes = ['Grenade']
imageFilePath = imageFolder_Tiered + 'grenade.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Stone Wall"
stackSize = 100
recipes = ['Stone Wall']
imageFilePath = imageFolder_Tiered + 'wall.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Firearm Magazine"
stackSize = 200
recipes = ['Firearm Magazine']
imageFilePath = imageFolder_Tiered + 'firearm-magazine.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Piercing Rounds Magazine"
stackSize = 200
recipes = ['Piercing Rounds Magazine']
imageFilePath = imageFolder_Tiered + 'piercing-rounds-magazine.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
TODO: Energy stuffs
"""

name = "Solar Panel"
stackSize = 50
recipes = ['Solar Panel']
imageFilePath = imageFolder_Tiered + 'solar-panel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Production Buildings
"""
name = "Stone Furnace"
stackSize = 50
moduleSlots = 0
powerConsumption = 90
craftingSpeed = 1
recipes = ['Stone Furnace']
imageFilePath = imageFolder_Tiered + 'stone-furnace.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Steel Furnace"
stackSize = 50
moduleSlots = 0
powerConsumption = 90
craftingSpeed = 2
recipes = ['Steel Furnace']
imageFilePath = imageFolder_Tiered + 'steel-furnace.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Electric Furnace"
stackSize = 50
moduleSlots = 2
powerConsumption = 186
craftingSpeed = 2
recipes = ['Electric Furnace']
imageFilePath = imageFolder_Tiered + 'electric-furnace.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Industrial Furnace"
stackSize = 20
moduleSlots = 4
powerConsumption = 90
craftingSpeed = 3
recipes = ['Industrial Furnace']
imageFilePath = imageFolder_Single_64x64 + 'industrial-furnace.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Burner Assembling Machine"
stackSize = 50
moduleSlots = 0
powerConsumption = 83.33
craftingSpeed = 0.5
recipes = ['Burner Assembling Machine']
imageFilePath = imageFolder_Single_64x64 + 'burner-assembling-machine.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Assembling Machine 1"
stackSize = 50
moduleSlots = 0
powerConsumption = 77.5
craftingSpeed = 0.5
recipes = ['Assembling Machine 1']
imageFilePath = imageFolder_Tiered + 'assembling-machine-1.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Assembling Machine 2"
stackSize = 50
moduleSlots = 2
powerConsumption = 155
craftingSpeed = 0.75
recipes = ['Assembling Machine 2']
imageFilePath = imageFolder_Tiered + 'assembling-machine-2.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Assembling Machine 3"
stackSize = 50
moduleSlots = 4
powerConsumption = 388
craftingSpeed = 1.25
recipes = ['Assembling Machine 3']
imageFilePath = imageFolder_Tiered + 'assembling-machine-3.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Space Assembling Machine"
stackSize = 50
moduleSlots = 4
powerConsumption = 388
craftingSpeed = 1.25
recipes = ['Space Assembling Machine']
imageFilePath = imageFolder_Single_64x64 + 'space-assembling-machine.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Space Manufactory"
stackSize = 1
moduleSlots = 6
powerConsumption = 1000
craftingSpeed = 10
recipes = ['Space Manufactory']
imageFilePath = imageFolder_Single_64x64 + 'space-manufactory.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Supercomputer"
stackSize = 15
moduleSlots = 4 # TODO IDK HOW MANY
powerConsumption = 1003
craftingSpeed = 1
recipes = ['Supercomputer']
imageFilePath = imageFolder_Single_64x64 + 'supercomputer-1.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Pulveriser'
stackSize = 5
moduleSlots = 4
powerConsumption = 517
craftingSpeed = 2
recipes = ['Pulveriser']
imageFilePath = imageFolder_Single_64x64 + 'pulveriser.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Oil Refinery'
stackSize = 10
moduleSlots = 3
powerConsumption = 434
craftingSpeed = 1
recipes = ['Oil Refinery']
imageFilePath = imageFolder_Tiered + 'oil-refinery.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Chemical Plant'
stackSize = 10
moduleSlots = 3
powerConsumption = 217
craftingSpeed = 1
recipes = ['Chemical Plant']
imageFilePath = imageFolder_Tiered + 'chemical-plant.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Decontamination Facility'
stackSize = 10
moduleSlots = 10 # TODO IDK
powerConsumption = 2070
craftingSpeed = 1
recipes = ['Decontamination Facility']
imageFilePath = imageFolder_Single_64x64 + 'decontamination-facility.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Fuel Refinery'
stackSize = 10
moduleSlots = 3
powerConsumption = 1030
craftingSpeed = 1
recipes = ['Fuel Refinery']
imageFilePath = imageFolder_Tiered + 'oil-refinery.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Burner Mining Drill'
stackSize = 50
moduleSlots = 0
powerConsumption = 0
craftingSpeed = 0.25
recipes = ['Burner Mining Drill']
imageFilePath = imageFolder_Tiered + 'burner-mining-drill.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Electric Mining Drill'
stackSize = 50
moduleSlots = 2
powerConsumption = 90
craftingSpeed = 0.5
recipes = ['Electric Mining Drill']
imageFilePath = imageFolder_Tiered + 'electric-mining-drill.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Big Mining Drill'
stackSize = 50
moduleSlots = 4 # TODO CHECK THIS WHEN I BUILD ONE LOL
powerConsumption = 500
craftingSpeed = 0.1
recipes = ['Big Mining Drill']
imageFilePath = imageFolder_Single_64x64 + 'big-mining-drill.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Offshore Pump"
stackSize = 20
moduleSlots = 0
powerConsumption = 50
craftingSpeed = 1
recipes = ['Offshore Pump']
imageFilePath = imageFolder_Tiered + 'offshore-pump.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Boiler"
stackSize = 50
moduleSlots = 0
powerConsumption = 1800
craftingSpeed = 1
recipes = ['Boiler']
imagefilePath = imageFolder_Tiered + 'boiler.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Pumpjack"
stackSize = 20
moduleSlots = 2
powerConsumption = 90
craftingSpeed = 1
recipes = ['Offshore Pump']
imageFilePath = imageFolder_Tiered + 'pumpjack.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = "Basic Beacon"
stacksize = 10
moduleSlots = 8
powerConsumption = 200
craftingSpeed = 0
recipes = ['Basic Beacon']
imageFilePath = imageFolder_Tiered + 'basic-beacon.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

"""
Modules
"""
name = "Empty Module"
stackSize = 50
moduleType = 'n'
productivityEffect = 0
speedEffect = 0
powerEffect = 0
recipes = [None]
imageFilePath = imageFolder_Tiered + 'water-wube.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Speed Module 1"
stackSize = 50
moduleType = 's'
productivityEffect = 0
speedEffect = 0.2
powerEffect = 0.5
recipes = ['Speed Module 1']
imageFilePath = imageFolder_Single_64x64 + 'speed-1.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Speed Module 2"
stackSize = 50
moduleType = 's'
productivityEffect = 0
speedEffect = 0.3
powerEffect = 0.6
recipes = ['Speed Module 2']
imageFilePath = imageFolder_Single_64x64 + 'speed-2.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Speed Module 3"
stackSize = 50
moduleType = 's'
productivityEffect = 0
speedEffect = 0.4
powerEffect = 0.8
recipes = ['Speed Module 3']
imageFilePath = imageFolder_Single_64x64 + 'speed-3.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Productivity Module 1"
stackSize = 50
moduleType = 'p'
productivityEffect = 0.04
speedEffect = -0.1
powerEffect = 0.5
recipes = ['Productivity Module 1']
imageFilePath = imageFolder_Single_64x64 + 'productivity-1.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Productivity Module 2"
stackSize = 50
moduleType = 'p'
productivityEffect = 0.06
speedEffect = -0.15
powerEffect = 0.6
recipes = ['Productivity Module 2']
imageFilePath = imageFolder_Single_64x64 + 'productivity-2.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Productivity Module 3"
stackSize = 50
moduleType = 'p'
productivityEffect = 0.08
speedEffect = -0.2
powerEffect = 0.8
recipes = ['Productivity Module 3']
imageFilePath = imageFolder_Single_64x64 + 'productivity-3.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Efficiency Module 1"
stackSize = 50
moduleType = 'e'
productivityEffect = 0
speedEffect = 0
powerEffect = -0.4
recipes = ['Efficiency Module 1']
imageFilePath = imageFolder_Single_64x64 + 'effectivity-1.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Efficiency Module 2"
stackSize = 50
moduleType = 'e'
productivityEffect = 0
speedEffect = 0
powerEffect = -0.6
recipes = ['Efficiency Module 2']
imageFilePath = imageFolder_Single_64x64 + 'effectivity-2.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Efficiency Module 3"
stackSize = 50
moduleType = 'e'
productivityEffect = 0
speedEffect = 0
powerEffect = -1.0
recipes = ['Efficiency Module 3']
imageFilePath = imageFolder_Single_64x64 + 'effectivity-3.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)
