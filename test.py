def brute_force_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [3, 5, 1, 4, 2]
target = 4
index = brute_force_search(arr, target)
print(f"Element {target} found at index {index}" if index != -1 else "Element not found")
