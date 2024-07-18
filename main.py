import math
from defs import GeometryCalculator

# Юнит-тесты
def test_circle_area():
    gc = GeometryCalculator()
    assert gc.circle_area(radius) == 25 * math.pi

def test_triangle_area():
    gc = GeometryCalculator()
    assert gc.triangle_area(side1, side2, side3) == 6

def test_is_right_triangle():
    gc = GeometryCalculator()
    assert gc.is_right_triangle(side1, side2, side3) == True

if __name__ == "__main__":
    gc = GeometryCalculator()

    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Triangle")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle:", gc.circle_area(radius))
    elif choice == 2:
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
        print("Area of the triangle:", gc.triangle_area(side1, side2, side3))
        if gc.is_right_triangle(side1, side2, side3):
            print("The triangle is a right-angled triangle.")
        else:
            print("The triangle is not a right-angled triangle.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

