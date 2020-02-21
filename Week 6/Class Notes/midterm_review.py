"""This is a list of concepts that we will be covering in the midterm for this class
List Comprehensions
The Try/Except Syntax
Class varaibles vs. Instance Variables
Variable naming conventions
When to use self and cls
Inheritence concepts
Duck typing instead of inheritance
How to define an Abstract base class, and how to inherit from an abstract base class.
"""


def double_list(list_to_double):

    """ Return a list where each element is doubled in value

    :param list_to_double: (list) numbers to double
    :return: List of numbers
    """

    # An example of using list comprehensions instead of a for loop.
    # For loop would look like this
    # for item in list_to_double:
    #   new_list.append(item * 2)

    new_list = [item * 2 for item in list_to_double]

    return new_list


def conditional_double_list(list_to_double):
    """ Returns a list where each element is doubled in value if it is a nmber

    :param list_to_double: (list) a list that may or may not contain numeric values to double
    :return: A list containing only the numeric values returned
    """

    # An example of using list comprehensions instead of a for loop with a conditional
    # for item in list_to_double:
    #    if type(item) in (int, float):
    #        new_list.append(item * 2)

    new_list = [item * 2 for item in list_to_double if type(item) in (int, float)]

    return new_list

""" Difference between an static, class, and instance method

By default you should assume a method is an instance method. If it uses no instance variables (doesn't reference self) 
but does use class variables, it's a class method. If it uses neither, it's a static method.

You use self in instance methods, cls in class methods
"""


# Test code goes here.
my_nums = [1, 2, 3]
my_polluted_nums = [1, 2, "dog", 3]

print(double_list(my_nums))

print(conditional_double_list(my_polluted_nums))
