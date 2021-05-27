

class Bus:
    type = ""
    engine_power = 0
    passenger = 0
    fuel_consumption = 0
    global_weight = 0
    ratio = 0


def in_bus(elem, line, cars):
    elem.type = 'bus'
    elem.engine_power = line[2]
    elem.passenger = line[1]
    elem.fuel_consumption = line[3]
    elem.global_weight = line[1] * 75
    ratio_calc(elem)
    cars.append(elem)


def display_bus(file, i, cars):
    file.write(str(i) + '.Автобус' + "\n")
    file.write('пассажировместимость: ' + str(cars.passenger) + "\n")


def ratio_calc(elem):
    elem.ratio = elem.global_weight / elem.engine_power
