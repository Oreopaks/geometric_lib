import math

def area(r):
    '''Принимает r- радиус окружности и возвращает ее площадь'''
    return abs(math.pi * r * r)


def perimeter(r):
    '''Принимает r - радиус окружности и возвращает ее периметр'''
    return abs(2 * math.pi * r)

import unittest

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_minus(self):
        res = area(-5)
        self.assertEqual(res, math.pi*5*5)

    def test_peperimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_peperimeter_minus(self):
        res = perimeter(-5)
        self.assertEqual(res,2*5*math.pi)