# Create a class called Point that has two attributes x-coordinate and y-coordinate. It should have method called dist_from_origin that should give how far point is from origin.  [Hint: 𝑑= √(𝑥^2 〖+𝑦〗^2 ) ]. Operator + should add as (x1+x2, y1+y2), – should implement (x1-x2, y1-y2). Print should display P(x, y). Also, overwrite relational operators that shows if point is smaller or greater based on distance from origin. (i.e. Overwrite <, >, <=, >=, == and !=). Initialize two point objects to demo above methods
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        """Calculate distance from origin (0,0) using Euclidean distance"""
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"P({self.x}, {self.y})"

    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    def __le__(self, other):
        return self.dist_from_origin() <= other.dist_from_origin()

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __ge__(self, other):
        return self.dist_from_origin() >= other.dist_from_origin()

    def __eq__(self, other):
        return math.isclose(self.dist_from_origin(), other.dist_from_origin())

    def __ne__(self, other):
        return not math.isclose(self.dist_from_origin(), other.dist_from_origin())


if __name__ == "__main__":

    p1 = Point(3, 4)
    p2 = Point(1, 2)

    print("Point 1:", p1)
    print("Point 2:", p2)

    print(f"Distance from origin for p1: {p1.dist_from_origin():.2f}")
    print(f"Distance from origin for p2: {p2.dist_from_origin():.2f}")

    p3 = p1 + p2
    print("p1 + p2 =", p3)

    p4 = p1 - p2
    print("p1 - p2 =", p4)

    print("p1 > p2:", p1 > p2)
    print("p1 < p2:", p1 < p2)
    print("p1 >= p2:", p1 >= p2)
    print("p1 <= p2:", p1 <= p2)
    print("p1 == p2:", p1 == p2)
    print("p1 != p2:", p1 != p2)

    p5 = Point(4, 3)
    print("\nPoint 5:", p5)
    print(f"Distance from origin for p5: {p5.dist_from_origin():.2f}")
    print("p1 == p5:", p1 == p5)
    print("p1 != p5:", p1 != p5)
