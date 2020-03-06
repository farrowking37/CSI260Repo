"""Tests for Week 8 Lab.

Prof. Joshua Auerbach
Champlain College
CSI-260 -- Spring 2019
"""

import unittest
from temperature import Temperature, TemperatureError
import sys


# define constants used by tests

STUDENT_CODE = ["temperature.py"]

VALID_TEMPERATURES = [-45, 55.2, "-14.75", "34C", "3.4C", "-10.2C",
                      "-11.2F", "23.5F", "74.5F", "245.3K"]
INVALID_TEMPERATURES = ["garbage", "34 degrees celsius", [], "45P", "34CC",
                        {"C": 23}]

DEGREES_celsius = [-45.0, 55.2, -14.75, 34.0, 3.4, -10.2, -24.0,
                   -4.722222222222222, 23.61111111111111, -27.849999999999966]
DEGREES_FAHRENHEIT = [-49.0, 131.36, 5.449999999999999, 93.2, 38.12, 13.64,
                      -11.200000000000003, 23.5, 74.5, -18.12999999999994]
KELVINS = [228.14999999999998, 328.34999999999997, 258.4, 307.15,
           276.54999999999995, 262.95, 249.14999999999998, 268.42777777777775,
           296.76111111111106, 245.3]

AVERAGE_TEMPERATURE = sum(DEGREES_celsius) / len(DEGREES_celsius)


def equal_to_n_decimal_places(value1, value2, n):
    """Return if value1 is equal to value2 when rounded to n decimal places."""
    return f"{value1:.{n}f}" == f"{value2:.{n}f}"


class TestWeek8(unittest.TestCase):
    """Main testing class for Week 8 Lab."""

    def test_1_raises(self):
        """Test if the initializer raises errors as specified."""
        for temp_value in INVALID_TEMPERATURES:
            try:
                Temperature(temp_value)
                self.fail("Attempting to initialize a temperature"
                          f" with invalid value {temp_value} must"
                          " raise TemperatureError.")

            except Exception as e:
                self.assertIsInstance(e, TemperatureError,
                                      "Attempting to initialize a temperature "
                                      f"with invalid value {temp_value} must "
                                      f"raise TemperatureError not {type(e)}.")

    def test_2_inits(self):
        """Test if the initializer properly sets celsius."""
        for temp_value, celsius in zip(VALID_TEMPERATURES, DEGREES_celsius):
            temperature = Temperature(temp_value)
            try:
                self.assertTrue(equal_to_n_decimal_places(temperature.celsius,
                                                          celsius, 4),
                                f"Temperature temperature initialized with "
                                f"{temp_value} should have temperature.celsius"
                                f" = {celsius}, but it is "
                                f"{temperature.celsius}")
            except AttributeError:
                self.fail(f"Temperature instance has no attribute "
                          "celsius.")

    def test_3_fahrenheit(self):
        """Test if fahrenheit property exists and is computed properly."""
        for temp_value, fahrenheit in zip(VALID_TEMPERATURES,
                                          DEGREES_FAHRENHEIT):
            temperature = Temperature(temp_value)
            try:
                self.assertTrue(equal_to_n_decimal_places(
                                                     temperature.fahrenheit,
                                                     fahrenheit, 4),
                                f"Temperature temperature initialized with "
                                f"{temp_value} should have "
                                f"temperature.fahrenheit = {fahrenheit}, "
                                f"but it is {temperature.fahrenheit}")
            except AttributeError:
                self.fail(f"Temperature instance has no property "
                          "fahrenheit.")

    def test_4_kelvin(self):
        """Test if kelvin property exists and is computed properly."""
        for temp_value, kelvin in zip(VALID_TEMPERATURES, KELVINS):
            temperature = Temperature(temp_value)
            try:
                self.assertTrue(equal_to_n_decimal_places(temperature.kelvin,
                                                          kelvin, 4),
                                f"Temperature temperature initialized with "
                                f"{temp_value} should have temperature.kelvin "
                                f"= {kelvin}, but it is "
                                f"{temperature.kelvin}")
            except AttributeError:
                self.fail(f"Temperature instance has no property "
                          "kelvin.")

    def test_5_conversions(self):
        """Test if setting various attributes works appropriately."""
        for celsius, fahrenheit, kelvin in zip(DEGREES_celsius,
                                               DEGREES_FAHRENHEIT,
                                               KELVINS):
            temperature = Temperature()
            temperature.celsius = celsius
            self.assertTrue(equal_to_n_decimal_places(temperature.fahrenheit,
                                                      fahrenheit, 4))
            self.assertTrue(equal_to_n_decimal_places(temperature.kelvin,
                                                      kelvin, 4))

            temperature.fahrenheit = fahrenheit
            self.assertTrue(equal_to_n_decimal_places(temperature.celsius,
                                                      celsius, 4))
            self.assertTrue(equal_to_n_decimal_places(temperature.kelvin,
                                                      kelvin, 4))

            temperature.kelvin = kelvin
            self.assertTrue(equal_to_n_decimal_places(temperature.celsius,
                                                      celsius, 4))
            self.assertTrue(equal_to_n_decimal_places(temperature.fahrenheit,
                                                      fahrenheit, 4))

    def test_6_average(self):
        """Test if averaging works as specified."""
        average_temperature = Temperature.average([Temperature(temp)
                                                   for temp in
                                                   VALID_TEMPERATURES]).celsius
        self.assertTrue(equal_to_n_decimal_places(AVERAGE_TEMPERATURE,
                                                  average_temperature, 4),
                        f"Average temperature should be {AVERAGE_TEMPERATURE} "
                        f"degrees celsius, but is {average_temperature} "
                        "degrees celsius")

    def test_7_style(self):
        """Run the linter and check that the header is there."""
        try:
            from flake8.api import legacy as flake8
            # noqa on the following since just importing to test installed
            import pep8ext_naming  # noqa
            import flake8_docstrings  # noqa
            print("\nLinting Code...\n" + "=" * 15)

            style_guide = flake8.get_style_guide()

            report = style_guide.check_files(STUDENT_CODE)

            self.assertEqual(report.total_errors, 0,
                             "You should fix all linting errors "
                             "before submission in order to receive full "
                             "credit!")

            for module in STUDENT_CODE:
                self.check_header(module)

            print("Passing linter tests!")

        except ImportError:
            print("""
### WARNING: Unable to import flake8 and/or extensions, so cannot \
properly lint your code. ###

Please install flake8, pep8-naming, and flake8-docstrings to auto-check \
whether you are adhering to proper style and docstring conventions.

To install, run:

pip install flake8 pep8-naming flake8-docstrings

""")

    def check_header(self, module):
        """Check the header of the given module."""
        docstring = sys.modules[module[:-3]].__doc__
        for check in ['Author:', 'Class:', 'Assignment:',
                      'Certification of Authenticity:']:
            self.assertIn(check, docstring,
                          "Missing '{}' in {}'s docstring".format(
                            check, module))


if __name__ == '__main__':
    unittest.main(failfast=True)
