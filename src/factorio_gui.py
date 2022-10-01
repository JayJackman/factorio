"""
Filename: factorio_gui.py
Date Created: 6/5/2021
"""

import tkinter as tk

from planner_tree import PlannerTree, PlanNode
from planner_tree_frame import PlannerTreeFrame
from plan_viewer_frame import PlanViewerFrame
from total_statistics_frame import TotalStatisticsFrame
from ingredient import Ingredient
from plan import Plan


class Settings:
    defaultIngredient = Ingredient('Electronic Circuit', 1)

class FactorioGui(tk.Frame):
    def __init__(self, parent, desiredIngredient: Ingredient = Settings.defaultIngredient):
        tk.Frame.__init__(self, parent)

        self.rootNode = PlannerTree.createTree(Plan(desiredIngredient))

        self.topFrame = tk.Frame(self)
        self.topFrame.grid(row=0, column=0, sticky='nsew')
        # self.topFrame.columnconfigure([0,1], weight=1)

        """
        Set up the Tree on the left hand side
        """
        self.plannerTreeFrame = PlannerTreeFrame(self.topFrame, self.rootNode)
        self.plannerTreeFrame.grid(row=0, column=0, sticky='nsew')
        self.plannerTreeFrame.configurePlanNodeCallback(self.onPlanNodeClicked)

        """
        Set up the Plan Configurator/Viewer in the middle
        """
        self.planViewFrame = PlanViewerFrame(self.topFrame, self.rootNode)
        self.planViewFrame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.planViewFrame.configureSaveCallback(self.onPlanNodeChanged)

        """
        Set up the total statistics frame on the bottom
        """
        self.totalStatisticsFrame = TotalStatisticsFrame(self, self.rootNode)
        self.totalStatisticsFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.totalStatisticsFrame.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, minsize=self.plannerTreeFrame.getMinWidth())
        self.columnconfigure(1, weight=1)

    def onPlanNodeChanged(self, oldNode: PlanNode, newPlan: Plan):
        """
        This is called when a specific node of the tree has been changed. This will be called from the PlanViewerFrame
        after it saves edits. This function will refresh the Plan Tree to account for the edits made.
        :param oldNode: The node of the PlannerTree that was edited
        :param newPlan: The new Plan that will be used to create a new sub-tree
        :return: The new, edited node of the tree
        """
        # If nothing changed, don't do anything
        if newPlan is None:
            print("New plan is none")
            return

        if newPlan.recipe.name == 'Treat As Raw (Always)':
            print("Recipe changed to always raw, applying to whole tree.")
            self.rootNode.applyRawIngredient(newPlan.desiredIngredient.item)
            newNode = oldNode

        # BEGIN NEW CODE
        elif newPlan.recipe.name == oldNode.plan.recipe.name:
            # if we havent changed the recipe, we want to preserve the beacons/modules/buildings/etc. for our children
            # but we need to update the ingredient amounts (productivity modules)
            print("Recipe didnt change, updating ingredients for subtree")

            self.updateNode(oldNode, newPlan)
            newNode = oldNode

        # TODO: make it so that we dont overwrite beacons of children when saving
        # Create the new tree (stemmed from the current plan node)
        # END NEW CODE
        else:
            print("recipe changed, recreating tree")
            #If the recipe changed, recreate the whole subtree
            newNode = PlannerTree.createTree(newPlan)

            # if we are the root of the tree, we are done; we do not need to add our parent
            if oldNode.parent is None:
                self.rootNode = newNode
            # Add the new node and delete the old node
            else:
                oldNode.parent.addChildNode(newNode)
                oldNode.delete()

        self.refreshPlannerTreeFrame()
        self.totalStatisticsFrame.refresh(self.rootNode)
        # print("newNode:", newNode)
        return newNode

    def updateNode(self, node: PlanNode, plan: Plan):
        print("updating node with plan:", plan.recipe.name)
        node.plan = Plan.copy(plan)
        ingredients = plan.calculateRequiredInputsForDesiredOutput()

        for child in node.children:
            ingredientName = child.plan.desiredIngredient.name
            # TODO: This is garbage. IngredientList needs to be way better than it is
            for i, ingredient in enumerate(ingredients.getIngredients()):
                if ingredient.name == ingredientName:
                    ingredientAmount = ingredient.amount
            ingredient = Ingredient(ingredientName, ingredientAmount)

            newPlan = Plan(ingredient, child.plan.recipe, child.plan.building, child.plan.buildingModules.copy(), child.plan.beaconModules.copy())
            self.updateNode(child, newPlan)


    def onPlanNodeClicked(self, planNode: PlanNode):
        """
        This is called when we click a plan node in our PlannerTreeFrame
        :param planNode:
        :return:
        """
        if self.planViewFrame.isDirty():
            print('Dirty! dont change me!')
            return
        self.planViewFrame.destroy()
        self.planViewFrame = PlanViewerFrame(self.topFrame, planNode)
        self.planViewFrame.grid(row=0, column=1, sticky='nsew')
        self.planViewFrame.configureSaveCallback(self.onPlanNodeChanged)

    def refreshPlannerTreeFrame(self):
        self.plannerTreeFrame.destroy()
        self.plannerTreeFrame = PlannerTreeFrame(self.topFrame, self.rootNode)
        self.plannerTreeFrame.grid(row=0, column=0, sticky='nsew')
        self.plannerTreeFrame.configurePlanNodeCallback(self.onPlanNodeClicked)
        self.columnconfigure(0, minsize=self.plannerTreeFrame.getMinWidth())


if __name__ == '__main__':
    from ingredient import Ingredient
    from tkinter import PhotoImage

    root = tk.Tk()

    myGui = FactorioGui(root)
    myGui.grid(row=0, column=0, sticky='nsew')

    photo = PhotoImage(file='C:/Users/Jay Jackman/Desktop/Capture.PNG')
    root.iconphoto(True, photo)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # myIngredient = Ingredient('Big Mining Drill', 5)
    # myTree = PlannerTree(myIngredient)
    # myTree.root.printSubgraph()
    #
    #
    # viewer = PlannerTreeFrame(root, myTree)
    # viewer.configure(bg='yellow')
    #
    # viewer.grid(row=0, column=0, sticky='nsew')
    #
    # root.rowconfigure([0,1], weight=1)
    # root.columnconfigure([1], weight=1)
    #
    # NE = tk.Frame(root, bg='red')
    # SE = tk.Frame(root, bg='blue')
    # SW = tk.Frame(root, bg='green')
    #
    # NE.grid(row=0,column=1,sticky='nsew')
    # SE.grid(row=1,column=1,sticky='nsew')
    # SW.grid(row=1,column=0,sticky='nsew')
    #
    # # viewer.pack(fill='both', expand=1)
    # #
    # # asdf = tk.Label(text='ASDFASFDSAFD', bg='blue')
    # # asdf.pack()
    root.mainloop()