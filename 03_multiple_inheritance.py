# Parent class 1
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def show_engine_info(self):
        return f"Engine Horsepower: {self.horsepower} HP"

# Parent class 2
class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def show_wheel_info(self):
        return f"Number of Wheels: {self.wheel_count}"

# Child class
class Car(Engine, Wheels):
    def __init__(self, brand, model, horsepower, wheel_count):
        Engine.__init__(self, horsepower)  # Initialize from Engine class
        Wheels.__init__(self, wheel_count)  # Initialize from Wheels class
        self.brand = brand
        self.model = model

    def show_car_info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, " +
                self.show_engine_info() + ", " +
                self.show_wheel_info())

# Creating an object
my_car = Car("Tesla", "Model S", 1020, 4)

# Accessing methods
print(my_car.show_car_info())
