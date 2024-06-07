'''
given a string containing only characters '(' and ')', check if its a valid sequence of parentheses.
Examples:
()()() - valid
((((((())))))) - valid
(()(()())) - valid
)( - invalid
())( - invalid
( - invalid
) - invalid
'''

def is_valid_parentheses(string: str) -> bool:
    counter = 0
    for i in string:
        if counter < 0:
            return False
        if i == "(":
            counter += 1
        if i == ")":
            counter -= 1
    return counter == 0

def is_valid_parentheses_stack(string: str) -> bool:
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
