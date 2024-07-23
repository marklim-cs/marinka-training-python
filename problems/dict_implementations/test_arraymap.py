import unittest
from .compare_dicts import ArrayMap

class TestArrayMap(unittest.TestCase):
    def test_insert(self):
        arr = ArrayMap()
        arr.insert("apple", 1)
        arr.insert("banana", 2)
        arr.insert("kiwi", 3)
        arr.insert("banana", 3)
        self.assertEqual(arr.repres(), (["apple", "banana", "kiwi"], [1, 3, 3]))
        arr.insert("apple", 10)
        self.assertEqual(arr.repres(), (["apple", "banana", "kiwi"], [10, 3, 3]))

    def test_find(self):
        arr = ArrayMap()
        arr.insert("apple", 1)
        arr.insert("banana", 2)
        arr.insert("kiwi", 3)
        arr.insert("banana", 3)
        self.assertEqual(arr.find("banana"), 3)

    def test_find_no_key(self):
        arr = ArrayMap()
        arr.insert("apple", 1)
        arr.insert("banana", 2)
        arr.insert("kiwi", 3)
        arr.insert("banana", 3)
        self.assertEqual(arr.find("salmon"), None)

    def test_find_empty_map(self):
        arr = ArrayMap()
        self.assertEqual(arr.find("salmon"), None)

if __name__ == '__main__':
    unittest.main()