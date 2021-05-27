

class LightCar:
    type = ""
    engine_power = 0
    max_speed = 0
    fuel_consumption = 0
    global_weight = 0
    ratio = 0


def in_light_car(elem, line, cars):
    elem.type = 'light car'
    elem.engine_power = line[2]
    elem.max_speed = line[1]
    elem.fuel_consumption = line[3]
    elem.global_weight = 4 * 75
    ratio_calc(elem)
    cars.append(elem)


def display_light_car(file, i, cars):
    file.write(str(i) + '.Легковой автомобиль' + "\n")
    file.write('максимальная скорость: ' + str(cars.max_speed) + "\n")


def ratio_calc(elem):
    elem.ratio = elem.global_weight / elem.engine_power
