'''test FIFO'''
import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue0(self):
        '''checks enqueue, dequeue and is_empty with 0 and 1 element in the list'''
        q = Queue()
        self.assertEqual(q.is_empty(), True)
        self.assertEqual(q.enqueue(5), [5])
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), None)
    def test_queue1(self):
        '''checks removing several elements from the list and IndexError raise'''
        q = Queue()
        q.enqueue(5)
        q.enqueue(3)
        q.enqueue(6)
        q.enqueue(0)
        self.assertEqual(q.enqueue(100), [5, 3, 6, 0, 100])
        self.assertEqual(q.dequeue_number_of_elements(2), [6, 0, 100])

if __name__ == '__main__':
    unittest.main()
