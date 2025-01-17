from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method with no implementation

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method with no implementation

# Concrete Class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Concrete Class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Accessing abstract methods implemented in concrete classes
print(f"Rectangle Area: {rectangle.area()}")       # Output: Rectangle Area: 20
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Perimeter: 18
print(f"Circle Area: {circle.area()}")             # Output: Circle Area: 28.26
print(f"Circle Perimeter: {circle.perimeter()}")   # Output: Circle Perimeter: 18.84

# Abstraction is a principle of object-oriented programming (OOP) where only essential details are shown to the user while the implementation details are hidden. It is achieved using abstract classes and abstract methods.
# In Python, abstraction is implemented using the abc module (Abstract Base Classes).

