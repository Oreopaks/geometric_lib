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

## [circle.py][https://github.com/Oreopaks/geometric_lib/blob/lab_num_two/circle.py]
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


# Hash commit

1. 98661bba2d4301c79cb80ea832f2903eb9265908 - Добавил Cube.py
2. a8031debfdd4f0725217b4340c00560dcd7462c6 - Исправил Cube.pu
3. 769f36f8a6b065af00c026b1344cf502e2fcd78c - Исправил Cube.py и добавил описание функций 
4. 48445662b045e708244ba38d2000afb8cac919a5 - Добавил описание функций в circle.py
5. 3b5e18bf44c51cbe68f1bde4db6f13dc1b69da18 - Добавил описание функций в square.py
6. e35e89ba68e1b65d8b1da7cf5caf401407d810b3 - Переписал README.dm