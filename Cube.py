def Surface_Area(a):
    '''Принимает a - длинну ребра куба и возвращает площадь его поверхности 
       input: a = 5
       output: 150'''
    return abs(6*a**2)



import unittest

class CubeTestCase(unittest.TestCase):
    def test_Surface_Area_zero(self):
        res = Surface_Area(0)
        self.assertEqual(res, 0)

    def test_Surface_Area_minus(self):
        res = Surface_Area(-5)
        self.assertEqual(res, 150)