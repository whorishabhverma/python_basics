given_string = "iloveyou"
cnt = 0
for i in given_string:
    if i in 'aeiou':
        cnt += 1
print(cnt)

# Reverse the words in a string
given_string = "fun is Python"
words = given_string.split()
reversed_words = " ".join(reversed(words))
print(reversed_words)

# Find the student with the highest marks
students = {"rishabh": 9, "gaurav": 122, "rishi": 43, "ritisha": 32, "deepshika": 12}
maxi = max(students.values())
for name, marks in students.items():
    if marks == maxi:
        print(f"Topper: {name}, Marks: {marks}")



# Merge Two Dictionaries with Summed Values
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}
merged_dict = {}

for key in set(dict1.keys()).union(dict2.keys()):
    merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(merged_dict)  # Output: {'a': 10, 'b': 50, 'c': 40}


# remove last char from string
string = "Hello!"
string = string[:-1]  # Removes the last character
print(string)  # Output: Hello


# Get a specific value using a key:
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')  # Safely fetches the value for key 'b'
print(value)  # Output: 2
