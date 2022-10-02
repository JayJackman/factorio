"""
Filename: recipes.py
Date Created: 10/1/2022
"""

from mods import MODS


""" Now load the recipes"""
if MODS == 'vanilla':
    from dictionaries.recipe_dictionary_vanilla import recipeDict as RECIPE_DICT
elif MODS == 'SE':
    from src.dictionaries.recipe_dictionary_SE import recipeDict as RECIPE_DICT

recipeDict = RECIPE_DICT
