"""
Filename: planner_tree.py
Date Created: 5/31/2021
"""
from tree_graph import Tree
from plan_node import PlanNode
from plan import Plan
from ingredient import Ingredient  # TODO, do a list of ingredients all at the same time


class PlannerTree(Tree):
    def __init__(self, desired: Ingredient = None):
        Tree.__init__(self)
        self.root = self.create(desired)

    @classmethod
    def createTree(cls, plan: Plan):
        newPlanNode = PlanNode(plan=plan)

        for inputIngredient in newPlanNode.plan.calculateRequiredInputsForDesiredOutput().getIngredients():
            newPlanNode.addChildNode(cls.createTree(Plan(inputIngredient)))

        return newPlanNode

    def create(self, desiredIngredient: Ingredient):
        """
        Returns the root node for a tree corresponding to the desired ingredient
        :return:
        """
        """
         TODO: implement check to see if this is a base ingredient. I think this will look like
         if node.plan.treatAsBase:
             return
        """
        newPlanNode = PlanNode(plan=Plan(desiredIngredient))

        for inputIngredient in newPlanNode.plan.calculateRequiredInputsForDesiredOutput().getIngredients():
            newPlanNode.addChildNode(self.create(inputIngredient))

        return newPlanNode


if __name__ == "__main__":
    from tree_graph import TreeViewer
    import tkinter as tk

    myIngredient = Ingredient('Space Science Pack', 1000)
    myTree = PlannerTree(myIngredient)
    myTree.root.printSubgraph()

    root = tk.Tk()
    viewer = TreeViewer(root, myTree)
    viewer.pack(fill='both', expand=1)
    root.mainloop()
