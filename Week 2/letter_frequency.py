"""
We are going to analyze moby_dick and determine the frequency
of each letter in the book.

Your program should be able to load the included txt file,
and then build a letter frequency dictionary.

You should ignore the case of the letter. I.E. The upper and lower case version of 'a' count as the same character.

You should print the letter frequency dictionary to the screen.

You should also create a seperate dictionary with the percentages of each character in it.

"""

# Import the pprint function from the pretty print module to make our lives easier later.
from pprint import pprint

# Import string so we can us string.ascii_uppercase
import string

# Standard code to open a text file and assign the contents to a string
with open('moby_dick.txt', 'r') as file_handler:
    moby_dick = file_handler.read()

# Create a dictionary named frequency dict using dictionary comprehensions
frequency_dict = {character: moby_dick.upper().count(character) for character in string.ascii_uppercase}

# Use pretty print to print the entire dictionary nicely (automatic alphabetization, clean formatting, etc.)
pprint(frequency_dict)

# Sum up all the values stored in the frequency dictionary
total_characters = sum(frequency_dict.values())

# Create percentage dictionary using dictionary comprehension
percentage_dict = {key: value / total_characters for key, value in frequency_dict.items()}

pprint(percentage_dict)
