my_string = "Hello"
string_iterator = iter(my_string)

print(next(string_iterator))  # Output: H
print(next(string_iterator))  # Output: e

# Fibonccci iterator 
class Fibonacci:
    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

# Example usage
fib = Fibonacci(10)
for num in fib:
    print(num, end=" ")  # Output: 0 1 1 2 3 5 8

#     Right-Hand Side:

# self.b, self.a + self.b
# Python computes the new values for self.a and self.b:
# self.b is the new value for self.a.
# self.a + self.b (old values) is the new value for self.b.
# Left-Hand Side:

# self.a, self.b
# Python assigns the computed values to self.a and self.b.
