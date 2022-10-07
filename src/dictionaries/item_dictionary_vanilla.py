"""
Filename: item_dictionary_vanilla.py
Date Created: 7/5/2022
"""


from item import Item
from building import Building
from module import Module

imageFolder_Tiered = '../resources/images/tiered/'
imageFolder_Single_64x64 = '../resources/images/single_64x64/'

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
recipes = ['Advanced Oil Processing', 'Heavy Oil Cracking to Light Oil']
imageFilePath = imageFolder_Tiered + 'light-oil.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Heavy Oil"
stackSize = None
recipes = ['Advanced Oil Processing', 'Coal Liquefaction']
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

name = "Steam"
stackSize = None
recipes = []
imageFilePath = imageFolder_Tiered + 'steam.png'
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

name = "Rocket Fuel"
stackSize = 10
recipes = ['Rocket Fuel']
imageFilePath = imageFolder_Tiered + 'rocket-fuel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Solid Fuel"
stackSize = 50
recipes = ['Solid Fuel From Light Oil', 'Solid Fuel From Petroleum', 'Solid Fuel From Heavy Oil']
imageFilePath = imageFolder_Tiered + 'solid-fuel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Rocket Control Unit"
stackSize = 10
recipes = ["Rocket Control Unit"]
imageFilePath = imageFolder_Tiered + 'rocket-control-unit.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
Logistics Items
"""
name = "Pipe"
stackSize = 100
recipes = ['Pipe']
imageFilePath = imageFolder_Tiered + 'pipe.png'
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

name = "Underground Belt"
stackSize = 50
recipes = ['2x Underground Belt']
imageFilePath = imageFolder_Tiered + 'underground-belt.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Splitter"
stackSize = 50
recipes = ['Splitter']
imageFilePath = imageFolder_Tiered + 'splitter.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Fast Transport Belt"
stackSize = 100
recipes = ['Fast Transport Belt']
imageFilePath = imageFolder_Tiered + 'fast-transport-belt.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Fast Underground Belt"
stackSize = 50
recipes = ['2x Fast Underground Belt']
imageFilePath = imageFolder_Tiered + 'fast-underground-belt.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Fast Splitter"
stackSize = 50
recipes = ['Fast Splitter']
imageFilePath = imageFolder_Tiered + 'fast-splitter.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Express Transport Belt"
stackSize = 100
recipes = ['Express Transport Belt']
imageFilePath = imageFolder_Tiered + 'express-transport-belt.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Express Underground Belt"
stackSize = 50
recipes = ['2x Express Underground Belt']
imageFilePath = imageFolder_Tiered + 'express-underground-belt.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Express Splitter"
stackSize = 50
recipes = ['Express Splitter']
imageFilePath = imageFolder_Tiered + 'express-splitter.png'
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
recipes = ['3x Utility Science Pack']
imageFilePath = imageFolder_Tiered + 'utility-science-pack.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Satellite"
stackSize = 1
recipes = ['Satellite']
imageFilePath = imageFolder_Tiered + 'satellite.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Rocket Part"
stackSize = 5
recipes = ['Rocket Part']
imageFilePath = imageFolder_Tiered + 'rocket-part.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Space Science Pack"
stackSize = 200
recipes = ['1000x Space Science Pack']
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

name = "Wall"
stackSize = 100
recipes = ['Wall']
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

name = "Radar"
stackSize = 50
recipes = ['Radar']
imageFilePath = imageFolder_Tiered + 'radar.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

"""
TODO: Energy stuffs
"""

name = "Solar Panel"
stackSize = 50
recipes = ['Solar Panel']
imageFilePath = imageFolder_Tiered + 'solar-panel.png'
itemDict[name] = Item(name, stackSize, recipes, imageFilePath)

name = "Accumulator"
stackSize = 50
recipes = ['Accumulator']
imageFilePath = imageFolder_Tiered + 'accumulator.png'
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

name = 'Oil Refinery'
stackSize = 10
moduleSlots = 3
powerConsumption = 434
craftingSpeed = 1
recipes = ['Oil Refinery']
imageFilePath = imageFolder_Tiered + 'oil-refinery.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Rocket Silo'
stackSize = 1
moduleSlots = 4
powerConsumption = 4000
craftingSpeed = 1
recipes = ['Rocket Silo']
imageFilePath = imageFolder_Tiered + 'rocket-silo.png'
itemDict[name] = Building(name, stackSize, moduleSlots, craftingSpeed, powerConsumption, recipes, imageFilePath)

name = 'Chemical Plant'
stackSize = 10
moduleSlots = 3
powerConsumption = 217
craftingSpeed = 1
recipes = ['Chemical Plant']
imageFilePath = imageFolder_Tiered + 'chemical-plant.png'
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

name = "Beacon"
stacksize = 10
moduleSlots = 2
powerConsumption = 480
stackable = True
recipes = ['Beacon']
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
speedEffect = 0.5
powerEffect = 0.7
recipes = ['Speed Module 3']
imageFilePath = imageFolder_Single_64x64 + 'speed-3.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Productivity Module 1"
stackSize = 50
moduleType = 'p'
productivityEffect = 0.04
speedEffect = -0.05
powerEffect = 0.4
recipes = ['Productivity Module 1']
imageFilePath = imageFolder_Single_64x64 + 'productivity-1.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Productivity Module 2"
stackSize = 50
moduleType = 'p'
productivityEffect = 0.06
speedEffect = -0.1
powerEffect = 0.6
recipes = ['Productivity Module 2']
imageFilePath = imageFolder_Single_64x64 + 'productivity-2.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Productivity Module 3"
stackSize = 50
moduleType = 'p'
productivityEffect = 0.1
speedEffect = -0.15
powerEffect = 0.8
recipes = ['Productivity Module 3']
imageFilePath = imageFolder_Single_64x64 + 'productivity-3.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Efficiency Module 1"
stackSize = 50
moduleType = 'e'
productivityEffect = 0
speedEffect = 0
powerEffect = -0.3
recipes = ['Efficiency Module 1']
imageFilePath = imageFolder_Single_64x64 + 'effectivity-1.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Efficiency Module 2"
stackSize = 50
moduleType = 'e'
productivityEffect = 0
speedEffect = 0
powerEffect = -0.4
recipes = ['Efficiency Module 2']
imageFilePath = imageFolder_Single_64x64 + 'effectivity-2.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)

name = "Efficiency Module 3"
stackSize = 50
moduleType = 'e'
productivityEffect = 0
speedEffect = 0
powerEffect = -0.5
recipes = ['Efficiency Module 3']
imageFilePath = imageFolder_Single_64x64 + 'effectivity-3.png'
itemDict[name] = Module(name, stackSize, moduleType, productivityEffect, speedEffect, powerEffect, recipes, imageFilePath)