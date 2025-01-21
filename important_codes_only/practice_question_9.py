def strictly_increasing(start, end, arr):
    for i in range(start, end - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

def strictly_decreasing(start, end, arr):
    for i in range(start, end - 1):
        if arr[i] <= arr[i + 1]:
            return False
    return True

def solve(arr):
    n = len(arr)
    if n < 3:
        return False  # Less than 3 elements cannot form the required pattern

    # Check if the array is fully increasing or fully decreasing
    if strictly_increasing(0, n, arr) or strictly_decreasing(0, n, arr):
        return False

    for i in range(1, n):
        if strictly_increasing(0, i, arr) and strictly_decreasing(i, n, arr):
            return True
        if strictly_decreasing(0, i, arr) and strictly_increasing(i, n, arr):
            return True

    return False

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    result = solve(arr)
    output = "YES" if result else "NO"
    print(f"Result: {output}")
