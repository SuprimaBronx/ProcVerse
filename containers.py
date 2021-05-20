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


def out(file , container,x):
    if x == 0:
        file.write('в вводимых данных содержится ошибка, неизвестный символ')
    elif x == 1:
        file.write('в вводимых данных содержится ошибка, выбран несуществующий класс автомобилей')
    elif x == 2:
        file.write('в вводимых данных содержится ошибка, параметры автомобилей не могут быть отирцательными')
    elif x == 4:
        file.write('неверно введённое имя входного файла')
    else:
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


def out_filtr(file, cars,x):
    if x == 0:
        file.write('в вводимых данных содержится ошибка, неизвестный символ')
    elif x == 1:
        file.write('в вводимых данных содержится ошибка, выбран несуществующий класс автомобилей')
    elif x == 2:
        file.write('в вводимых данных содержится ошибка, параметры автомобилей не могут быть отирцательными')
    elif x == 4:
        file.write('неверно введённое имя входного файла')
    else:
        file.write('Контейнер содержит ' + str(len(cars)) + ' элементов \n')
        for i in range(len(cars)):
            if cars[i].type == 'truck':
                out_cars(cars[i], file, i)
                file.write('мощность двигателя: ' + str(cars[i].engine_power) + "\n")
                file.write('расход топлива: ' + str(cars[i].fuel_consumption) + "\n")
                file.write('Отношение веса груза к мощности двигателя: ' + str(cars[i].ratio) + "\n")


def check(file):
    for line in file:
        temp = (line + '.')[:-1]
        for i in range(len(temp)):
            if temp[i] not in '|\n0123456789':
                return 0
        temp = temp.rstrip('\n')
        temp = temp.split('|')
        if temp[0] not in '012':
            return 1
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        if temp[1] <= 0 or temp[2] <= 0 or temp[3] <= 0:
            return 2
    return 'x'


def clear(cars):
    cars = []
    return cars
