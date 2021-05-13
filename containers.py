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
        file.write('расход топлива: ' + str(container[i].fuel_consumption) + "\n")
        file.write('Отношение веса груза к мощности двигателя: ' + str(container[i].ratio) + "\n")
    print('всё')


def sort(cars):
    for i in range(len(cars) - 1):
        for j in range(len(cars) - 1):
            if cars[j].ratio > cars[j + 1].ratio:
                cars[j], cars[j + 1] = cars[j + 1], cars[j]


def out_filtr(file, cars):
    file.write('Контейнер содержит ' + str(len(cars)) + ' элементов \n')
    for i in range(len(cars)):
        if cars[i].type == 'truck':
            out_cars(cars[i], file, i)
            file.write('мощность двигателя: ' + str(cars[i].engine_power) + "\n")
            file.write('расход топлива: ' + str(cars[i].fuel_consumption) + "\n")
            file.write('Отношение веса груза к мощности двигателя: ' + str(cars[i].ratio) + "\n")



def clear(cars):
    cars = []
    return cars
