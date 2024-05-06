"Test the DoublyLinkedList class"
import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_push_front(self):
        "checks adding an element at the beginning, reverse traversing and to_list"
        dll = DoublyLinkedList()
        dll.push_front(5)
        self.assertEqual(dll.to_list(), [5])
        dll.push_front(20)
        dll.push_front(10)
        self.assertEqual(dll.to_list(), [10, 20, 5])
        self.assertEqual(dll.to_list_reverse(), [5, 20, 10])

    def test_push_back(self):
        "checks adding an element at the end and overriding __len__ magic method"
        dll = DoublyLinkedList()
        dll.push_back(5)
        self.assertEqual(len(dll), 1)
        dll.push_back(10)
        dll.push_back(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        dll.push_back(25)
        self.assertEqual(dll.to_list(), [5, 10, 20, 25])
        self.assertEqual(dll.to_list_reverse(), [25, 20, 10, 5])
        self.assertEqual(len(dll), 4)

    def test_insert(self):
        "checks adding an element at the spesified position"
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
        "checks deleting an element at the beginning"
        dll = DoublyLinkedList()
        dll.push_back(5)
        dll.push_back(10)
        dll.push_back(20)
        dll.pop_front()
        self.assertEqual(dll.to_list(), [10, 20])
        self.assertEqual(dll.pop_front(), 10)
        self.assertEqual(dll.pop_front(), 20)

    def test_pop_back(self):
        "checks deleting an element at the end"
        dll = DoublyLinkedList()
        dll.push_back(5)
        dll.push_back(10)
        dll.push_back(20)
        self.assertEqual(dll.pop_back(), 20)
        dll.pop_back()
        self.assertEqual(dll.to_list(), [5])
        self.assertEqual(dll.pop_back(), 5)
        self.assertEqual(dll.pop_back(), None)
        self.assertEqual(len(dll), 0)

    def test_remove(self):
        "checks deleting an element at the spesified position"
        dll = DoublyLinkedList()
        dll.push_back(5)
        with self.assertRaises(IndexError):
            dll.remove(100500)
        dll.push_back(10)
        dll.push_back(20)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        self.assertEqual(dll.remove(1), 10)
        with self.assertRaises(IndexError):
            dll.remove(10)
        with self.assertRaises(IndexError):
            dll.remove(-10)
        self.assertEqual(dll.to_list(), [5, 20])
        self.assertEqual(dll.remove(0), 5)
        self.assertEqual(len(dll), 1)

if __name__ == '__main__':
    unittest.main()
