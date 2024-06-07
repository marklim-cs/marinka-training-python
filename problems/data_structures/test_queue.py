'''test FIFO'''
import unittest
from .queue_struct import Queue

class TestQueue(unittest.TestCase):
    def test_queue0(self):
        '''checks enqueue, dequeue and is_empty with 0 and 1 element in the list'''
        q = Queue()
        self.assertEqual(len(q), 0)
        q.enqueue(5)
        self.assertEqual(q.to_list(), [5])
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), None)

    def test_empty_queue_to_list_returns_empty_list(self):
        self.assertEqual(Queue().to_list(), [])

    def test_single_element_to_list(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.to_list(), [1])

    def test_to_list_returns_valid_content(self):
        q = Queue()
        for i in range(10):
            q.enqueue(i)

        expected = list(range(10))
        self.assertEqual(q.to_list(), expected)

    def test_deque_from_empty_queue_returns_none(self):
        self.assertEqual(Queue().dequeue(), None)

    def test_queue1(self):
        '''checks removing several elements from the list and IndexError raise'''
        q = Queue()
        q.enqueue(5)
        q.enqueue(3)
        q.enqueue(6)
        q.enqueue(0)
        self.assertEqual(q.to_list(), [5, 3, 6, 0])

if __name__ == '__main__':
    unittest.main()
