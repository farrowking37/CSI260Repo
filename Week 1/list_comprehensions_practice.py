# List comprehension one, list all numbers in the range of 1 - 1000 that are divisible by secen
divisible_by_seven = [n for n in range(1, 1001) if n % 7 == 0]

print(divisible_by_seven)

# List comprehension two, list all numbers that have the digit three in them.
has_three_digits = [x for x in range(1, 1001) if '3' in str(x)]

print(has_three_digits)


# List comprehension 3. Print a given string without any words or vowels
words = 'This list is a lot of wrods and vowels!!'
vowels = 'AEIOU'
without_vowels = [character for character in words if character.upper() not in vowels]

# This statement lets you print the contents of an array where each item is a single character as a string.
print(''.join(without_vowels))


# List comprehension 4. Find all of the words in a string that are less than 4 letters.
sentence = 'This list is a lot of words and vowels'
words = sentence.split()
short_words = [word for word in words if len(word) < 4]

# This statement lets you print the contents of an array where each item is a single word.
print(' '.join(short_words))

# List comprehension 5. Use a dictionary comprehension to map each word in a sentence to it's length
sentence = 'This list is a lot of words and vowels'
words = sentence.split()
word_length = {word: len(word) for word in words}

# Print all the words along with their length
for word in word_length.keys():
    print(word + ": " + str(word_length[word]))

# Additional Challenge: Use a nested list comprehension to find all numbers from 1-1000 divisible by any in from 2-9

""" This is actually a set comprehension. Using a set because they are not allowed to contain duplicate values.
    You can think of sets as groups of dictionary keys. You can't have duplicate keys, or duplicate values in a set.
    Nested List Comprehensions can be a lot faster than the equivalent nested for loops but they sacrifice readability.
    Consider which is more important to your code before using one.
"""
divisible = {n for n in range(1, 1001) for divisor in range(2, 10) if n % divisor == 0}

print(divisible)
