from math import sqrt


def length_of_line_my1(array):
    a, b = array
    tmp = sum(abs(a[i] - b[i]) ** 2 for i in range(len(array)))
    tmp = '{:1.2f}'.format(sqrt(tmp))
    return tmp


def length_of_line_my2(array):
    a, b = array
    tmp = sum(abs(a[i] - b[i]) ** 2 for i in range(len(array)))
    result = '{:1.2f}'.format(sqrt(tmp))
    return result


def length_of_line_my3(array):
    a, b = array
    tmp = sum((a[i] - b[i]) ** 2 for i in range(len(array)))
    result = '{:.2f}'.format(sqrt(tmp))
    return result


def length_of_line_best(array):
    x1, y1, x2, y2 = array[0][0], array[0][1], array[1][0], array[1][1]
    return '{:.2f}'.format((sqrt((x2-x1)**2 + (y2-y1)**2)))