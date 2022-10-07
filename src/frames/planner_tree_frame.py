"""
Filename: planner_tree_frame.py
Date Created: 6/2/2021
"""

import tkinter as tk
from PIL import ImageTk, Image

from planner_tree import PlannerTree
from planner_tree import PlanNode
from functools import partial
import utils

class Settings:
    backgroundColor = 'black'
    treeColor = 'grey'
    buttonBackgroundColor = 'black'
    buttonClickColor = 'grey'

class PlannerTreeFrame(tk.Frame):
    def __init__(self, parent, planNode: PlanNode, **kwargs):
        tk.Frame.__init__(self, parent, kwargs)

        self.root = planNode
        self.planNodeClickCallback = utils.emptyCallback

        # The canvas fills the entire PlannerTreeFrame, so that the area can be scrollable.
        self.canvas = tk.Canvas(self)
        # Place the scrollbar in our frame and set it to scroll the canvas
        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        # Put a frame in the canvas to fill it up with what we want
        self.mainFrame = tk.Frame(self.canvas)

        # Whenever mainFrame changes size, we will call this function. The function modifies canvas' scroll region to
        # have the size of the canvas
        self.mainFrame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # Place the frame into our canvas
        self.canvas.create_window((0, 0), window=self.mainFrame, anchor='nw')

        # Make the scrollbar move on mouse wheel when cursor is in the frame
        self.bind('<Enter>', self.bindMouseWheel)
        self.bind('<Leave>', self.unbindMouseWheel)

        self.mainFrame.configure(bg=Settings.backgroundColor)

        # Have to keep a list of all images so they can render
        self.images = []

        self.createGraph()

        # Draw the things so we can get their widths
        self.mainFrame.update_idletasks()
        self.scrollbar.update_idletasks()

        self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1, minsize=self.mainFrame.winfo_width())
        # self.columnconfigure(1, minsize=self.scrollbar.winfo_width())

        # Add the canvas on the left and the scrollbar on the right
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.scrollbar.grid(row=0, column=1, sticky='nsew')

        # Allow the canvas to set the scrollbar position, as well as set the width to match the mainFrame
        self.canvas.configure(yscrollcommand=self.scrollbar.set, width=self.mainFrame.winfo_width(), highlightthickness=0)

        # Should never see these but might help for debugging
        self.configure(bg='yellow')
        self.canvas.configure(bg='purple')

    def configurePlanNodeCallback(self, callbackFunction):
        self.planNodeClickCallback = callbackFunction

    def bindMouseWheel(self, event):
        self.bind_all("<MouseWheel>", self.onMouseWheel)

    def unbindMouseWheel(self, event):
        self.unbind_all("<MouseWheel>")

    def onMouseWheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def createGraph(self):
        def recursiveCall(node: PlanNode, doneList: list, index: int):
            """
            This function recursively traverses a tree structure and creates labels to view it
            :param node: This is the root node to create a tree viewer from
            :param doneList: This list keeps track of the recursive history of ingredients. It enables us to properly
            draw the tree structure.
            :param index: This index keeps track of how many total nodes we have viewed, so we can expand the tree
            viewer downwards
            :return:
            """
            # Loop through the stack and draw the correct tree parts
            for i, done in enumerate(doneList):
                label = tk.Label(master=self.mainFrame, font=('Courier New CE', 15))
                if i == len(doneList) - 1:
                    if done:
                        label.configure(text='└', bg=Settings.backgroundColor, fg=Settings.treeColor)
                    else:
                        label.configure(text='├', bg=Settings.backgroundColor, fg=Settings.treeColor)
                else:
                    if done:
                        label.configure(text='', bg=Settings.backgroundColor, fg=Settings.treeColor)
                    else:
                        label.configure(text='│', bg=Settings.backgroundColor, fg=Settings.treeColor)
                label.grid(row=index, column=i, sticky='nsew')

            # Create the clickable icon
            icon = utils.getIcon(node.plan.desiredIngredient.item.imageFile)
            self.images.append(icon)
            recipeButton = tk.Button(master=self.mainFrame, image=icon, activebackground=Settings.buttonClickColor, bg=Settings.backgroundColor, relief='raised')
            recipeButton.grid(row=index, column=len(doneList))
            recipeButton.bind("<Button-1>", partial(self.handleButtonPress, node))

            for i, child in enumerate(node.children):
                newList = doneList.copy()
                # If this is the last child, then we mark that the parent is done so we can draw the appropriate part of the graph
                last = True if i == len(node.children) - 1 else False
                newList.append(last)
                # The index is the next row to draw on so that we can expand the graph downwards
                index = recursiveCall(child, newList, index + 1)
            return index
        recursiveCall(self.root, [], 0)

    def getMinWidth(self):
        """
        This function returns the minimum number of pixels to properly draw the graph
        :return:
        """
        self.mainFrame.update_idletasks()
        self.scrollbar.update_idletasks()
        return self.mainFrame.winfo_width() + self.scrollbar.winfo_width()

    def handleButtonPress(self, node: PlanNode, _):
        """
        This function passes the node that was clicked to the owner of this class
        """
        self.planNodeClickCallback(node)

if __name__ == '__main__':
    from ingredient import Ingredient

    myIngredient = Ingredient('Space Science Pack', 5)
    myTree = PlannerTree(myIngredient)
    myTree.root.printSubgraph()

    root = tk.Tk()

    viewer = PlannerTreeFrame(root, myTree)
    viewer.configure(bg='yellow')

    viewer.grid(row=0, column=0, sticky='nsew')

    root.rowconfigure([0,1], weight=1)
    root.columnconfigure([1], weight=1)

    NE = tk.Frame(root, bg='red')
    SE = tk.Frame(root, bg='blue')
    SW = tk.Frame(root, bg='green')

    NE.grid(row=0,column=1,sticky='nsew')
    SE.grid(row=1,column=1,sticky='nsew')
    SW.grid(row=1,column=0,sticky='nsew')

    # viewer.pack(fill='both', expand=1)
    #
    # asdf = tk.Label(text='ASDFASFDSAFD', bg='blue')
    # asdf.pack()
    root.mainloop()