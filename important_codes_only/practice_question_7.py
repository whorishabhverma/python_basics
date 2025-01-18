# Extracting a substring using slicing
text = "Hello, Python!"
substring = text[7:13]  # Characters from index 7 to 12
print(substring)  # Output: Python

# Check if a substring exists in a string
if "Python" in text:
    print("Substring found!")



# Sort a string
text = "python"
sorted_text = ''.join(sorted(text))  # ''.join() combines the sorted characters
print(sorted_text)  # Output: hnopty


# Reverse a string
text = "Python"
reversed_text = text[::-1]
print(reversed_text)  # Output: nohtyP



# Use map to square each number in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]


# List:
# Mutable (can change).
# Ordered collection.
# Allows duplicate items.
# python

# List example
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an item
print(fruits[1])  # Access an item by index



# Tuple:
# Immutable (cannot change after creation).
# Ordered collection.
# Allows duplicate items.
# Tuple example
coordinates = (10, 20, 30)
print(coordinates[1])  # Access an item by index
coordinates[2]=30 # typeError : tuple object does no support item assignment


# Dictionary:
# Mutable.
# Unordered collection (as of Python 3.7+, insertion order is preserved).
# Key-value pairs.
# Dictionary example
person = {"name": "Rishabh", "age": 21}
print(person["name"])  # Access a value by key
person["age"] = 22  # Update a value



# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Example of break and continue
for num in range(1, 6):
    if num == 3:
        continue  # Skip this iteration
    if num == 5:
        break  # Exit the loop
    print(num)




student_names = {"rishabh": 12, "gaurav": 13, "gargi": 14}
for name, marks in student_names.items():  # Use .items() to get key-value pairs
    print(f"Student name is {name} and marks are {marks}")



# Example of .values() in Dictionaries
names = student_names.keys()
print(list(names))
