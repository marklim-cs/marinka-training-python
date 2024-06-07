'''
First in First out - FIFO
Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it
'''
class Queue:
    def __init__(self):
        '''create a queue'''
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def is_empty(self):
        '''checks queue is empty or is full'''
        return len(self.queue) == 0

    def enqueue(self, element):
        '''add an element'''
        self.queue.append(element)
        return self.queue

    def dequeue(self):
        '''remove an element'''
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def dequeue_number_of_elements(self, remove_elements_number):
        '''remove several elements'''
        if self.is_empty():
            return None

        if remove_elements_number <= 0 or remove_elements_number > len(self.queue):
            raise IndexError(f"Index out of range, queue length is {len(self.queue)}")

        for _ in range(remove_elements_number):
            self.queue.pop(0)
        return self.queue

    def __len__(self) -> int:
        return len(self.queue)
