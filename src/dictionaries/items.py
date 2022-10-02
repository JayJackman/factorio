"""
Filename: items.py
Date Created: 10/1/2022
"""

from mods import MODS

if MODS == 'vanilla':
    from dictionaries.item_dictionary_vanilla import itemDict as ITEM_DICT

elif MODS == 'SE':
    from src.dictionaries.item_dictionary_SE import itemDict as ITEM_DICT

itemDict = ITEM_DICT
