"""Classes for working with Temperatures."""
import re


class TemperatureError(Exception):
    """Error raised for invalid temperatures."""

    pass


def handle_string_temps(degrees):
    # Create a list named parsed input containing all substrings matching this regex pattern
    #
    # -? Optional block, matches a possible negative number
    # [0-9/.]+ Matches any string that contains at least one number or decimal point
    # [FKC]? Optional block, matches any of the three possible temperature characters
    parsed_degrees = re.match("-?[0-9/.]+[FKC]?", degrees)

    # Save whatever the matching text is to parsed_degrees
    try:
        parsed_degrees = parsed_degrees.group()
        return parsed_degrees
    except AttributeError:
        raise TemperatureError(f"Provided string '{degrees}' has no number.")


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees celsius,
    or Kelvins.
    """

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees.

        Args:
            degrees, which can be one of the following:
                (1) a number, or a string containing a number
                    in which case it is interpreted as degrees celsius
                (2) a string containing a number followed by one of the
                    following symbols:
                       C, in which case it is interpreted as degrees celsius
                       F, in which case it is interpreted as degrees Fahrenheit
                       K, in which case it is interpreted as Kelvins

        Raises:
            TemperatureError: if degrees is not one of the specified
                                     forms

        """

        if isinstance(degrees, (int, float)):
            self.celsius = degrees

        elif isinstance(degrees, str):

            parsed_degrees = handle_string_temps(degrees)

            if parsed_degrees:

                if parsed_degrees[-1] == 'C':
                    float(parsed_degrees[:-1])
                elif parsed_degrees[-1] == 'F':
                    pass
                elif parsed_degrees[-1] == 'K':
                    pass
                elif parsed_degrees[-1].isnumeric():
                    self.celsius = float(parsed_degrees)

                else:
                    raise ValueError(f'Provided string \'{degrees}\' does not contain a number')

        else:
            raise TemperatureError('Degrees must be an int, float, or properly formatted string')

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, degrees):

        if isinstance(degrees, (int, float)):
            self._celsius = float(degrees)
        elif isinstance(degrees, str):
            parsed_degress = handle_string_temps(degrees)

            if parsed_degress[-1] == 'C':
                self._celsius = float(parsed_degress[:-1])
            else:
                self._celsius = float(parsed_degress)
        else:
            raise TemperatureError(f"Provided string '{degrees}' contains no numbers")



    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        pass


"""test1 = Temperature(1)
print(test1.celsius)
test2 = Temperature("1")
print(test2.celsius)
test3 = Temperature("33C")
print(test3.celsius)
test4 = Temperature("33.54")
print(test4.celsius)
test5 = Temperature("10005097.1C")
print(test5.celsius)
test6 = Temperature("Thisdon'tgotnumbersin")
print(test6.celsius)"""
