from abc import ABC, abstractmethod

class Device(ABC):  # Abstract Base Class
    @abstractmethod
    def specs(self):
        pass 

class Laptop(Device):
    def specs(self):
        return "Laptop: 16GB RAM, i7 Processor"

class Smartphone(Device):
    def specs(self):
        return "Smartphone: 8GB RAM, Snapdragon Processor"

class Tablet(Device):
    def specs(self):
        return "Tablet: 4GB RAM, A12 Chip"

def show_specs(obj):
    print(obj.specs())  # Display directly

# Test cases
show_specs(Laptop())       # Output: Laptop: 16GB RAM, i7 Processor
show_specs(Smartphone())   # Output: Smartphone: 8GB RAM, Snapdragon Processor
show_specs(Tablet())       # Output: Tablet: 4GB RAM, A12 Chip
