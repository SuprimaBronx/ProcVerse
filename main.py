from containers import *


def main():
    input_name = str(input())
    output_name = str(input())
    file = open(input_name)
    container = Container()
    in_data(file, container.cars)
    file.close()
    file = open(output_name, 'w')
    out(file, container.cars)
    container.cars = clear(container.cars)
    out(file, container.cars)
    file.close()


if __name__ == '__main__':
    main()
