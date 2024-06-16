'''LIFO'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def push(self, data):
        '''ads an element at the end of the list'''
        node = Node(data)
        if self._tail is None:
            self._head = node
            self._tail = node
            self._length += 1
            return

        node.next = self._tail
        self._tail = node
        self._length += 1

    def pop(self):
        '''removes an element from the end of the list'''
        self._length = max(self._length-1, 0)
        if self._tail is None:
            return None

        if self._tail.next is None:
            popped_element = self._tail.data
            self._tail = None
            return popped_element

        popped_element = self._tail.data
        self._tail = self._tail.next
        if self._tail is None:
            self._head = None

        return popped_element

    def to_list(self) -> list:

        if self._tail is None:
            return []

        node_list = []
        current_node = self._tail
        while current_node is not None:
            node_list.append(current_node.data)
            current_node = current_node.next
        node_list.reverse()
        return node_list

    def __len__(self) -> int:
        return self._length

    def top(self):
        if self._tail is None:
            return None
        return self._tail.data
