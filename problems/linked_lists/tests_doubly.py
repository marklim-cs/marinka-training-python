"Test the DoublyLinkedList class"
import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_push_front(self):
        "checks if an element is added at the beginning"
        dll = DoublyLinkedList()
        dll.push_front(5)
        self.assertEqual(dll.to_list(), [5])
        dll.push_front(10)
        dll.push_front(20)
        self.assertEqual(dll.to_list(), [20, 10, 5])

    def test_push_back(self):
        "checks if an element is added at the end"
        dll = DoublyLinkedList()
        dll.push_back(5)
        dll.push_back(10)
        dll.push_back(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        dll.push_back(25)
        self.assertEqual(dll.to_list(), [5, 10, 20, 25])
        self.assertEqual(dll.backward_traversal(), [25, 20, 10, 5])

    def test_insert(self):
        "checks if an element is added at the spesified position"
        dll = DoublyLinkedList()
        dll.insert(5, 5)
        self.assertEqual(dll.to_list(), [5])
        dll.push_back(10)
        dll.push_back(20)
        dll.insert(25, 1)
        self.assertEqual(dll.to_list(), [5, 25, 10, 20])
        dll.insert(30, 2)
        self.assertEqual(dll.to_list(), [5, 25, 30, 10, 20])

    def test_pop_front(self):
        "checks if an element is deleted at the beginning"
        dll = DoublyLinkedList()
        dll.push_back(5)
        dll.push_back(10)
        dll.push_back(20)
        dll.pop_front()
        self.assertEqual(dll.to_list(), [10, 20])
        self.assertEqual(dll.pop_front(), 10)
        self.assertEqual(dll.pop_front(), None)

    def test_pop_back(self):
        "checks if an element is deleted at the end"
        dll = DoublyLinkedList()
        dll.push_back(5)
        dll.push_back(10)
        dll.push_back(20)
        self.assertEqual(dll.pop_back(), 20)
        dll.pop_back()
        self.assertEqual(dll.to_list(), [5])
        self.assertEqual(dll.pop_back(), None)

    def test_remove(self):
        "checks if an element is deleted at the spesified position"
        dll = DoublyLinkedList()
        dll.push_back(5)
        dll.push_back(10)
        dll.push_back(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        self.assertEqual(dll.remove(1), 10)
        with self.assertRaises(IndexError):
            dll.remove(10)
        dll.remove(0)
        self.assertEqual(dll.to_list(), [20])

if __name__ == '__main__':
    unittest.main()