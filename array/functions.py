# Creating a list (array in Python)
arr = [1, 2, 3, 4, 5]
print("Initial Array:", arr)

# 1. Add elements to the list
arr.append(6)
print("After append(6):", arr)

arr.insert(2, 10)  # Insert 10 at index 2
print("After insert(2, 10):", arr)

# 2. Remove elements from the list
arr.remove(3)  # Removes the first occurrence of 3
print("After remove(3):", arr)

arr.pop(2)  # Removes the element at index 2
print("After pop(2):", arr)

# 3. Access and update elements in the list
print("Element at index 1:", arr[1])  # Access element by index
arr[1] = 20  # Update the element at index 1
print("After arr[1] = 20:", arr)

# 4. Slice and reverse the list
print("Slice of arr[1:4]:", arr[1:4])  # Slice the list
arr.reverse()  # Reverse the list
print("After reverse():", arr)

# 5. Find the length of the list
print("Length of arr:", len(arr))

# 6. Sort the list
arr.sort()
print("After sort():", arr)

# 7. Check membership in the list
print("Is 5 in arr?", 5 in arr)  # Check if 5 is in the list
print("Is 50 in arr?", 50 in arr)  # Check if 50 is in the list
