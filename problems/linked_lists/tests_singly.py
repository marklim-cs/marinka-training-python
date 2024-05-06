'''tests to check the methods of SinglyLinkedList class'''
import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_push(self):
        '''
        checks adding an element at the end of the linked list 
        and if the linked list is transformed to list
        '''
        ll = SinglyLinkedList()
        self.assertEqual(ll.to_list(), [])
        ll.push(1)
        self.assertEqual(ll.to_list(), [1])
        ll.push(2)
        self.assertEqual(ll.to_list(), [1, 2])
        ll.push(3)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_pop(self):
        "checks deleting an element at the end of the linked list"
        ll = SinglyLinkedList()
        ll.push(5)
        ll.push(10)
        ll.push(15)
        self.assertEqual(ll.pop(), 15)
        self.assertEqual(ll.to_list(), [5, 10])
        self.assertEqual(ll.pop(), 10)
        self.assertEqual(ll.to_list(), [5])
        self.assertEqual(ll.pop(), 5)
        self.assertEqual(ll.to_list(), [])
        self.assertEqual(ll.pop(), None)


    def test_len(self):
        '''checks overriding __len__ magic method'''
        ll = SinglyLinkedList()
        ll.push(5)
        ll.push(10)
        ll.push(15)
        self.assertEqual(len(ll), 3)
        ll.pop()
        ll.pop()
        ll.pop()
        self.assertEqual(len(ll), 0)

    def test_sort(self):
        '''checks the bubble sorting algorithm in singly linked list'''
        ll = SinglyLinkedList()
        ll.push(20)
        self.assertEqual(ll.sort(), [20])
        ll.push(5)
        ll.push(10)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.sort(), [5, 10, 20])
        ll.push(-5)
        ll.push(55)
        ll.push(0)
        ll.push(13)
        self.assertEqual(ll.sort(), [-5, 0, 5, 10, 13, 20, 55])
        ll.pop()
        self.assertEqual(ll.sort(), [-5, 0, 5, 10, 13, 20])
        ll.push(33)
        self.assertEqual(ll.sort(), [-5, 0, 5, 10, 13, 20, 33])

if __name__ == '__main__':
    unittest.main()
