import unittest
from .priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_push(self):
        arr = PriorityQueue()
        arr.push(5, "banana")
        arr.push(1, "apple")
        arr.push(3, "cat")
        arr.push(7, "ape")
        arr.push(2, "cow")
        arr.push(4, "bee")
        self.assertEqual(arr.show(), [(1, "apple"), (2, "cow"), (3, "cat"), (7, "ape"), (5, "banana"), (4, "bee")])

    def test_emty_queue(self):
        arr = PriorityQueue()
        self.assertEqual(arr.show(), [])

    def test_pop(self):
        arr = PriorityQueue()
        arr.push(5, "banana")
        arr.push(1, "apple")
        arr.push(3, "cat")
        arr.push(7, "ape")
        arr.push(2, "cow")
        arr.push(4, "bee")
        self.assertEqual(arr.pop(), (1, "apple"))

    def test_pop_empty(self):
        arr = PriorityQueue()
        self.assertEqual(arr.pop(), None)

if __name__ == "__main__":
    unittest.main()