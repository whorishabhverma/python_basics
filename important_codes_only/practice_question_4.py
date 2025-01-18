def frogs_and_flies(frog_positions, tongue_sizes, fly_positions):
    # Initialize the result list with empty lists for each frog
    result = [[] for _ in frog_positions]

    for i in range(len(frog_positions)):
        xi = frog_positions[i]
        si = tongue_sizes[i]
        for fly in fly_positions:
            # If the fly is within the frog's reach
            if abs(xi - fly) <= si:
                result[i].append(fly)

    return result


# Example Input
frog_positions = [1, 5, 10]       # Frogs' positions
tongue_sizes =   [2, 1, 3]        # Frogs' tongue sizes
fly_positions =  [1, 3, 6, 9, 12]  # Flies' positions

# Compute which flies each frog can eat
result = frogs_and_flies(frog_positions, tongue_sizes, fly_positions)
 
# Output Result
for i, flies in enumerate(result):
    print(f"Frog {i + 1} at position {frog_positions[i]} can eat flies at: {flies}")
