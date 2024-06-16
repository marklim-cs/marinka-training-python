'''
Data structures: doubly linked lists
+ bubble sort
'''
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        '''
        returns the length of the linked list
        '''
        length = 0
        if self.head is None:
            return length

        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def to_list_reverse(self) -> list:
        '''
        traverses throught the list starting from the last element of the doubly linked list
        '''
        node = self.head

        if node is None:
            return []

        make_list = []
        while node.next is not None:
            node = node.next
        while node is not None:
            make_list.append(node.data)
            node = node.prev

        return make_list

    def push_front(self, data):
        '''
        ads an element at the beginning of a doubly linked list
        '''
        ns = Node(data)
        if self.head is None:
            self.head = ns
            self.tail = ns
            return

        ns.next = self.head
        self.head.prev = ns
        self.head = ns

    def push_back(self, data):
        '''
        ads an element at the end of a doubly linked list
        '''
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ne
        ne.prev = node

    def insert(self, data, position):
        '''
        ads an element at the specified position of a doubly linked list
        '''
        ns = Node(data)
        if self.head is None:
            self.head = ns
            return

        node = self.head
        for _ in range(0, position-1):
            node = node.next

        ns.prev = node
        ns.next = node.next
        node.next.prev = ns
        node.next = ns

    def pop_front(self):
        '''
        removes an element at the beginning of the doubly linked list and returns its value,
        returns None if the list is empty or contained only one element
        '''
        if self.head is None:
            return None
        if self.head.next is None:
            pop_element = self.head.data
            self.head = None
            return pop_element

        pop_element = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return pop_element

    def pop_back(self):
        '''
        removes an element at the end of the doubly linked list and returns its value,
        returns None if the list is empty or contained only one element
        '''
        if self.head is None:
            return None
        if self.head.next is None:
            pop_element = self.head.data
            self.head = None
            return pop_element

        previous_node = self.head
        current_node = self.head.next

        while current_node.next is not None:
            current_node = current_node.next
            previous_node = previous_node.next
        pop_element = current_node.data
        current_node.prev = None
        previous_node.next = None
        return pop_element

    def remove(self, position):
        '''
        removes an element at the specified position of a doubly linked list and returns its value,
        returns None if the list is empty
        '''
        if position < 0 or position >= self.__len__():
            raise IndexError(f"Position out of range, list's length is {self.__len__()}")

        if self.head is None:
            return None
        if self.head.next is None:
            pop_element = self.head
            self.head = None
            return pop_element

        previous_node = self.head
        current_node = self.head.next

        if position == 0:
            pop_element = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return pop_element

        for _ in range(1, position):
            previous_node = current_node
            current_node = current_node.next
        pop_element = current_node.data

        previous_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = previous_node

        return pop_element

    def to_list(self) -> list:
        '''
        converts a linked list to regular Python list
        '''
        if self.head is None:
            return []

        to_list = []
        current_node = self.head
        while current_node is not None:
            to_list.append(current_node.data)
            current_node = current_node.next
        return to_list
