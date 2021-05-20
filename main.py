from containers import *


def main():
    x = 0
    input_name = str(input())
    output_name = str(input())
    output_filter_name = str(input())
    try:
        file = open(input_name)
    except:
        x = 4
    if x!=4:
        container = Container()
        x = check(file)
        if x == 'x':
            in_data(file, container.cars)
            file.close()
            file = open(output_name, 'w')
            sort(container.cars)
            file_filter = open(output_filter_name, 'w')
            out_filtr(file_filter, container.cars, x)
            out(file, container.cars, x)
            container.cars = clear(container.cars)
            out(file, container.cars,x)
            out_filtr(file_filter, container.cars,x)
            file.close()
            file_filter.close()
        else:
            file.close()
            file = open(output_name, 'w')
            file_filter = open(output_filter_name, 'w')
            out_filtr(file_filter, container.cars, x)
            out(file, container.cars, x)
    else:
        file = open(output_name, 'w')
        file_filter = open(output_filter_name, 'w')
        out_filtr(file_filter, 0, x)
        out(file, 0, x)


if __name__ == '__main__':
    main()
