'''
The sort() function modifies the list it is called on, 
meaning it sorts the list in-place and doesn't return anything. 
On the other hand, the sorted() function creates a new list 
containing a sorted version of the list it is given. 
The sorted() function can accept any iterable, while sort() is a method specific to lists.
'''

# sort()
list_of_tuples = [('a', 2), ('b', 1), ('c', 3)]
list_of_tuples.sort(key = lambda element: element[1])
print(list_of_tuples)

# sorted()
# sort the list in descending order based on the length of the strings.
list_of_str = ['apple', 'banana', 'no', 'cherry', 'date', 'yes', 'misunderstanding']
new_list = list(sorted(list_of_str, key = len, reverse=True))
print(new_list)

# sorted()
# sort this list of dictionaries by the average grade of each student.
students = [
    {"name": "Alice", "math": 85, "english": 92, "science": 78}, #255
    {"name": "Bob", "math": 90, "english": 88, "science": 82}, #260
    {"name": "Charlie", "math": 80, "english": 85, "science": 86} #251
]

list_of_dicts = list(sorted(students, key = lambda diction:
    (diction["math"] + diction["english"] + diction["science"]) / 3, reverse=True))
print(list_of_dicts)

# sorted()
# sort this list of sentences by the number of vowels in each sentence
sentences = [
    "I love CS50",
    "The quick brown fox jumps over the lazy dog",
    "Hello, world!",
    "Python is fun",
    "Keep calm and code on"
]
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_sentences = list(sorted(sentences,
                              key = lambda sentence:
                              len([char for char in sentence if char.lower()
                                   in vowels]))) # in 'aeiou'
print(([char for char in 'marina' if char.lower() in 'aeiou']))
print(vowel_sentences)

# sort
# sort the list in alphabetical order. However, the sorting should ignore the case of the strings.
list_alphabet = ['Cherry', 'cat', 'Banana', 'boo', 'date', 'apple', 'ao']
list_alphabet.sort(key = lambda word: word.lower()[:2])
print(list_alphabet)


# filter()
list_of_strings = ['apple', 'banana', 'cherry', 'date']
new_list = list(filter(lambda str: len(str) == 5, list_of_strings))
print(new_list)

# any()
# filter out all numbers in this list that are divisible by any number in another list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisors = [2, 3, 5]
new_list = list(filter(lambda number: any(number % divisor == 0 for divisor in divisors), numbers))
print(new_list)

# map()
list_of_ints = [2, 4, 6, 8, 10]
new_list = list(map(lambda x: x**2, list_of_ints))
print(new_list)
