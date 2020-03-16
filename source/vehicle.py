'''
Vehicle Class
-------------

The Vehicle class will contain 2 attributes: state and license plate
'''

class Vehicle:
	def __init__(self, license):
		'''Initializes Vehicle class with size and license plate'''
		self.license = license

	def get_license(self):
		'''Return the vehicle's license plate'''
		return self.license
