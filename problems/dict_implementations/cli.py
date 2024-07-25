import argparse
import timeit
from pathlib import Path
from typing import Callable
import abc
import json

class Dictionary(abc.ABC):
    @abc.abstractmethod
    def insert(self, key, value):
        pass

    @abc.abstractmethod
    def find(self, key) -> object:
        pass

    @abc.abstractmethod
    def repres(self) -> str:
        pass

class Node:
    def __init__(self, key, value):
        self.key = key or None
        self.value = value or None
        self.leftchild = None
        self.rightchild = None

class TreeMap(Dictionary):
    def __init__(self):
        self._root = None

    def insert(self, key: int|str, value: object):
        self._root = self._insert_recursively(self._root, key, value)

    def _insert_recursively(self, node, key, value):
        if node is None:
            node = Node(key, value)
            return node

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

    def repres(self):
        tree = self._iter_recursively(self._root)
        list_tree = list(tree)
        return json.dumps(list_tree, indent=2)

    def _iter_recursively(self, node):
        if node is None:
            return

        if node.leftchild is not None:
            yield from self._iter_recursively(node.leftchild)

        yield (node.key, node.value)

        if node.rightchild is not None:
            yield from self._iter_recursively(node.rightchild)

class PythonDict(Dictionary):
    def __init__(self):
        self.dict = {}

    def insert(self, key, value):
        self.dict[key] = value

    def find(self, key):
        return self.dict.get(key)

    def repres(self):
        return json.dumps(self.dict, indent=2)

class ArrayMap(Dictionary):
    def __init__(self):
        self.keys = []
        self.values = []


    def insert(self, key, value):
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
        result = "\n".join(f"{key} : {value}" for key, value in zip(self.keys, self.values))
        return result

def create_storage(storage_type):
    if storage_type == "tree":
        return TreeMap
    elif storage_type == "array":
        return ArrayMap
    elif storage_type == "dict":
        return PythonDict
    else:
        raise ValueError(f"Unknown storage type: {storage_type}")

def count_words(storage_factory: Callable[[], Dictionary], text_path, result_path):
    with open(text_path, "r", encoding="utf-8") as f:
        textfile = f.read()

    words = textfile.split()
    dictionary = storage_factory()

    for word in words:
        value = dictionary.find(word.lower()) or 0
        dictionary.insert(word.lower(), value + 1)

    representation = dictionary.repres()

    with open(result_path, "w", encoding="utf-8") as fr:
        fr.write(representation)


def execution_time(storage, text_path, result_path):
    start = timeit.default_timer()
    count_words(storage, text_path, result_path)
    end = timeit.default_timer()
    time_taken = end - start
    return time_taken

def main():
    parser = argparse.ArgumentParser(
        description="Measures the time the calculation of word frequency map took"
        )
    parser.add_argument("storage", type=create_storage, help="Storage type (array, tree or dict)")
    parser.add_argument("pathtext")
    parser.add_argument("pathresult")
    arguments = parser.parse_args()

    text_path = Path(arguments.pathtext)
    if not text_path.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)

    result_path = Path(arguments.pathresult)
    if not result_path.exists():
        print("The target file doesn't exist")
        raise SystemExit(1)

    output = execution_time(arguments.storage, text_path, result_path)
    print(f"Time taken: {output}")

if __name__ == "__main__":
    main()