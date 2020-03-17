# Parking Garage

A fun small project that I created to work on using Multithreading. I'm currently in the process
of adding it to the code. This project creates a parking garage that has multi-levels and utilizes
a nice capacity that can be rooted (i.e 100, 256, etc). The garage will find parking spots for
the cars that are waiting in the queue. There is a car generator that's randomly creating three
models of different cars (Compact, Sedan, Truck).

Once the cars are created, they'll be inputted into the garage (if there's room) or it'll be relocated
to the parking queue. Once the parking queue is filled up (currently set to 200), then the program will
shut down!  

## How to use  

Below is a quick guide to how to use and watch the cars get filled up!

### Requirements  

* Python 3
* Docker

### Instructions  

* Pull down the github repo onto your local computer.
* Cd into the directory
* Run `docker build -t python-garage .`
* Run `docker run python-garage`
