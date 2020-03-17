'''
Car Generator Class
-------------------

This class will generate car objects using a factory pattern.
'''

from . car import Compact, Sedan, Truck
from . car_factory import CarFactory
import random
import numpy as np

class CarGenerator:
	def __init__(self):
		'''Initializes a factory pattern and types of vehicles'''

		self.factory = CarFactory()
		self.types = ['Compact', 'Sedan', 'Truck']
		self.weights = [0.4, 0.4, 0.2]
		random.seed()

	def generate_car(self):
		'''
		Generates a car with a 10% probability. Then, generates a random make
		with the given weighted probabilities
		'''

		if random.random() <= 1:
			car_type = np.random.choice(self.types, p=self.weights)
			car = self.factory.create_car(car_type)

			return car
		else:
			return None
