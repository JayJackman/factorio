"""
Filename: desired_ingredient_frame.py
Date Created: 6/26/2021
"""

import tkinter as tk
from tkinter import simpledialog

import utils as utils
from plan import Plan
from ingredient import Ingredient
from dictionaries.items import itemDict

class DesiredIngredientFrame(tk.Frame):
    def __init__(self, parent, desiredIngredient: Ingredient, isRoot: bool = False):
        tk.Frame.__init__(self, parent, borderwidth=1, relief='groove')

        self.desiredIngredient = desiredIngredient
        self.isRoot = isRoot

        self.desired_ingredient_changed_callback_function = utils.emptyCallback

        self.columnconfigure(0, weight=1)

        # Set up the Label that just says desired
        self.desiredLabel = tk.Label(self, text="Desired Ingredient:")
        self.desiredLabel.grid(row=0, column=0, pady=5)

        # This frame holds the icon and amount labels
        self.desiredIngredientSubFrame = tk.Frame(self)
        self.desiredIngredientSubFrame.grid(row=1, column=0, padx=5, pady=5)

        # Desired Ingredient Icon Label
        self.desiredIngredientIcon = utils.getIcon(self.desiredIngredient.item.imageFile)
        self.desiredIngredientIconLabel = tk.Label(self.desiredIngredientSubFrame, image=self.desiredIngredientIcon)
        self.desiredIngredientIconLabel.grid(row=0, column=0, padx=5, pady=5)

        # Desired Ingredient Amount Label
        text = self.desiredIngredient.name + ' ({amount:.2f}/s)'.format(amount=self.desiredIngredient.amount)
        self.desiredIngredientAmountLabel = tk.Label(self.desiredIngredientSubFrame, text=text)
        self.desiredIngredientAmountLabel.grid(row=0, column=1, padx=5, pady=5)

        if self.isRoot:
            self.changeButton = tk.Button(self, text="Change", command=self.onChangeButtonClicked)
            self.changeButton.grid(row=2, column=0, padx=5, pady=5)

    def onChangeButtonClicked(self):
        newIngredientName = simpledialog.askstring(title='Change Ingredient', prompt='Enter new ingredient:')
        if newIngredientName is None:
            return

        # make sure the name is valid
        while newIngredientName not in itemDict:
            newIngredientName = simpledialog.askstring(title='Change Ingredient', prompt = 'Invalid ingredient; try again:')
            if newIngredientName is None:
                return

        amount = simpledialog.askfloat(title='Amount /s', prompt='Enter desired amount per second:')

        self._refresh(Ingredient(newIngredientName, amount))

        self.desired_ingredient_changed_callback_function(self.desiredIngredient)

    def _refresh(self, ingredient: Ingredient):
        self.desiredIngredient = ingredient

        self.desiredIngredientIcon = utils.getIcon(self.desiredIngredient.item.imageFile)
        self.desiredIngredientIconLabel.configure(image=self.desiredIngredientIcon)

        text = self.desiredIngredient.name + ' ({amount:.2f}/s)'.format(amount=self.desiredIngredient.amount)
        self.desiredIngredientAmountLabel.configure(text=text)

    def refresh(self, plan: Plan):
        self._refresh(plan.desiredIngredient)

    def configureCallback(self, callbackFunction):
        self.desired_ingredient_changed_callback_function = callbackFunction