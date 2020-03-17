'''
Car Queue Class
---------------

This class provides a waiting queue-like structure to handle overflow of the
spots in the parking garage
'''

from collections import deque

class CarQueue:
	def __init__(self):
		'''Initializes a waitlist queue with 200 capacity'''
		self.waitlist = deque()
		self.capacity = 200

	def add_car(self, car):
		'''
		Adds a car into the waiting queue

		Parameters:
			car (object): Object representing the car waiting in a queue

		Returns:
			Boolean: If there is room to add into waitlist
		'''

		if self.is_full():
			print("Parking Queue is full, cannot add anymore")

			return False
		else:
			self.waitlist.append(car)
			return True

	def add_car_original_spot(self, car):
		self.waitlist.appendleft(car)

	def remove_car(self):
		'''
		Removes the next car from the waiting queue

		Returns:
			Boolean: If the car was successfully removed
		'''

		if self.is_empty():
			return None
		else:
			next_car = self.waitlist.popleft()
			return next_car

	def is_full(self):
		'''Returns a boolean to signify if waiting list is full'''
		return True if (len(self.waitlist) >= self.capacity) else False

	def is_empty(self):
		'''Returns a boolean to signify if waiting list is empty'''
		return True if (len(self.waitlist) == 0) else False

	def get_waitlist(self):
		return self.waitlist
