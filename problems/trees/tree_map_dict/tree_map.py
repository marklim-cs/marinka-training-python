'''
Implement a `TreeMap` data structure, which allows to store
and search key-value pairs (just like python `dict`). 
Interface:
- insert(self, key: int|str, value: object)` - insert/replace a value for a given key
- find(self, key: int|str) -> object | None` - find a value by a key and return it. 
  Returns `None` if key isn't found
- __len__(self) -> int` - wiadomo
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftchild = None
        self.rightchild = None

class TreeMap:
    def __init__(self):
        self._root = None

    def insert(self, key: int|str, value: object):
        self._root = self._insert_recursively(self._root, key, value)

    def _insert_recursively(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.leftchild = self._insert_recursively(node.leftchild, key, value)
        elif key > node.key:
            node.rightchild = self._insert_recursively(node.rightchild, key, value)
        else:
            node.value = value
        return node

    def find(self, key: int|str) -> object | None:
        found_value = self._find_recursively(self._root, key)
        return found_value

    def _find_recursively(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._find_recursively(node.leftchild, key)
        elif key > node.key:
            return self._find_recursively(node.rightchild, key)
        elif key == node.key:
            return node.value
        else:
            return None

    def __len__(self) -> int:
        count = self._len_recursive(self._root)
        return count

    def _len_recursive(self, node):
        if node is None:
            return 0

        count = 1
        count += self._len_recursive(node.leftchild)
        count += self._len_recursive(node.rightchild)
        return count
