# # 1. String Reversal
# # Write a Python function that takes a string as input and returns the string reversed. Try to do it without using Python's built-in reverse() or slicing.

str = input("enter a string")
temp = ''
n = len(str)
# for i in range(0,n):
#     temp = str[i]
#     str[i] = str[n-i-1]
#     str[n-i-1] = temp
# print(str)    
# above code is wrong because strings are immutable in Python

#1 way
for i in range(n-1,-1,-1):
    temp+=str[i]
print(temp)

#2 way 
reversedString = str[::-1]
print(reversedString)

#3 way
revString  = ''.join(reversed(str))
print(revString)


#find longest word
def find_longest_word(str1):
    words = str1.split()
    longest_word = max(words, key=len)
    return longest_word

str1 = input("Enter a string: ")
longest_word = find_longest_word(str1)
print("Longest word:", longest_word)
