# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Surface_Area
- Cube: S = 6a²

# Programs

## circle.py
- def area(r):
    Принимает r- радиус окружности и возвращает ее площадь return math.pi * r * r
- def perimeter(r):
    Принимает r - радиус окружности и возвращает ее периметр return 2 * math.pi * r

### Examples
    input: a = 6
    output: 113.09733552923255

    input: a = 6
    output: 37.69911184307752


## Cube.py
- def Surface_Area(a):
    Принимает a - длинну ребра куба и возвращает площадь его поверхности return 6*a**2

### Example
    input: a = 5
    output: 150


## square.py
- def area(a):
    Принимает a -  длинну стороны квадрата и возвращает его площадь return a * a
- def perimeter(a):
    Принимает a - длинну стороны квадрата и возвращает его площадь return 4 * a

### Examples
    input: a = 12
    output: 144

    input: a = 6
    output: 48