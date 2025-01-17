class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between two Vectors")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Subtraction is only supported between two Vectors")
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
def test_vector_operations():
    vector1 = Vector(3, 4)
    vector2 = Vector(1, 2)
    vector3 = Vector(3, 4)

    # Test addition
    addition_result = vector1 + vector2
    print(f"Addition Result: {addition_result}")  # Output: Vector(4, 6)

    # Test subtraction
    subtraction_result = vector1 - vector2
    print(f"Subtraction Result: {subtraction_result}")  # Output: Vector(2, 2)

    # Test equality
    equality_result1 = vector1 == vector2
    equality_result2 = vector1 == vector3
    print(f"Equality Test (vector1 == vector2): {equality_result1}")  # Output: False
    print(f"Equality Test (vector1 == vector3): {equality_result2}")  # Output: True

    # Test invalid addition
    try:
        invalid_result = vector1 + "invalid"
    except TypeError as e:
        print(f"Error: {e}")  # Output: Addition is only supported between two Vectors

test_vector_operations()
