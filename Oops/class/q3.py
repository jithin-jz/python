# 3. Circle Class

# Create a class Circle with attribute radius.

# Add methods to calculate area() and perimeter().

# Create two circles and compare which has a bigger area.
import math

# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def area(self):
        return math.pi * self.radius**2

    # Method to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# Create two circles
circle1 = Circle(5)
circle2 = Circle(7)

# Print area and perimeter of both circles
print(
    f"Circle 1 - Radius: {circle1.radius}, Area: {circle1.area():.2f}, Perimeter: {circle1.perimeter():.2f}"
)
print(
    f"Circle 2 - Radius: {circle2.radius}, Area: {circle2.area():.2f}, Perimeter: {circle2.perimeter():.2f}"
)

# Compare which circle has a bigger area
if circle1.area() > circle2.area():
    print("Circle 1 has a bigger area.")
elif circle1.area() < circle2.area():
    print("Circle 2 has a bigger area.")
else:
    print("Both circles have the same area.")
