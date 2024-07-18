import math

class GeometryCalculator:
    def __init__(self):
        pass

    def circle_area(self, radius):
        return math.pi * (radius ** 2)

    def triangle_area(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    def is_right_triangle(self, side1, side2, side3):
        sides = [side1, side2, side3]
        max_side = max(sides)
        sides.remove(max_side)
        return max_side**2 == sides[0]**2 + sides[1]**2