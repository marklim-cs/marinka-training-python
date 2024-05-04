import math
from dataclasses import dataclass
from abc import ABC, abstractmethod
from tkinter import Canvas, Tk, mainloop

def distance(point1: tuple, point2: tuple):
    '''Calculate the distance between two points in a 2-dimensional plane.'''
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

@dataclass
class Point():
    '''2D point'''
    x: float
    y: float

class Shape(ABC):
    '''abstract shape'''
    @abstractmethod
    def name(self) -> str:
        '''shape's name'''

    @abstractmethod
    def area(self) -> float:
        '''shape's area'''

    @abstractmethod
    def center(self) -> Point:
        '''shape's mass center'''

    @abstractmethod
    def draw(self, canvas: Canvas):
        '''draw a shape on a tkinter canvas'''

    @abstractmethod
    def __str__(self):
        pass

class Circle(Shape):
    '''Circle shape'''
    def __init__(self, radius: float, circle_center: Point):
        self.radius = radius
        self._center = circle_center

    def area(self) -> float:
        return math.pi * self.radius**2

    def center(self) -> Point:
        return self._center

    def name(self) -> str:
        return "Circle"

    def draw(self, canvas: Canvas):
        canvas.create_oval(
            self._center.x - self.radius, self._center.y - self.radius,
            self._center.x + self.radius, self._center.y + self.radius,
            fill= "yellow", outline= "purple" )

    def __str__(self):
        return f"{self.name()}(center={self._center}, radius={self.radius}"

class Triangle(Shape):
    '''Triangle shape'''
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def center(self) -> Point:
        '''Calculate the center (centroid) of the triangle.'''
        x = (self.a.x + self.b.x + self.c.x) / 3
        y = (self.a.y + self.b.y + self.c.y) / 3
        return Point(x, y)

    def sides(self):
        '''Calculate the lengths of the sides of a triangle given its vertices.'''
        a = distance(self.a, self.b)
        b = distance(self.b, self.c)
        c = distance(self.c, self.a)
        return a, b, c

    def area(self) -> float:
        '''Calculate the area of the triangle using Heron's formula.'''
        a, b, c = self.sides()
        s = (a + b + c) / 2
        triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return triangle_area

    def draw(self, canvas: Canvas):
        canvas.create_polygon(self.a.x, self.a.y, self.b.x, self.b.y, self.c.x, self.c.y,
                              fill= "green", width=5)

    def name(self) -> str:
        return "Triangle"

    def __str__(self):
        return f"{self.name()}({self.a}, {self.b}, {self.c})"

class Rectangle(Shape):
    '''Rectangle shape'''
    def __init__(self, top: int, left: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def center(self) -> Point:
        return Point(self.height/2, self.width/2)

    def name(self) -> str:
        return "Rectangle"

    def draw(self, canvas: Canvas):
        bottom_right_x = self.left + self.width
        bottom_right_y = self.top + self.height
        canvas.create_rectangle(self.left, self.top, bottom_right_x, bottom_right_y,
                                fill= "red", outline= "white")

    def __str__(self):
        return f"{self.name()}(top={self.top}, left={self.left}, width={self.width}, height={self.height})"


class Line(Shape):
    '''Line shape'''
    def __init__(self, endpoint_a: Point, endpoint_b: Point):
        self.a = endpoint_a
        self.b = endpoint_b

    def area(self) -> float:
        return 0.0

    def center(self) -> Point:
        x = (self.a.x + self.b.x) / 2
        y = (self.b.y + self.b.y) / 2
        return Point(x, y)

    def name(self) -> str:
        return "Line"

    def draw(self, canvas: Canvas):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill="purple", width=6)

    def __str__(self):
        return f"{self.name()}({self.a}, {self.b})"



master = Tk()
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

canvas_widget = Canvas(master,
                width=CANVAS_WIDTH,
                height=CANVAS_HEIGHT)
canvas_widget.pack()

shapes = [
    Line(Point(20, 35), Point(50, 50)),
    Line(Point(40, 35), Point(200, 50)),
    Rectangle(50, 20, 150, 80),
    Circle(50, Point(150, 75)),
    Triangle(Point(245, 200), Point(270, 50), Point(200, 90))
]
for shape in shapes:
    shape.draw(canvas_widget)
mainloop()
