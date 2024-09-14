# CSE-5311-Hands-On-4
CSE 5311 Assignment 4

Problem 0
Fibonachi sequence is implemented in fibonacci_sequence.py
Comments show the step by step calculation and function call stack of fib(5)

Problem 1
1. Implementation is found in merge_sorted_arrays.py
2. Time complexity is shown in the comments as T(n) = O(n * K * logK)
3. One way to improve the implementation is to use a priority queue or heap, pushing all first elements of k arrays into the heap. The lowest of the heap is put into the array, and the next element is pushed to the heap. Process repeats until the heap is empty and all elements are now in the merged sorted array.

Problem 2
1. Implementation is found in remove_duplicates.py
2. Time complexity is shown in the comments as O(n)
3. One way to improve this implementation is to check for arrays containing one element, as there is no need to process the removal of a single element.
