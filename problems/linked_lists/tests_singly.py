import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_push(self):
        '''
        checks if an element is added at the end of the linked list 
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
        "checks if an element is deleted at the end of the linked list"
        ll = SinglyLinkedList()
        ll.push(5)
        ll.push(10)
        ll.push(15)
        ll.pop()
        self.assertEqual(ll.to_list(), [5, 10])
        ll.pop()
        self.assertEqual(ll.to_list(), [5])
        ll.pop()
        self.assertEqual(ll.to_list(), [])

    def test_len(self):
        ll = SinglyLinkedList()
        ll.push(5)
        ll.push(10)
        ll.push(15)
        self.assertEqual(ll.len(), 3)
        ll.pop()
        ll.pop()
        ll.pop()
        self.assertEqual(ll.len(), 0)

if __name__ == '__main__':
    unittest.main()