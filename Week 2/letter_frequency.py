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

# Standard code to open a text file and assign the contents to a string
with open('moby_dick.txt', 'r') as file_handler:
    moby_dick = file_handler.read()

# Create a dictionary named frequency dict.
frequency_dict = dict()

# For each character in the moby_dick string
for character in moby_dick:

    # Check to see if the character is alphanumeric
    if character.isalpha():

        # Check to see if the uppercase version of the character is in the dictionary keys
        if character.upper() not in frequency_dict.keys():

            # If it's not, create the variable with value 1
            frequency_dict[character.upper()] = 1

        else:

            # If it is, simply increment the total count by one
            frequency_dict[character.upper()] += 1

# Use pretty print to print the entire dictionary nicely (automatic alphabetization, clean formatting, etc.)
pprint(frequency_dict)
