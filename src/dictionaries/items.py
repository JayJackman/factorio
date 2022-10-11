"""
Filename: items.py
Date Created: 10/1/2022
"""

from mods import MODS

if MODS == 'vanilla':
    from dictionaries.item_dictionary_vanilla import itemDict as ITEM_DICT
    from dictionaries.item_dictionary_vanilla import BUILDINGS as _buildings

elif MODS == 'SE':
    from src.dictionaries.item_dictionary_SE import itemDict as ITEM_DICT
    # from dictionaries.item_dictionary_SE import BUILDINGS as _buildings

itemDict = ITEM_DICT
BUILDINGS = _buildings
