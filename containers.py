from Car import *


class Container:
    cars = []


def in_data(file_input, cars):
    for line in file_input:
        line = line.rstrip('\n')
        temp = line.split('|')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        in_cars(temp, cars)


def out(file, container):
    file.write('Контейнер содержит ' + str(len(container)) + ' элементов \n')
    for i in range(len(container)):
        out_cars(container[i], file, i)
        file.write('мощность двигателя: ' + str(container[i].engine_power) + "\n")
    print('всё')


def multimethods(cars, out_name):
    objects = {
        Truck: 'Truck',
        Bus: 'Bus'
    }
    for i in range(0, len(cars), 2):
        res = ''
        res += objects[type(cars[i])] + ' and ' + objects[type(cars[i + 1])]
        out_name.write(res + '\n')


def clear(cars):
    cars = []
    return cars
