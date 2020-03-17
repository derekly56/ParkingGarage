'''
Car Factory
-----------
This car factory will utilize a factory pattern to generate similar objects
'''

from . car import Compact, Sedan, Truck
import random

letters = [
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
	'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [
	0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]

class CarFactory:
	def __init__(self):
		'''Initializes the letters and numbers used for license plate'''
		self.letters = letters
		self.numbers = numbers

	def create_car(self, make):
		'''
		Creates a car base on the make using a factory pattern

		Parameters:
			make (string): Type of car make to create pattern

		Returns:
			car (object): Car type depending on make
		'''
		random.seed()
		license = self.generate_license()

		if make == 'Compact':
			return self.create_compact(license)

		if make == 'Sedan':
			return self.create_sedan(license)

		if make == 'Truck':
			return self.create_truck(license)

		return None

	def create_compact(self, license):
		'''Creates a Compact Vehicle'''
		return Compact(license)

	def create_sedan(self, license):
		'''Creates a Sedan Vehicle'''
		return Sedan(license)

	def create_truck(self, license):
		'''Creates a Truck Vehicle'''
		return Truck(license)

	def generate_license(self):
		'''Generates a random license plate'''
		license = ""

		for i in range(3):
			license += random.choice(self.letters)

		for i in range(3):
			license += str(random.choice(self.numbers))

		return license
