from source.garage import Garage
from source.car_generator import CarGenerator
from source.car_queue import CarQueue
import random
import threading
import time

TIME_SLEEP = 0.1

def display(iterations, parking_queue, levels, capacity, garage):
	print()
	print("End of Iteration #", str(iterations))
	print("-----------------")
	print("Cars in queue: " + str(len(parking_queue.get_waitlist())))
	print("Cars in Garage: " + str(levels * capacity - garage.available_spots))

def main():
	random.seed()
	end = False
	levels = 5
	capacity = 100

	garage = Garage(levels, capacity)
	car_generator = CarGenerator()
	parking_queue = CarQueue()
	iterations = 0

	while not end:
		iterations += 1

		# Cleans up garage and then generates a new vehicle
		garage.clean_up()
		car = car_generator.generate_car()

		# Generate a car and add to end of queue
		if car:
			status = parking_queue.add_car(car)

			if not status:
				break

		# Grab first car from the parking queue
		# If there's no available cars, then do nothing
		# Else, find an available spot in the garage and
		# set a timer_limit of 1-3 seconds
		first_car = parking_queue.remove_car()

		if first_car:
			available, section = garage.check_space(car)

			if available:
				time_limit = random.randint(1,3)

				garage.assign_spot(car, section, time_limit)
			else:
				parking_queue.add_car_original_spot(first_car)

		time.sleep(TIME_SLEEP)

	display(iterations, parking_queue, levels, capacity, garage)

if __name__ == "__main__":
	main()
