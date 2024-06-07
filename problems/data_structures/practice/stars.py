'''
You are given a string s, which contains stars *.

In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
'''
from ..stack_struct import Stack


class Solution:
    "s = leet**cod*e"
    def remove_stars(self, s: str) -> str:
        stack = Stack()
        for i in s:
            if i != "*":
                stack.push(i)
            else:
                stack.pop()
        return "".join(stack.to_list())