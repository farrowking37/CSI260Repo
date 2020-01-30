"""This module contains the country class detailed in the week 3 lab instructions

Author: John Shultz
Class: CSI-260-02
Assignment: Week 3 Lab
Due Date: February 4, 2020 11:59 PM

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


class Country:

	def __init__(self, name, population, area):
		"""Initialize a new country

		:param name: (str) The name of the country.
		:param population: (int) The population of the country
		:param area: (int) the area of the country, given in square kilometers.
		"""
		self.name = name
		self.population = population
		self.area = area

	def is_larger(self, other_country):
		"""Compare the area of the country to another given country.

		:argument other_country: (Country) The country to compare area to.
		:returns: True if the country's area is larger than the other country's area, and false otherwise."""

		if self.area > other_country.area:
			return True
		else:
			return False

	def population_density(self):
		"""Determine and return the population density of the country

		:return: An fstring containing the population density of the country."""

		density = self.population / self.area

		return float(f'{density:.1f}')

	def summary(self):
		"""Create a formatted summary of the countries information

		"return: An fstring formatted summary of the countries information"""

		return f'{self.name} has a population of {self.population} people and is {self.area} square km. ' \
			f'It therefore has a population density of {self.population_density()} people per square km.'
