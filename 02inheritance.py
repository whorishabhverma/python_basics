# Base class (Parent class)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

# Derived class (Child class)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call the parent class constructor
        # //The super() function is used to call the parent class's constructor and methods.
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()}, Doors: {self.doors}"

# Another Derived class
class Motorcycle(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def display_info(self):
        return f"{super().display_info()}, Engine Capacity: {self.cc}cc"

# Creating objects
car = Car("Toyota", "Corolla", 4)
motorcycle = Motorcycle("Yamaha", "MT-15", 155)

# Accessing methods
print(car.display_info())         # Output: Brand: Toyota, Model: Corolla, Doors: 4
print(motorcycle.display_info())  # Output: Brand: Yamaha, Model: MT-15, Engine Capacity: 155cc
