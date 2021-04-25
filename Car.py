from Bus import *
from Truck import *


def in_cars(line, cars):
    cd = []
    if line[0] == 0:
        cd = Truck()
        cd = in_truck(cd, line, cars)
    elif line[0] == 1:
        cd = Bus()
        cd = in_bus(cd, line, cars)


def out_cars(cars , file, i):
    if cars.type == 'truck':
        display_truck(file, i, cars)
    elif cars.type == 'bus':
        display_bus(file, i, cars)
