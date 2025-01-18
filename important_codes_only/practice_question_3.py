def group_identical_strings(strings):
    groups = {}
    
    for word in strings:
        # Sort the characters in the word to create a key
        key = ''.join(sorted(word))
        
        # Group the words by their sorted character key
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    
    # Return the grouped values
    return list(groups.values())

# Example input
strings = ["good", "god", "abc", "bac"]
result = group_identical_strings(strings)
print(result)
# Print the groups
for group in result:
    print(" ".join(group))
