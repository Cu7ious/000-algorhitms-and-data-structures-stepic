#! /usr/bin/env python3
import sys

class Node:
    def __init__(self, val, p, offs):
        self.node = {
            value: val,
            parent: p,
            offsprings: offs
        }

        return self.node

class Tree:
    def __init__(self, tree_arr):
        self.height = 1

        node_value = tree_arr.index(-1)
        children = self.nodes_children(node_value, tree_arr)

        node = create_node(node_value, None, children)

    def create_node(value, children):
        self.node = Node(value, parent, children)

    def nodes_children(node, tree):
        n = tree.count(node)
        kids = []

        while (n):
            if (len(kids) is 0):
                kids.append(tree.index(node))
            else:
                kids.append(tree.index(node, kids[-1] + 1))
            n -= 1

        return kids




def tree_height(tree):
    """Computes the height of a given thee"""
    
    return height


print(
# tree_height([4, -1, 4, 1, 1])
          #  0   1  2  3  4
# tree_height([-1, 0, 4, 0, 3])
tree_height([9, 7, 5, 5, 2, 9, 9, 9, 2, -1])
           # 0  1  2  3  4  5  6  7  8   9
)
