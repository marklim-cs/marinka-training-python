"Test the Doubly_linked_list"
import unittest
from doubly_linked_list import Doubly_linked_list

class TestDoublyLinkedList(unittest.TestCase):
    def test_push_at_end(self):
        "checks if an element is added at the end"
        dll = Doubly_linked_list()
        dll.push_at_end(5)
        dll.push_at_end(10)
        dll.push_at_end(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        dll.push_at_end(25)
        self.assertEqual(dll.to_list(), [5, 10, 20, 25])
        self.assertEqual(dll.backward_traversal(), [25, 20, 10, 5])

    def test_push_at_position(self):
        "checks if an element is added at the spesified position"
        dll = Doubly_linked_list()
        dll.push_at_position(5, 5)
        self.assertEqual(dll.to_list(), [5])
        dll.push_at_end(10)
        dll.push_at_end(20)
        dll.push_at_position(25, 1)
        self.assertEqual(dll.to_list(), [5, 25, 10, 20])
        dll.push_at_position(30, 2)
        self.assertEqual(dll.to_list(), [5, 25, 30, 10, 20])

    def test_pop_at_end(self):
        "checks if an element is deleted at the end"
        dll = Doubly_linked_list()
        dll.push_at_end(5)
        dll.push_at_end(10)
        dll.push_at_end(20)
        dll.pop_at_end()
        self.assertEqual(dll.to_list(), [5, 10])
        dll.pop_at_end()
        dll.pop_at_end()
        self.assertEqual(dll.to_list(), [])

    def test_pop_at_position(self):
        "checks if an element is deleted at the spesified position"
        dll = Doubly_linked_list()
        dll.push_at_end(5)
        dll.push_at_end(10)
        dll.push_at_end(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        dll.pop_at_position(2)
        self.assertEqual(dll.to_list(), [5, 10])
        with self.assertRaises(IndexError):
            dll.pop_at_position(10)
        dll.pop_at_position(0)
        self.assertEqual(dll.to_list(), [10])

if __name__ == '__main__':
    unittest.main()