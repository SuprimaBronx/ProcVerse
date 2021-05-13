from containers import *


def main():
    input_name = str(input())
    output_name = str(input())
    output_filter_name = str(input())
    file = open(input_name)
    container = Container()
    in_data(file, container.cars)
    file.close()
    file = open(output_name, 'w')
    sort(container.cars)
    file_filter = open(output_filter_name, 'w')
    out_filtr(file_filter, container.cars)
    out(file, container.cars)
    container.cars = clear(container.cars)
    out(file, container.cars)
    out_filtr(file_filter, container.cars)
    file.close()
    file_filter.close()


if __name__ == '__main__':
    main()
