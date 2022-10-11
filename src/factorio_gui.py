"""
Filename: factorio_gui.py
Date Created: 6/5/2021
"""

import tkinter as tk

from building import Building
from planner_tree import PlannerTree, PlanNode
from ingredient import Ingredient
from plan import Plan

from frames.planner_tree_frame import PlannerTreeFrame
from frames.plan_viewer_frame import PlanViewerFrame
from frames.total_statistics_frame import TotalStatisticsFrame
from frames.configurator_frame import ConfiguratorFrame


class Settings:
    defaultIngredient = Ingredient('Space Science Pack', 0.75)


class FactorioGui(tk.Frame):
    def __init__(self, parent, desiredIngredient: Ingredient = Settings.defaultIngredient):
        tk.Frame.__init__(self, parent)

        self.rootNode = PlannerTree.createTree(Plan(desiredIngredient))
        # self.configure(bg='blue')

        self.topFrame = tk.Frame(self)
        self.topFrame.grid(row=0, column=0, sticky='nsew')
        # self.topFrame.configure(bg='red')
        # self.topFrame.columnconfigure([0,1], weight=1)
        self.topFrame.rowconfigure(0, weight=1)

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
        Set up the Global Configurator Frame on the right
        """
        self.globalConfigFrame = ConfiguratorFrame(self.topFrame)
        self.globalConfigFrame.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        self.globalConfigFrame.configureBuildingCallback(self.onGlobalBuildingChanged)

        """
        Set up the total statistics frame on the bottom
        """
        self.totalStatisticsFrame = TotalStatisticsFrame(self, self.rootNode)
        self.totalStatisticsFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.totalStatisticsFrame.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, minsize=self.plannerTreeFrame.getMinWidth())
        self.columnconfigure([0,1], weight=1)

    def onPlanNodeChanged(self, oldNode: PlanNode, newPlan: Plan):
        """
        This is called when a specific node of the tree has been changed. This will be called from the PlanViewerFrame
        after it saves edits. This function will refresh the Plan Tree to account for the edits made.
        :param oldNode: The node of the PlannerTree that was edited
        :param newPlan: The new Plan that will be used to create a new sub-tree
        :return: The new, edited node of the tree
        """
        # print('old node:', oldNode)
        # print('new plan:', newPlan)
        # If nothing changed, don't do anything
        if newPlan is None:
            # print('none')
            return

        if newPlan.recipe.name == 'Treat As Raw (Always)':
            self.rootNode.applyRawIngredient(newPlan.desiredIngredient.item)
            newNode = oldNode

        elif newPlan.recipe == oldNode.plan.recipe:
            # Here, we haven't changed the recipe but need to update our children for modified ingredient amounts
            self.updateNode(oldNode, newPlan)
            newNode = oldNode

        else:
            # If the recipe changed, recreate the whole subtree
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

    # TODO: Move this to PlanNode?
    def updateNode(self, node: PlanNode, plan: Plan):
        node.plan = Plan.copy(plan)
        ingredients = plan.calculateRequiredInputsForDesiredOutput()

        for child in node.children:
            ingredientName = child.plan.desiredIngredient.name
            ingredientAmount = ingredients[ingredientName].amount

            ingredient = Ingredient(ingredientName, ingredientAmount)

            newPlan = Plan(ingredient, child.plan.recipe, child.plan.building, child.plan.buildingModules.copy(),
                           child.plan.beaconModules.copy())
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
        # self.columnconfigure(0, minsize=self.plannerTreeFrame.getMinWidth())
        # self.columnconfigure(1, minsize=self.planViewFrame.getMinWidth())

    def onGlobalBuildingChanged(self, building: Building):
        # If we are in the middle of changing a specific node, we don't want to muck things up. Force the user to save.
        if self.planViewFrame.isDirty():
            print('Dirty! dont change me!')
            return

        currentNode = self.planViewFrame.planNode
        self.planViewFrame.destroy()

        self.rootNode.applyBuilding(building.name)
        self.refreshPlannerTreeFrame()
        self.totalStatisticsFrame.refresh(self.rootNode)

        self.planViewFrame = PlanViewerFrame(self.topFrame, currentNode)
        self.planViewFrame.grid(row=0, column=1, sticky='nsew')
        self.planViewFrame.configureSaveCallback(self.onPlanNodeChanged)



if __name__ == '__main__':
    from tkinter import PhotoImage
    from dictionaries.items import itemDict

    root = tk.Tk()

    myGui = FactorioGui(root)

    # myGui.rootNode.applyBuilding('Assembling Machine 3')
    # myGui.rootNode.setAllBuildingModules(itemDict['Productivity Module 3'])
    myGui.grid(row=0, column=0, sticky='nsew')

    # photo = PhotoImage(file='C:/Users/Jay Jackman/Desktop/Capture.PNG')
    photo = PhotoImage(file='../resources/images/single_64x64/scrap.png')
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
