"""Practice extending built-ins using magic methods and advanced function args.

Options.py was written to get practice extending built-ins, using magic
methods, and advanced function args. It implements each of these things in a
class called Options that extends from a dictionary.

Author: John Shultz
Class: CSI-260-03
Assignment: Week 13 Lab

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


class Options(dict):
    """Represents a set of options."""

    def __init__(self, *args, **kwargs):
        """Initialize an Options argument.

        :param args: Must be strings. Each string is set to True
        :param kwargs: Options paired with their values.
        """
        # Set any passed arg to true.
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError('Only strings are allowed as arguments.')
            else:
                self[arg] = True

        # Set any keyword arg with keyword as key and value as value.
        self.update(kwargs)

        # Make all passed arguments accessible as attributes.
        for key, item in self.items():
            self.__setattr__(key, item)

    def __getitem__(self, key):
        """Define the behavior when a non-existent item is accessed.

        :param key: The key being used to retrieve the item.
        :return: The item indexed by the key, or false if there is no such item
        """
        # Try to get the item indexed by the key. Return False if none exists.
        try:
            return super().__getitem__(key)
        except KeyError:
            return False

    def __getattr__(self, item):
        """Define the behavior when a non-existent attribute is accessed.

        :param item: The name of the parameter that did not exist.
        :return: False.
        """
        return False

    def __setitem__(self, key, value):
        """Define the behavior of self[key] = value item creation format.

        :param key: The key indexing the value. Must be a string
        :param value: The value indexed by the key
        :return: Nothing, just sets value internally.
        """
        # If the key is not a string, raise a type error.
        if not isinstance(key, str):
            raise TypeError(f"Provided key '{key}' is not a string.")

        # Otherwise, set the item.
        else:
            # Set the key value pair as an item
            super().__setitem__(key, value)

            # Set the key value pair as an attribute
            self.__setattr__(key, value)

    def __setattr__(self, name, value):
        """Define the behavior of self.name = value attribute creation format.

        :param name: The name of the attribute
        :param value: The value of the attribute
        :return: Nothing, just sets attribute internally
        """
        # Set the key value pair as an attribute
        self.__dict__[name] = value

        # Set the key value pair as an item.
        super().__setitem__(name, value)

    def __delitem__(self, key):
        """Define the behavior of using the del self[key] format.

        :param key: The key to be deleted along with its value
        :return: Nothing. Just delete the values
        """
        # Delete the item format version of the key
        super().__delitem__(key)

        # Delete the attribute format version of the key
        super().__delattr__(key)

    def __delattr__(self, value):
        """Define the behavior of using the del self.value format.

        :param value: The attribute to be deleted along with it's value.
        :return: Nothing. Just delete the values.
        """
        # Delete the attribute format version of the value
        super().__delattr__(value)

        # Delete the item format version of the value
        super().__delitem__(value)
