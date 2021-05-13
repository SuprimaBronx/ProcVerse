

class Truck:
    type = ""
    engine_power = 0
    weight = 0
    fuel_consumption = 0
    global_weight = 0
    ratio = 0


def in_truck(elem, line, cars):
    elem.type = 'truck'
    elem.engine_power = line[2]
    elem.weight = line[1]
    elem.fuel_consumption = line[3]
    elem.global_weight = line[1]
    ratio_calc(elem)
    cars.append(elem)


def display_truck(file, i, cars):
    file.write(str(i) + '.Грузовик' + "\n")
    file.write('Грузоподъёмность: ' + str(cars.weight) + "\n")


def ratio_calc(elem):
    elem.ratio = elem.global_weight / elem.engine_power

