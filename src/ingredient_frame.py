"""
Filename: ingredient_frame.py
Date Created: 6/26/2021
"""
import tkinter as tk

from ingredient import Ingredient
import utils

class IngredientFrame(tk.Frame):
    """
    An ingredient frame combines two labels to show the image and the amount of an ingredient
    """
    def __init__(self, parent, ingredient: Ingredient, asRate=True):
        tk.Frame.__init__(self, parent)
        self.ingredient = ingredient
        self.asRate = asRate

        self.text = ""
        self.icon = None

        self.iconLabel = tk.Label(self)
        self.iconLabel.grid(row=0, column= 0, padx=5, pady=5)

        self.itemLabel = tk.Label(self, text=self.text)
        self.itemLabel.grid(row=0, column=1, padx=5, pady=5)

        self.refresh(self.ingredient)

    def refresh(self, ingredient):
        self.ingredient = ingredient
        self.icon = utils.getIcon(ingredient.item.imageFile)
        self.iconLabel.configure(image=self.icon)

        if self.asRate:
            self.text = ingredient.item.name + ' ({amount:.2f}/s)'.format(amount=ingredient.amount)
        else:
            self.text = ingredient.item.name + ' ({amount:.2f})'.format(amount=ingredient.amount)

        self.itemLabel.configure(text=self.text)
