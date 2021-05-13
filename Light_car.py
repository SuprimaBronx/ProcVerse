

class Light_car:
    type = ""
    engine_power = 0
    max_speed = 0

def in_light_car(elem, line, cars):
    elem.type = 'light car'
    elem.engine_power = line[2]
    elem.max_speed = line[1]
    elem.fuel_consumption = line[3]
    cars.append(elem)

def display_light_car(file, i, cars):
    file.write(str(i) + '.Легковой автомобиль' + "\n")
    file.write('максимальная скорость: ' + str(cars.max_speed) + "\n")
