import pylab


def coordinates_data(file):
    data = open(file, 'r')
    data_x = []
    data_y = []
    for i in data.read().split('\n'):
        if i == '':
            break
        cur_x, cur_y = [float(j) for j in i.split(' ')]
        data_x.append(cur_x)
        data_y.append(cur_y)
    return data_x, data_y


r_outer = int(input())
distance_plates = int(input())
r_interior = r_outer - distance_plates
x, y = coordinates_data("coordinates.txt")
pylab.xlim(0, max(max(x), max(y)))
pylab.ylim(r_interior, r_outer)
pylab.plot(x, y)
pylab.title("coordinates")
pylab.show()

x, y = coordinates_data("acceleration_time.txt")
pylab.xlim(0, max(max(x), max(y)))
pylab.ylim(0, max(max(x), max(y)))
pylab.plot(x, y)
pylab.title("acceleration_time")
pylab.show()

x, y = coordinates_data("speed_time.txt")
pylab.xlim(0, max(max(x), max(y)))
pylab.ylim(0, max(max(x), max(y)))
pylab.plot(x, y)
pylab.title("speed_time")
pylab.show()
