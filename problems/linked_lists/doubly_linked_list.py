
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Doubly_linked_list:
    def __init__(self):
        self.head = None

    def len(self):
        '''returns the length of the linked list'''
        length = 0
        if self.head is None:
            return length
        else:
            current_node = self.head
            while current_node is not None:
                length += 1
                current_node = current_node.next
            return length

    def backward_traversal(self):
        node = self.head
        if node is None:
            return None

        else:
            make_list = []
            while node.next is not None:
                node = node.next
            while node is not None:
                make_list.append(node.data)
                node = node.prev
            return make_list

    def push_at_beginning(self, data):
        ns = Node(data)
        ns.next = self.head
        self.head.prev = ns
        self.head = ns

    def push_at_end(self, data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ne
        ne.prev = node

    def push_at_position(self, data, position):
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

    def pop_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None

        previous_node = self.head
        current_node = self.head.next

        while current_node.next is not None:
            current_node = current_node.next
            previous_node = previous_node.next
        current_node.prev = None
        previous_node.next = None

    def pop_at_position(self, position):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None

        previous_node = self.head
        current_node = self.head.next

        if position < 0 or position >= self.len():
            raise IndexError(f"Position out of range, list's length is {self.len()}")

        if position == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        for _ in range(1, position):
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = previous_node

    def to_list(self):
        if self.head is None:
            return []

        to_list = []
        current_node = self.head
        while current_node is not None:
            to_list.append(current_node.data)
            current_node = current_node.next
        return to_list
