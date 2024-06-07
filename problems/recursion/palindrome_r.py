'''
Write a recursive function called is_palindrome' that takes a string as input
and returns 'True if the string is a palindrome (reads the same forwards and backwards), 
and 'False otherwise.
'''

def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
