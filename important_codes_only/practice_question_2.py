def reverse_words(input_string):
    words = input_string.split()
    reversed_words = []
    for word in words:
        reverWord = word[::-1]
        reversed_words.append(reverWord)
    
    result = " ".join(reversed_words)
    return result
input_string = input("enter string")
output = reverse_words(input_string);
print(output)