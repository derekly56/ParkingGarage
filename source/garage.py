'''
Garage Class
-------------
Will be able to hold cars of different models/make. Uniquely identify
them by their license plate

The garage class will dedicate the following amount of spacing per vehicle sizes
Compact: 40%, Sedan: 30%, Truck: 20%
'''

import math
from collections import deque
from . car_spot import Spot
import time
from . car import Truck, Sedan, Compact

COMPACT_RATIO = 0.4
SEDAN_RATIO = 0.3
TRUCK_RATIO = 0.2

class Garage:
	def __init__(self, levels, capacity):
		'''Initializes the parking garage and spots allocated for each sizes of vehicles'''

		self.garage = self._init_garage(levels, capacity)
		self.compact, self.sedan, self.truck = self._init_spots(levels, capacity)
		self.available_spots = capacity * levels

	def _init_garage(self, levels, capacity):
		'''
		Creates a 3d matrix that represents a garage

		Parameters:
			levels (int): The amount of levels in the parking garage
			capacity (int): The amount of parking spots per level

		Returns:
			garage (list<list<list>>): 3D matrix representing the parking
									   garage
		'''

		garage = []

		x = int(math.sqrt(capacity))
		level = [[None] * x for _ in range(x)]

		for each_level in range(levels):
			garage.append(level)

		return garage

	def _init_spots(self, levels, capacity):
		'''
		Allocates space for each vehicle sizes in a queue of available coordinates

		Parameters:
			garage (list<list<list>>): 3D Matrix Representation of Garage
			levels (int): The amount of levels in the parking garage
			capacity (int): The amount of parking spots per level

		Returns:
			compact (queue): Available spots for compact vehicles
			sedan (queue): Available spots for sedan vehicles
			truck (queue): Available spots for truck vehicles
		'''

		compact, sedan, truck = deque(), deque(), deque()
		total_capacity = capacity * levels

		compact_space = total_capacity * COMPACT_RATIO
		sedan_space = total_capacity * SEDAN_RATIO
		truck_space = total_capacity * TRUCK_RATIO

		for level in range(len(self.garage)):
			for i in range(len(self.garage[0])):
				for j in range(len(self.garage[0][0])):
					if compact_space > 0:
						compact_space -= 1
						compact.append((level, i, j))
					elif sedan_space > 0:
						sedan_space -= 1
						sedan.append((level, i, j))
					else:
						truck.append((level, i, j))

		return compact, sedan, truck

	def assign_spot(self, car_type, car_queue, time_limit):
		'''
		Assigns a spot to a vehicle according to the car_queue (1,2,3) with a
		given time limit

		Parameters:
			car_type (object): Object class representing a car type
			car_queue (int): Signifying 1 (compact), 2 (sedan), 3(truck)
			time_limit (int): Time limit in seconds

		'''

		curr_time = int(round(time.time()))
		self.available_spots -= 1

		if car_queue == 1:
			parking_loc = self.compact.popleft()
			level, row, col = parking_loc

			parking_spot = Spot(car_type, time_limit, curr_time, parking_loc)
			self.garage[level][row][col] = parking_spot
		elif car_queue == 2:
			parking_loc = self.sedan.popleft()
			level, row, col = parking_loc

			parking_spot = Spot(car_type, time_limit, curr_time, parking_loc)
			self.garage[level][row][col] = parking_spot
		else:
			parking_loc = self.truck.popleft()
			level, row, col = parking_loc

			parking_spot = Spot(car_type, time_limit, curr_time, parking_loc)
			self.garage[level][row][col] = parking_spot

	def remove_spot(self, spot):
		'''
		Removes the car type at the spot that the time limit is currently up

		Parameters:
		 	spot (object): Spot object containing car type and location
		'''

		level, row, col = spot.get_parking_loc()
		car_type = spot.get_car()
		car_size = car_type.get_size()
		self.available_spots += 1

		if car_size == 1:
			self.compact.append((level, row, col))
		elif car_size == 2:
			self.sedan.append((level, row, col))
		else:
			self.truck.append((level, row, col))

		self.garage[level][row][col] = None

	def clean_up(self):
		'''Clears all cars with expired time from parking spots'''
		levels, row, col = len(self.garage), len(self.garage[0]), len(self.garage[0][0])

		for level in range(levels):
			for r in range(row):
				for c in range(col):
					curr_spot = self.garage[level][r][c]

					if curr_spot:
						if curr_spot.get_time_remaining() <= 0:
							self.remove_spot(curr_spot)

	def check_space(self, car_type):
		'''
		Checks for available space according to car size. Compact cars can fit
		in both compact and sedan. Sedan can fit in both sedan and truck. Trucks
		can only fit in truck

		Parameters:
			vehicle_size (int): Sizes denoting vehicle type

		Return:
			boolean: True or False for available spots according to car size
		'''

		if self.available_spots < 1:
			return False, 0
		else:
			if isinstance(car_type, Compact):
				if len(self.compact) >= 1:
					return True, 1
				elif len(self.sedan) >= 1:
					return True, 2
				else:
					return False, 0
			elif isinstance(car_type, Sedan):
				if len(self.sedan) >= 1:
					return True, 2
				elif len(self.truck) >= 1:
					return True, 3
				else:
					return False, 0
			elif isinstance(car_type, Truck):
				if len(self.truck) >= 1:
					return True, 3
				else:
					return False, 0
			else:
				return False, 0
