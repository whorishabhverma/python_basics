class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("Unsupported operand type(s) for +: 'Point' and '{}'".format(type(other).__name__))

    def __str__(self):
        return f"({self.x}, {self.y})"

# Example usage
p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2  # Calls the __add__ method
print(result)  # Output: (6, 8)
