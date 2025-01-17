class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between two Vectors")
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

# Test addition
addition_result = vector1.add(vector2)
print(f"Addition Result: {addition_result}")  # Output: Vector(4, 6)
