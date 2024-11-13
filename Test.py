import unittest
import math

from circle import circle_area, circle_perimeter
from square import square_area, square_perimeter
from Cube import Surface_Area


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_area_minus(self):
        res = circle_area(-5)
        self.assertEqual(res, abs(math.pi * -5 * -5))

    def test_peperimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)
    
    def test_peperimeter_minus(self):
        res = circle_perimeter(-5)
        self.assertEqual(res,abs(2*-5*math.pi))

class squareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_area_minus(self):
        res = square_area(-5)
        self.assertEqual(res, 25)

    def test_peperimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)
    
    def test_peperimeter_minus(self):
        res = square_perimeter(-5)
        self.assertEqual(res, 20)

class CubeTestCase(unittest.TestCase):
    def test_Surface_Area_zero(self):
        res = Surface_Area(0)
        self.assertEqual(res, 0)

    def test_Surface_Area_minus(self):
        res = Surface_Area(-5)
        self.assertEqual(res, 150)