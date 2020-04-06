"""Tools for working with temperatures.

Author: John Shultz
Class: CSI-260-03
Assignment: Week 11 Lab
Due Date: April 8th, 2020 11:59 AM

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
from functools import total_ordering


@total_ordering
class Temperature:
    """Represents a temperature."""

    def __str__(self):
        """Return a string representation of a temperature.

        :return: A formatted string looking like the following. 20.5°C
        """
        return f'{self.celsius}°C'

    def __repr__(self):
        """Return an appropriate more complete representation of a temperature.

        :return: A string looking like 'Temperature(20.5)'
        """
        return f'Temperature({self.celsius})'

    def __lt__(self, other):
        """Compare the temperature object to another object.

        :param other: Either another temperature, or an int/float.
        :return: True if the value of self.celsius < value of other
        """
        if isinstance(other, Temperature):
            return self.celsius < other.celsius
        else:
            return self.celsius < other

    def __eq__(self, other):
        """Compare the temperature object to another object.

        :param other: Either another temperature, or an int/float
        :return: True if the values are equal
        """
        if isinstance(other, Temperature):
            return self.celsius == other.celsius
        else:
            return self.celsius == other

    def __add__(self, other):
        """Add two objects and return a temperature object with the sum of their value.

        :param other: Another temperature object or an int/float
        :return: a temperature object with the sum of their values
        """
        if isinstance(other, Temperature):
            return Temperature(self.celsius + other.celsius)
        else:
            return Temperature(self.celsius + other)

    def __radd__(self, other):
        """Add two objects together when the Temperature is on the right side.

        :param other: Another temperature object or an int/float
        :return: a temperature object with the sum of their values
        """
        if isinstance(other, Temperature):
            return Temperature(self.celsius + other.celsius)
        else:
            return Temperature(self.celsius + other)

    def __sub__(self, other):
        """Subtracts a Temperature and another object.

        :param other: Another temperature object or an int/float
        :return: a temperature object with the sum of their values
        """
        if isinstance(other, Temperature):
            return Temperature(self.celsius - other.celsius)
        else:
            return Temperature(self.celsius - other)

    def __rsub__(self, other):
        """Also subtraction, but when the temperature object is on the right side.

        :param other: Another temperatuer object or an int/float
        :return: A temperature object with the sum of their values
        """
        if isinstance(other, Temperature):
            return Temperature(other.celsius - self.celsius)
        else:
            return Temperature(other - self.celsius)

    def __iadd__(self, other):
        """Adding but for the += operator. Using code found on stackoverflow here.

        https://stackoverflow.com/questions/1047021/overriding-in-python-iadd-method

        :param other: Another temperature object, or another number
        :return: self.
        """
        if isinstance(other, Temperature):
            self.celsius += other.celsius
        else:
            self.celsius += other
        return self

    def __isub__(self, other):
        """Subtraction but for the -= Operator using code found on stack overflow here.

        https://stackoverflow.com/questions/1047021/overriding-in-python-iadd-method

        :param other: Another temperature object or another number
        :return: self
        """
        if isinstance(other, Temperature):
            self.celsius -= other.celsius
        else:
            self.celsius -= other
        return self

    def __hash__(self):
        """Get the hash of a temperature.

        :return: The hashed result of self.__str__()
        """
        return hash(str(self))

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
        """
        self.celsius = degrees
