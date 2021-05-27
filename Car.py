from Bus import *
from Truck import *
from LightСar import *


def in_cars(line, cars):
    cd = []
    if line[0] == 0:
        cd = Truck()
        cd = in_truck(cd, line, cars)
    elif line[0] == 1:
        cd = Bus()
        cd = in_bus(cd, line, cars)
    elif line[0] == 2:
        cd = LightCar()
        cd = in_light_car(cd, line, cars)


def out_cars(cars, file, i):
    if cars.type == 'truck':
        display_truck(file, i, cars)
    elif cars.type == 'bus':
        display_bus(file, i, cars)
    elif cars.type == 'light car':
        display_light_car(file, i, cars)
