'''LIFO'''
class Stack:
    '''LIFO'''
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        '''checks if the list is empty'''
        return len(self.stack) == 0

    def push(self, element):
        '''ads an element at the end of the list'''
        self.stack.append(element)
        return self.stack

    def pop(self):
        '''removes an element from the end of the list'''
        if self.is_empty():
            raise IndexError("the list is empty")
        return self.stack.pop()


class Word():
    '''a string'''
    def __init__(self, word: str):
        self.word = word

    def reverse_word(self):
        '''reverses a string'''
        stack = Stack()
        reversed_word = ""
        for char in self.word:
            stack.push(char)
        while not stack.is_empty():
            reversed_word += stack.pop()
        return reversed_word

w = Word("marina")
w.reverse_word()
