# Question: Group Anagrams
# Write a program to group anagrams together from a given list of strings. Each group of anagrams should be printed on a separate line.

# Input:
# The first line contains an integer n, the number of strings.
# The second line contains n space-separated strings.
# Output:
# Print groups of anagrams, with each group on a new line.
# Strings within each group can be printed in any order, but the groups themselves should be sorted lexicographically by their first element.


def group_anagrams(n, strings):
    # Dictionary to store the indices of sorted strings
    index_map = {}
    # Initialize an empty list of lists using a loop
    result = []
    for i in range(n):
        result.append([])

    for i in range(n):
        # Sort the current string to form the key
        sorted_string = ''.join(sorted(strings[i]))
        
        if sorted_string in index_map:
            result[index_map[sorted_string]].append(strings[i])
        else:
            index_map[sorted_string] = i
            result[i].append(strings[i])

    for i in range(len(result)):
        if len(result[i]) > 0:  # Check for non-empty groups
            for word in result[i]:
                print(word, end=" ")
            print()  # Move to the next line


if __name__ == "__main__":
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input())
    

    group_anagrams(n, strings)
