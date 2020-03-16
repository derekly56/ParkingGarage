'''
Car Class
----------
Will create cars and inherit from parent Vehicle class.

Attr: make, license, state
'''

from vehicle import Vehicle

class Truck(Vehicle):
	def __init__(self, license):
		'''Initializes Car class'''
		super().__init__(license)
		self.make = 'TRUCK'

	def get_make(self):
		'''Returns the make of the car'''
		return self.make

class Sedan(Vehicle):
	def __init__(self, license):
		'''Initializes Car class'''
		super().__init__(license)
		self.make = 'SEDAN'

	def get_make(self):
		'''Returns the make of the car'''
		return self.make

class Compact(Vehicle):
	def __init__(self, license):
		'''Initializes Car class'''
		super().__init__(license)
		self.make = 'COMPACT'

	def get_make(self):
		'''Returns the make of the car'''
		return self.make
