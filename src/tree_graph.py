"""
Filename: tree_graph.py
Date Created: 5/29/2021
"""
import tkinter as tk
from functools import partial
from typing import List


class Node:

    def __init__(self, obj, parent=None):
        self.obj = obj
        self.parent = parent
        self.children: List[Node] = []

        self.labelText = str(obj)

    def isRoot(self):
        return True if self.parent is None else False

    def isLeaf(self):
        return True if self.children == [] else False

    def getDepth(self):
        """
        returns the depth of the node. 0-indexed, so the root node is a depth of 0
        :return: 0-indexed depth of the node
        """
        depth = 0
        parent = self.parent
        while parent is not None:
            depth += 1
            parent = parent.parent
        return depth

    def addChild(self, obj):
        newNode = Node(obj, parent=self)
        self.children.append(newNode)

    def addChildNode(self, node):
        self.children.append(node)
        node.parent = self

    def delete(self):
        while not self.isLeaf():
            self.children[0].delete()
        if self.parent is not None:
            self.parent.children.remove(self)
        else:
            print("\033[93mWarning: Attempting to delete root node\033[0m")
        del self

    def size(self):
        """
        Returns the number of total nodes in the tree beneath the node (including the node)
        :return: Number of total nodes
        """

        def subgraphSize(node: Node):
            toReturn = 1
            for child in node.children:
                toReturn += subgraphSize(child)
            return toReturn

        return subgraphSize(self)

    def printSubgraph(self):
        def recursiveCall(node, doneList, last: bool):
            # Draw the right stuff
            for i, done in enumerate(doneList):
                if i == len(doneList) - 1:  # Last
                    if last:  # Last child
                        print('└ ', end='')
                    else:
                        print('├ ', end='')
                else:
                    if done is True:
                        print("  ", end='')
                    else:
                        print("│ ", end='')
            print(node.obj)
            for i, child in enumerate(node.children):
                newList = doneList.copy()
                last = False
                if i == len(node.children) - 1:
                    last = True
                    newList.append(True)
                else:
                    newList.append(False)

                recursiveCall(child, newList, last)

        recursiveCall(self, [], False)

    def __str__(self):
        toReturn = ""
        toReturn += "Node of type " + str(type(self.obj)) + ". Depth: " + str(self.getDepth()) + " children: " + str(
            len(self.children))
        return toReturn


class Tree:
    def __init__(self, root: Node = None):
        self.root = root

    def size(self):
        """
        Returns the number of total nodes in the tree
        :return: Number of total nodes in the tree
        """
        return self.root.size()

    def maxDepth(self) -> int:
        """
        Finds the greatest depth of the graph
        :return: depth of the graph
        """

        def recursiveCall(node: Node, depth: int) -> int:
            toReturn = depth
            for child in node.children:
                toReturn = max(toReturn, recursiveCall(child, depth + 1))
            return toReturn

        return recursiveCall(self.root, 0)

    def numAtDepth(self, targetDepth: int) -> int:
        """
        Calculates the total number of nodes at a given depth
        :param targetDepth: desired depth to count
        :return: number of nodes at the given depth
        """

        def recursiveCall(node: Node, depth: int) -> int:
            count = 0
            if depth == targetDepth:
                return 1
            else:
                for child in node.children:
                    count += recursiveCall(child, depth + 1)
                return count

        return recursiveCall(self.root, 0)


class TreeViewer(tk.Frame):

    def __init__(self, parent, tree: Tree):
        tk.Frame.__init__(self, parent)
        self.tree = tree

        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # These will be used for determining the dimensions of the tree viewer.
        self.depth = self.tree.maxDepth()
        self.numRows = self.tree.size()

        self.scrollable_frame.configure(bg='grey')

        self.createGraph()

        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')

    def createGraph(self):

        def recursiveCall(node: Node, doneList: list, last: bool, index: int):
            for i, done in enumerate(doneList):
                label = tk.Label(master=self.scrollable_frame)
                if i == len(doneList) - 1:
                    if last:
                        label.configure(text='└', bg='grey')
                    else:
                        label.configure(text='├', bg='grey')
                else:
                    if done is True:
                        label.configure(text='', bg='grey')
                    else:
                        label.configure(text='│', bg='grey')

                label.grid(row=index, column=i, sticky="nsew")
            recipeButton = tk.Button(master=self.scrollable_frame, text=node.labelText, activebackground='green',
                                     bg='forest green', relief='raised')
            recipeButton.grid(row=index, column=len(doneList))
            # partial lets us use the callback function with a built-in argument
            recipeButton.bind("<Button-1>", partial(self.handleButtonPress, node))

            for i, child in enumerate(node.children):
                newList = doneList.copy()
                last = False
                if i == len(node.children) - 1:
                    last = True
                    newList.append(True)
                else:
                    newList.append(False)
                index = recursiveCall(child, newList, last, index + 1)
            return index

        recursiveCall(self.tree.root, [], False, 0)

    def handleButtonPress(self, node: Node, _):
        # Here, we will pass out the node to the GUI manager that owns us. Then, they can get info of the Plan by looking at the node.
        print(node)
        pass


if __name__ == "__main__":
    root = Node("A")
    # root.addChild("A")
    # root.addChild("B")
    # root.addChild("C")
    # root.children[0].addChild("A-A")
    # root.children[1].addChild("B-A")
    # root.children[2].addChild("C-A")
    # root.children[2].addChild("C-B")
    # root.children[2].children[0].addChild("C-A-A")
    # root.children[2].children[0].addChild("C-A-B")
    # root.children[2].children[0].children[1].addChild("C-A-B-A")
    # root.children[2].children[0].children[1].addChild("C-A-B-B")
    # root.children[2].children[0].children[0].addChild("C-A-A-A")
    # root.children[0].children[0].addChild("A-A-B")
    # root.addChild("D")
    root.addChild("B")
    root.children[0].addChild("C")
    root.children[0].addChild("D")
    root.children[0].children[1].addChild("F")
    root.addChild("E")
    root.children[1].addChild("G")
    root.children[0].children[1].children[0].addChild("H")
    root.children[0].children[1].children[0].children[0].addChild("J")

    root.children[0].children[1].addChild("I")

    # root.printSubgraph()

    tree = Tree(root)
    # print(tree.size())
    tree.root.printSubgraph()
    print(tree.numAtDepth(2))
    print('number of nodes at 0:', tree.numAtDepth(0))
    print('number of nodes at 1:', tree.numAtDepth(1))
    print('number of nodes at 2:', tree.numAtDepth(2))
    print('number of nodes at 3:', tree.numAtDepth(3))
    print('number of nodes at 4:', tree.numAtDepth(4))
    print('number of nodes at 5:', tree.numAtDepth(5))

    root = tk.Tk()
    viewer = TreeViewer(root, tree)
    viewer.pack(fill='both', expand=1)

    root.mainloop()
    pass
