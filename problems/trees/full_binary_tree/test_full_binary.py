import unittest
from .full_binary_tree import is_full_tree, Node

class TestFullBinaryTree(unittest.TestCase):
    '''stack test'''
    def test_is_full_binary(self):
        root = Node(1)
        root.leftchild = Node(2)
        root.rightchild = Node(3)
        root.leftchild.leftchild = Node(4)
        root.leftchild.rightchild = Node(5)
        self.assertEqual(is_full_tree(root), True)

if __name__ == '__main__':
    unittest.main()