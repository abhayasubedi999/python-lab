# Your company is hosting a party. Detail of employee is stored in info.csv containing name,DOB,mobile_number. Write a program that reads csv file, determines number of soft drink or hard drink required and store result in JSON file as: {“hard_drink”: num_1, “soft_drink”: num_2}. Assume 1 drink per user and use function of 1 and 2 to determine the drink for user​
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Addition operator (+)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Subtraction operator (-)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # String representation (print)
    def __repr__(self):
        return f"P({self.x}, {self.y})"

    # Less than (<)
    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    # Less than or equal (<=)
    def __le__(self, other):
        return self.dist_from_origin() <= other.dist_from_origin()

    # Greater than (>)
    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    # Greater than or equal (>=)
    def __ge__(self, other):
        return self.dist_from_origin() >= other.dist_from_origin()

    # Equal (==)
    def __eq__(self, other):
        return math.isclose(self.dist_from_origin(), other.dist_from_origin())

    # Not equal (!=)
    def __ne__(self, other):
        return not math.isclose(self.dist_from_origin(), other.dist_from_origin())


# Demonstration
if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(1, 2)

    print("Point 1:", p1)  # P(3, 4)
    print("Point 2:", p2)  # P(1, 2)

    print("Distance from origin for p1:", p1.dist_from_origin())  # 5.0
    print("Distance from origin for p2:", p2.dist_from_origin())  # 2.236

    p3 = p1 + p2
    print("p1 + p2:", p3)  # P(4, 6)

    p4 = p1 - p2
    print("p1 - p2:", p4)  # P(2, 2)

    # Relational operators
    print("p1 > p2:", p1 > p2)  # True
    print("p1 < p2:", p1 < p2)  # False
    print("p1 == p2:", p1 == p2)  # False
    print("p1 != p2:", p1 != p2)  # True
