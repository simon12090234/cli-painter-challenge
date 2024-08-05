# TODO: Add code here
import matplotlib.pyplot as plt


class Point:

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:

    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self) -> float:
        return 3.1416 * self.radius ** 2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:
        x,y = self.center
        return f"Circle with center at ({x, y}) and radius r"


class Triangle:
        def __int__(self, point_1: Point, point_2: Point, point_3: Point):
            self.point_1: Point = point_1
            self.point_2: Point = point_2
            self.point_3: Point = point_3



