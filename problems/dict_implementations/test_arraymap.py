import unittest
from .compare_dicts import ArrayMap

class TestArrayMap(unittest.TestCase):
    def test_insert(self):
        arr = ArrayMap()
        arr.insert(1, "apple")
        arr.insert(2, "banana")
        self.assertEqual(arr.repres(), [(1, "apple"), (2, "banana")])
        arr.insert(2, "kiwi")
        self.assertEqual(arr.repres(), [(1, "apple"), (2, "kiwi")])
        self.assertEqual(len(arr), 2)
    def test_find_len(self):
        arr = ArrayMap()
        arr.insert(1, "apple")
        arr.insert(2, "banana")
        self.assertEqual(arr.find(2), (2, "banana"))

if __name__ == '__main__':
    unittest.main()