def merge_all_arrays(arrays):
    if not arrays:
        return []

    while len(arrays) > 1:
        new_arrays = []

        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                arr1 = arrays[i]
                arr2 = arrays[i + 1]

                res = []
                k = 0
                j = 0

                while k < len(arr1) and j < len(arr2):
                    if arr1[k] < arr2[j]:
                        res.append(arr1[k])
                        k += 1
                    else:
                        res.append(arr2[j])
                        j += 1

                res.extend(arr1[k:])
                res.extend(arr2[j:])

                merged = res
            else:
                merged = arrays[i]
            new_arrays.append(merged)

        arrays = new_arrays

    return arrays[0]


# Example usage
arrays1 = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
print("Merged array 1:", merge_all_arrays(arrays1))

arrays2 = [
    [1, 3, 7],
    [2, 4, 8],
    [9, 10, 11]
]
print("Merged array 2:", merge_all_arrays(arrays2))

#def merge_all_arrays(arrays):                          // Time complexity
#    if not arrays:                                     // Runs once - O(1)
#        return []                                      //

#    while len(arrays) > 1:                             // Runs until one array left
#        new_arrays = []                                // K arrays - O(Log(K))

#        for i in range(0, len(arrays), 2):             // Through K in 2 steps - O(K/2)
#            if i + 1 < len(arrays):                    //
#                arr1 = arrays[i]                       //
#                arr2 = arrays[i + 1]                   //

#                res = []                               // O(1) each time
#                k = 0                                  //
#                j = 0                                  //

#                while k < len(arr1) and j < len(arr2): // Goes through both arrays of N - O(N)
#                    if arr1[k] < arr2[j]:              //
#                        res.append(arr1[k])            //
#                        k += 1                         //
#                    else:                              //
#                        res.append(arr2[j])            //
#                        j += 1                         //

#                res.extend(arr1[k:])                   // Also O(N)
#                res.extend(arr2[j:])                   //

#                merged = res                           // O(1)
#            else:                                      //
#                merged = arrays[i]                     //
#           new_arrays.append(merged)                   //

#        arrays = new_arrays                            // merged back to arrays - O(N * K)
#
#    return arrays[0]                                   // O(1)

# Merging pairs of arrays takes O(N * K)
# While loop runs O(LogK) through K arrays
# overall complexity becomes O(N * K * LogK)
