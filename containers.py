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


def out(file , container):
    file.write('Контейнер содержит ' + str(len(container)) + ' элементов \n')
    for i in range(len(container)):
        out_cars(container[i], file, i)
        file.write('мощность двигателя: ' + str(container[i].engine_power) + "\n")
    print('всё')


def out_filtr(file, cars):
    file.write('Контейнер содержит ' + str(len(cars)) + ' элементов \n')
    for i in range(len(cars)):
        if cars[i].type == 'truck':
            out_cars(cars[i], file, i)
            file.write('мощность двигателя: ' + str(cars[i].engine_power) + "\n")


def clear(cars):
    cars = []
    return cars
