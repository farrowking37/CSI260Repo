"""An example of the usage of static methods. Static methods are methods which do not use any data contained within
a class. They technically run a smidge faster than typical methods as well. These are useful if there is a function
that you would often use in conjunction with your class, that does not technically need class variables.

In addition, you can make classes that are just a bundle of static methods if you want to keep your functions
together under one conveniently named hood."""


class Length:

    @staticmethod
    def inches_to_feet(inches):
        return inches / 12

    @staticmethod
    def inches_to_yard(inches):
        return inches / 36


class Volume:

    @staticmethod
    def cups_to_pints(cups):
        return cups / 2


print(f'{Length.inches_to_feet(40)}')
print(f'{Volume.cups_to_pints(9)}')
