# String Functions

# 1. len() - Returns the length of the string
s = "Hello, World!"
print(len(s))  # Output: 13

# 2. lower() - Converts all characters to lowercase
print(s.lower())  # Output: hello, world!

# 3. upper() - Converts all characters to uppercase
print(s.upper())  # Output: HELLO, WORLD!

# 4. capitalize() - Capitalizes the first character
print(s.capitalize())  # Output: Hello, world!

# 5. title() - Capitalizes the first letter of each word
print(s.title())  # Output: Hello, World!

# 6. strip() - Removes leading and trailing whitespaces
s2 = "   Hello   "
print(s2.strip())  # Output: Hello

# 7. replace() - Replaces a substring with another substring
print(s.replace("World", "Python"))  # Output: Hello, Python!

# 8. split() - Splits the string into a list based on the delimiter
print(s.split(", "))  # Output: ['Hello', 'World!']

# 9. find() - Returns the lowest index of the substring
print(s.find("World"))  # Output: 7

# 10. count() - Returns the number of occurrences of a substring
print(s.count("o"))  # Output: 2

# 11. isalpha() - Checks if all characters in the string are alphabets
print(s.isalpha())  # Output: False

# 12. isnumeric() - Checks if the string contains only numbers
print(s.isnumeric())  # Output: False

# 13. isdigit() - Checks if all characters in the string are digits
print("123".isdigit())  # Output: True

# 14. startswith() - Checks if the string starts with the specified prefix
print(s.startswith("Hello"))  # Output: True

# 15. endswith() - Checks if the string ends with the specified suffix
print(s.endswith("!"))  # Output: True

# 16. join() - Joins the elements of a sequence with a specified delimiter
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World

# 17. rfind() - Returns the highest index of the substring
print(s.rfind("o"))  # Output: 8

# 18. format() - Formats the string using placeholders
name = "Alice"
print("Hello, {}".format(name))  # Output: Hello, Alice

# 19. islower() - Checks if all characters in the string are lowercase
print(s.islower())  # Output: False

# 20. isupper() - Checks if all characters in the string are uppercase
print(s.isupper())  # Output: False

