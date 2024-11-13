import math

def circle_area(r):
    '''Принимает r- радиус окружности и возвращает ее площадь
       input: a = 6
       output: 113.09733552923255
    '''
    return abs(math.pi * r * r)


def circle_perimeter(r):
    '''Принимает r - радиус окружности и возвращает ее периметр
       input: a = 6
       output: 37.69911184307752'''
    return abs(2 * math.pi * r)
