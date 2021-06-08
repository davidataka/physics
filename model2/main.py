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


outer_r = int(input())
dist = int(input())
inner_r = outer_r - dist
x, y = coordinates_data("coordinates.txt")
max_value = max(max(x), max(y))
pylab.xlim(0, max_value)
pylab.ylim(inner_r, outer_r)
pylab.scatter(x, y, 0.5)
pylab.title('coordinates')
pylab.show()
