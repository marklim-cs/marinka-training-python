'''
checking if binary tree is full binary tree
an empty tree is by definition a full binary tree 
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.leftchild = None
        self.rightchild = None

def is_full_tree(root):
    if root is None:
        return True

    if root.leftchild is None and root.rightchild is None:
        return True

    if root.leftchild is not None and root.rightchild is not None:
        return (is_full_tree(root.leftchild) and is_full_tree(root.rightchild))

    return False