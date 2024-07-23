'''
Compare 3 dictionary implementations:
- python dict
- TreeMap
- ArrayMap

Write a console app (use python argparse module) which takes the following cmdline arguments:
- storage: "dict" | "tree" | "array" - data structure used for data storage
- src : path - path to a file containing some english words

The app should then find a word frequency map using the specified data structure
and measure how much time the calculation took (using python `timeit`). 

Print time (in miliseconds) to the console

Try with files containing 100, 10000, 1000000 words

Implement a ArrayMap data structure, which allows to store
and search key-value pairs (just like python `dict`). Interface:
- insert(self, key, value) - insert/replace a value for a given key
- find(self, key) -> object | None - find a value by a key and return it. 
Returns None if key isn't found
- __len__(self) -> int - wiadomo

ArrayMap should use one or more python list fields to store data
'''

class Node:
    def __init__(self, key, value):
        self.key = key or None
        self.value = value or None
        self.leftchild = None
        self.rightchild = None

class TreeMap:
    def __init__(self):
        self._root = None

    def insert(self, key: int|str, value: object):
        self._root = self._insert_recursively(self._root, key, value)

    def _insert_recursively(self, node, key, value):
        if node is None:
            node = Node(key, value)
            return node

        if key < node.key:
            self._insert_recursively(node.leftchild, key, value)
        elif key > node.key:
            self._insert_recursively(node.rightchild, key, value)
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
            self._find_recursively(node.leftchild, key)
        elif key > node.key:
            self._find_recursively(node.rightchild, key)
        elif key == node.key:
            return node.value
        else:
            return None

    def __len__(self):
        length = self._len_recursively(self._root)
        return length

    def _len_recursively(self, node):
        if node is None:
            return 0

        count = 1
        count += self._len_recursively(node.leftchild)
        count += self._len_recursively(node.rightchild)
        return count

    def __iter__(self):
        pass

    def _iter_recursively(self, node):
        if node is None:
            return

        self._iter_recursively(node.leftchild)
        yield (node.key, node.value)
        self._iter_recursively(node.rightchild)

class PythonDict:
    def __init__(self):
        self.dict = {}

    def insert(self, key, value):
        self.dict[key] = value

    def find(self, key):
        return self.dict.get(key)

class ArrayMap:
    def __init__(self):
        self.keys = []
        self.values = []


    def insert(self, key: int|str, value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def find(self, key) -> object | None:
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        return None

    def __len__(self) -> int:
        if len(self.keys) == len(self.values):
            return len(self.keys)
        else:
            raise ValueError("size doesn't match, the ArrayMap is not build properly")

    def repres(self):
        'for tests'
        return self.keys, self.values
