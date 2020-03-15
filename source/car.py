'''
Car Class
----------
Will create cars and identify cars by their license plate

Attr: Size (compact, sedan, truck), model/make, license plate, state
'''

class Car:
	def __init__(self, model, make, size, license, state):
		self.model = model
		self.make = make
		self.size = size
		self.license = license
		self.state = state

	def get_model(self):
		'''Returns the model of the car'''
		return self.model

	def get_make(self):
		'''Returns the make of the car'''
		return self.make

	def get_size(self):
		'''Returns the size of the car'''
		return self.size

	def get_license(self):
		'''Returns the license of the car'''
		return self.license

	def get_state(self):
		'''Returns the state of the car'''
		return self.state
