'''
Data structures: singly linked lists
+ bubble sort
'''
class Node:
    '''a Node class for linked lists '''
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        '''adds an element to the last positions of the linked list'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def pop(self):
        '''
        removes the last element from the linked list and returns the value of it
        and returns None if the list is empty or contained only one element
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
        previous_node.next = None
        return pop_element

    def to_list(self) -> list:
        '''converts a linked list to regular Python list'''
        if self.head is None:
            return []

        to_list = []
        current_node = self.head
        while current_node is not None:
            to_list.append(current_node.data)
            current_node = current_node.next
        return to_list

    def __len__(self) -> int:
        '''returns the length of the linked list'''
        length = 0
        if self.head is None:
            return length
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def sort(self):
        '''
        Bubble sort in ascending order, 
        returns None if the list is empty
        '''
        if self.head is None:
            return None

        swapped = True
        while swapped:
            swapped = False
            current_node = self.head

            while current_node.next is not None:
                if current_node.data > current_node.next.data:
                    temp = current_node.data
                    current_node.data = current_node.next.data
                    current_node.next.data = temp
                    swapped = True
                current_node = current_node.next

        return self.to_list()
