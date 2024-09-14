def remove_duplicates(arr):
    if not arr:
        return 0

    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    return arr[:j + 1]

input_array = [2, 2, 2, 2, 2]
output_array = remove_duplicates(input_array)
print(output_array)

input_array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
output_array = remove_duplicates(input_array)
print(output_array)

# def remove_duplicates(arr):       // Time complexity
#     if not arr:                   // Checks once - O(1)
#        return 0                   // one operation if true - O(1)

#     j = 0                         // one operation O(1)

#     for i in range(1, len(arr)):  // loop through arr from arr[1] - O(n - 1)
#         if arr[i] != arr[j]:      // checks once in loop - O(1)
#             j += 1                // once if true in loop - O(1)
#             arr[j] = arr[i]       // once if true in loop - O(1)

#     return arr[:j + 1]            // one operation - O(1)

# Dominated by O(n - 1) for loop
# Dominated by O(n) term
# Time complexity is O(n)
