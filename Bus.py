

class Bus:
    type = ""
    engine_power = 0
    passenger = 0


def in_bus(elem, line, cars):
    elem.type = 'bus'
    elem.engine_power = line[2]
    elem.passenger = line[1]
    cars.append(elem)


def display_bus(file, i, cars):
    file.write(str(i) + '.Автобус' + "\n")
    file.write('пассажировместимость: ' + str(cars.passenger) + "\n")
