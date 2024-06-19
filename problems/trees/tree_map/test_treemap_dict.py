import unittest
from .tree_map_dict import TreeMap

class TestTreeMap(unittest.TestCase):
    def test_insert(self):
        pass
    def test_find(self):
        n = TreeMap()
        n.insert(10, "value10")
        n.insert(20, "value20")
        n.insert(30, "value30")
        n.insert(11, "value11")
        n.insert(21, "value21")
        n.insert(1, "value1")
        self.assertEqual(n.find(11), "value11")

    def test_len(self):
        n = TreeMap()
        self.assertEqual(len(n), 0)

    def test_len1(self):
        n = TreeMap()
        n.insert(10, "value10")
        n.insert(20, "value20")
        n.insert(30, "value30")
        n.insert(11, "value11")
        n.insert(21, "value21")
        n.insert(1, "value1")
        self.assertEqual(len(n), 6)
if __name__ == '__main__':
    unittest.main()