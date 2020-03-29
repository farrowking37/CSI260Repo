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

    # Save whatever the matching text is to parsed_degrees. Include the scale symbol (F, K, C, etc.)
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
        # Check to see if degrees is an integer or float, if it is directly assign
        if isinstance(degrees, (int, float)):
            self.celsius = degrees

        # Otherwise, if it is a string handle the string
        elif isinstance(degrees, str):

            # Call our function handle_string_temps to parse string
            parsed_degrees = handle_string_temps(degrees)

            # If a block was returned from the string
            if parsed_degrees:

                # Handle the various possible legitimate options
                if parsed_degrees[-1] == 'C':
                    self.celsius = float(parsed_degrees[:-1])
                elif parsed_degrees[-1] == 'F':
                    self.fahrenheit = float(parsed_degrees[:-1])
                elif parsed_degrees[-1] == 'K':
                    self.kelvin = float(parsed_degrees[:-1])
                elif parsed_degrees[-1].isnumeric():
                    self.celsius = float(parsed_degrees)

                # If selected string cannot be parsed raise a value error
                else:
                    raise ValueError(f'Provided string \'{degrees}\' does not contain a number')

        else:
            # If neither of the previous options are useable, raise a temperature error
            raise TemperatureError('Degrees must be an int, float, or properly formatted string')

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, degrees):

        if isinstance(degrees, (int, float)):
            self._celsius = float(degrees)
        elif isinstance(degrees, str):
            parsed_degrees = handle_string_temps(degrees)

            # check to see if final character needs to be ignored before conversion.
            if parsed_degrees[-1] == 'C':
                self._celsius = float(parsed_degrees[:-1])
            else:
                self._celsius = float(parsed_degrees)
        else:
            raise TemperatureError(f"Provided string '{degrees}' contains no numbers")

    @property
    def fahrenheit(self):
        return (self._celsius * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, degrees):

        if isinstance(degrees, (int, float)):
            # Convert Fahrenheit value to Celsius and store.
            self._celsius = (degrees - 32) * (5/9)

        elif isinstance(degrees, str):
            parsed_degrees = handle_string_temps(degrees)

            # Check to see if the final character needs to be ignored before final conversion.
            if parsed_degrees[-1] == "F":
                self._celsius = (float(parsed_degrees[:-1]) - 32) * (5/9)
            else:
                self._celsius = (float(parsed_degrees) - 32) * (5/9)
        else:
            raise TemperatureError(f"Provided string '{degrees}' contains no numbers")

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, degrees):

        if isinstance(degrees, (int, float)):
            self._celsius = degrees - 273.15

        elif isinstance(degrees, str):
            parsed_degrees = handle_string_temps(degrees)

            # Check to see if the final character needs to be removed before conversion.
            if parsed_degrees[-1] == "K":
                self._celsius = float(parsed_degrees[:-1]) - 273.15
            else:
                self._celsius = float(parsed_degrees) - 273.15
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

        # Initialize the sum variable.
        sum_of_temperatures = 0.0
        try:
            # For each temperature in the list, add the value of the _celsius variable to sum_of_temperatures
            for temperature in temperatures:
                sum_of_temperatures += temperature.celsius

            # Calculate the mean.
            average_temp = sum_of_temperatures / len(temperatures)

        # Catch any type error that would occur if a non-temp argument was passed and re-raise as a temperature error.
        except TypeError:
            raise TemperatureError(f"Provided list contains one or more non-temperature objects.")

        # Return a temperature object with average_temp passed as the value for degrees.
        return Temperature(average_temp)
