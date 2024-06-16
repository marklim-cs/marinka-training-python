'''
First in First out - FIFO
Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        '''create a queue'''
        self._head = None
        self._tail = None
        self._length = 0

    def __str__(self):
        return str(self.to_list())

    def enqueue(self, data):
        '''add an element'''
        node = Node(data)
        if self._tail is None:
            self._tail = node
            self._head = node
            return

        self._tail.next = node
        self._tail = node
        self._length += 1

    def dequeue(self) -> object | None:
        '''remove an element and return it'''
        self._length = max(self._length-1, 0)

        if self._tail is None:
            return None

        if self._tail == self._head:
            popped_element = self._tail.data
            self._tail = None
            self._head = None
            return popped_element

        popped_element = self._head.data
        self._head = self._head.next
        return popped_element

    def __len__(self) -> int:
        return self._length

    def to_list(self) -> list:
        if self._head is None:
            return []

        arr = []
        current_node = self._head
        while current_node is not None:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr
