"""
Filename: recipe_selector_frame.py
Date Created: 6/26/2021
"""
import tkinter as tk

from recipe import Recipe
from plan import Plan
from recipe_dictionary import recipeDict
import utils

class RecipeSelectorFrame(tk.Frame):
    """
    A RecipeSelectorFrame contains an OptionMenu that selects a recipe. It shows a label of the recipe icon as well.
    """
    def __init__(self, parent, plan: Plan):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.recipe_changed_callback_function = utils.emptyCallback

        self.desiredIngredient = plan.desiredIngredient

        # Stretch horizontally
        self.columnconfigure(0, weight=1)

        # Set up the label that just says recipe
        self.recipeLabel = tk.Label(self, text="Recipe:")
        self.recipeLabel.grid(row=0, column=0, pady=5)

        # This frame holds icon and recipe dropdown labels
        self.recipeSubFrame = tk.Frame(self)
        self.recipeSubFrame.grid(row=1, column=0, padx=5, pady=5)

        # The label that shows the icon
        self.recipeIcon = utils.getIcon(plan.recipe.imageFile)
        self.recipeIconLabel = tk.Label(self.recipeSubFrame, image=self.recipeIcon)
        self.recipeIconLabel.grid(row=0, column=0, padx=5, pady=5)

        # Setup the Recipe Dropdown Menu
        self.recipeOptions = ['Treat as raw', 'Treat as raw (always)'] + self.desiredIngredient.item.recipes
        self.currentRecipeName = plan.recipe.name
        self.selectedRecipe = tk.StringVar(self)
        self.selectedRecipe.set(self.currentRecipeName)
        self.recipeOptionMenu = tk.OptionMenu(self.recipeSubFrame, self.selectedRecipe, *self.recipeOptions, command=self.onOptionMenuChanged)
        self.recipeOptionMenu.grid(row=0, column=1, padx=5, pady=5)

    def configureCallback(self, callbackFunction):
        """
        Configure the callback function. This will be called whenever a new recipe is selected. The callback function
        must accept one parameter which is a Recipe
        :param callbackFunction: A Function accepting exactly one parameter, a Recipe
        """
        self.recipe_changed_callback_function = callbackFunction

    def onOptionMenuChanged(self, recipeName: str):
        """
        When we change the option menu, we must retrieve the correct recipe from the recipe dictionary, and then alert
        our parent that we have changed via the callback function
        :param recipeName: the name of the recipe used to index into recipeDict
        """
        if recipeName == self.currentRecipeName:
            return
        self.currentRecipeName = recipeName

        if recipeName == 'Treat as raw':
            recipe = Recipe.getEmptyRecipe(self.desiredIngredient)
        elif recipeName == 'Treat as raw (always)':
            recipe = Recipe.getAlwaysRawEmptyRecipe(self.desiredIngredient)
        else:
            recipe = recipeDict[recipeName]

        # Update our icon label
        self.recipeIcon = utils.getIcon(recipe.imageFile)
        self.recipeIconLabel.configure(image=self.recipeIcon)

        # Emit the new recipe to parent
        self.recipe_changed_callback_function(recipe)

    def refresh(self, plan: Plan):
        """
        This method accepts a new plan and completely refreshes the layout. It recreates the dropdown menu and the
        selected recipe based on the input plan
        :param plan: the new Plan
        """
        # Set the desired ingredient (used for making raw recipes)
        self.desiredIngredient = plan.desiredIngredient
        self.currentRecipeName = plan.recipe.name

        # Get the new recipe icon
        self.recipeIcon = utils.getIcon(plan.recipe.imageFile)
        self.recipeIconLabel.configure(image=self.recipeIcon)

        # Refresh the option menu
        self.recipeOptions = ['Treat as raw', 'Treat as raw (Always)'] + plan.desiredIngredient.item.recipes

        self.selectedRecipe.set(self.currentRecipeName)
        self.recipeOptionMenu.destroy()
        self.recipeOptionMenu = tk.OptionMenu(self.recipeSubFrame, self.selectedRecipe, *self.recipeOptions, command=self.onOptionMenuChanged)
        self.recipeOptionMenu.grid(row=0, column=1, padx=5, pady=5)

        self.selectedRecipe.set(plan.desiredIngredient.item.recipes[0])

