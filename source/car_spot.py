'''
Spot Class
-----------

This spot class will contain two attributes: a car class and a time limit
'''

class Spot:
	def __init__(self, car_type, time_limit, start_time, parking_loc):
		'''Initializes parking spot with car object and time'''
		self.car = car_type
		self.time = time_limit
		self.start = start_time
		self.end = self.start + self.time
		self.parking_loc = parking_loc

	def get_time_remaining(self):
		'''Returns remaining time left in the parking spot'''
		return self.end - self.start

	def get_car(self):
		'''Returns car object in the Spot'''
		return self.car

	def get_parking_loc(self):
		'''Returns location of the spot'''
		return self.parking_loc
