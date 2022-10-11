"""
Filename: items.py
Date Created: 10/1/2022
"""

from mods import MODS

if MODS == 'vanilla':
    from dictionaries.item_dictionary_vanilla import itemDict as ITEM_DICT
    from dictionaries.item_dictionary_vanilla import BUILDINGS as _buildings
    from dictionaries.item_dictionary_vanilla import MODULES as _modules

# elif MODS == 'SE':
#     from src.dictionaries.item_dictionary_SE import itemDict as ITEM_DICT
#     # from dictionaries.item_dictionary_SE import BUILDINGS as _buildings
#     from dictionaries.item_dictionary_SE import MOULDES as _modules

itemDict = ITEM_DICT
BUILDINGS = _buildings
MODULES = _modules
