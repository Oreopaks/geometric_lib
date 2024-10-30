def area(a):
    '''Принимает a -  длинну стороны квадрата и возвращает его площадь'''
    return abs(a * a)

def perimeter(a):
    '''Принимает a - длинну стороны квадрата и возвращает его площадь'''
    return abs(4 * a)

import unittest

class squareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_minus(self):
        res = area(-5)
        self.assertEqual(res, 25)

    def test_peperimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_peperimeter_minus(self):
        res = perimeter(-5)
        self.assertEqual(res, 20)