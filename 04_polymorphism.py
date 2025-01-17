# Parent class
class Animal:
    def speak(self):
        return "I make a sound"

# Child class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Child class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Child class 3
class Cow(Animal):
    def speak(self):
        return "Moo!"

# Using polymorphism
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())


# class Shape:
#     def area(self):
#         pass  # Placeholder for area method

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# # Using polymorphism
# shapes = [Circle(5), Rectangle(4, 6)]

# for shape in shapes:
#     print(f"Area: {shape.area()}")
# Explanation:
# Parent Class (Shape):

# Defines a common interface (area method) for all shapes.
# Child Classes (Circle, Rectangle):

# Implement their specific area calculations.
# Polymorphism:

# The area method dynamically calls the appropriate implementation based on the object type.
# this is polymorphism where the same method is overridden in the derived class

