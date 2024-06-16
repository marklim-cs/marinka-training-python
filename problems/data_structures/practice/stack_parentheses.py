'''
{}, [], (),
[(({}){})] - valid 
{{{{}}}} - valid
{(}) - not valid
{]} - not valid 
[ - not valid
'''
from ..stack_struct import Stack

def is_valid_parentheses(string: str) -> bool:
    stack = Stack()
    def try_pop(parenthesis: str):
        if len(stack) == 0:
            return False
        elif stack.top() == parenthesis:
            stack.pop()
            return True
        else:
            return False
    for i in string:
        if i == "{":
            stack.push(i)
        elif i == "}":
            if not try_pop("{"):
                return False
        elif i == "[":
            stack.push(i)
        elif i == "]":
            if not try_pop("["):
                return False
        elif i == "(":
            stack.push(i)
        elif i == ")":
            if not try_pop("("):
                return False
    return len(stack) == 0
