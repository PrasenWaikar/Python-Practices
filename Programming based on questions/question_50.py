#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

# Example usage:
circle = Circle(5)
print("Area of the circle:", circle.area())
