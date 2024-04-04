import math

def distance(point1: tuple, point2: tuple):
    '''Calculate the distance between two points in a 2-dimensional plane.'''
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


class Shape:
    '''superclass'''
    def name(self):
        '''shape's name'''
        raise NotImplementedError()
    
    def area(self) -> float:
        '''shape's area'''
        raise NotImplementedError()

    def center(self) -> tuple:
        '''shape's mass center'''
        raise NotImplementedError()

    def __str__(self):
        return f"name: {self.name()}, center: {self.center()}, area: {self.area()}"

class Circle(Shape):
    '''define Circle subclass'''
    def __init__(self, radius: float, circle_center: tuple):
        self.radius = radius
        self.circle_center = circle_center

    def area(self) -> float:
        return 3.14 * self.radius**2

    def center(self) -> tuple:
        return self.circle_center

    def name(self):
        return "Circle"

    def __str__(self):
        return f"{self.name()}(center={self.circle_center), radius={self.radius}"

class Triangle(Shape):
    '''define Triangle subclass'''
    def __init__(self, a: tuple, b: tuple, c: tuple):
        self.a = a
        self.b = b
        self.c = c

    def center(self) -> tuple:
        '''Calculate the center (centroid) of the triangle.'''
        x = (self.a[0] + self.b[0] + self.c[0]) / 3
        y = (self.a[1] + self.b[1] + self.c[1]) / 3
        return x, y

    def sides_length(self):
        '''Calculate the lengths of the sides of a triangle given its vertices.'''
        a = distance(self.a, self.b)
        b = distance(self.b, self.c)
        c = distance(self.c, self.a)
        return a, b, c

    def triabngle_area(self):
        '''Calculate the area of the triangle using Heron's formula.'''
        a, b, c = self.sides()
        s = (a + b + c) / 2
        triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return triangle_area

    def name(self):
        return "Triangle"

    def __str__(self):
        return f"{self.name()}({self.a}, {self.b}, {self.c})"

class Rectangle(Shape):
    '''define Rectangle subclass'''
    def __init__(self, top: int, left: int, width: int, height: int):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def center(self):
        return (self.height/2, self.width/2)

    def name(self):
        return "Rectangle"

    def __str__(self):
        return f"{self.name()}(top={self.top}, left={self.left}, width={self.width}, height={self.height})"

class Line(Shape):
    '''define Line subclass'''
    def __init__(self, endpoint_a: int, endpoint_b: int):
        self.a = endpoint_a
        self.b = endpoint_b

    def area(self):
        return 0.0

    def center(self) -> tuple:
        return (self.b-self.a)/2

    def name(self):
        return "Line"

    def __str__(self):
        return f"{self.name()}({self.a}, {self.b})"