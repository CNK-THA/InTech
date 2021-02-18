# import time
# start_time = time.time()
# main()
# print("--- %s seconds ---" % (time.time() - start_time))
#
#
# # Python program for implementation of Insertion Sort
#
# # Function to do insertion sort
# def insertionSort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#
#         key = arr[i]
#
#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#     # Driver code to test above
#
#
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# for i in range(len(arr)):
#     print("% d" % arr[i])
#
#     # This code is contributed by Mohit Kumra
#
# # Python
# # program
# # for implementation of Selection
# # Sort
# import sys
#
# A = [64, 25, 12, 22, 11]
#
# # Traverse through all array elements
# for i in range(len(A)):
#
#     # Find the minimum element in remaining
#     # unsorted array
#     min_idx = i
#     for j in range(i + 1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
#
#             # Swap the found minimum element with
#     # the first element
#     A[i], A[min_idx] = A[min_idx], A[i]
#
# # Driver code to test above
# print("Sorted array")
# for i in range(len(A)):
#     print("%d" % A[i]),
#
#
#
#
#
# # Python program for implementation of MergeSort
# def mergeSort(arr):
#     if len(arr) > 1:
#
#         # Finding the mid of the array
#         mid = len(arr) // 2
#
#         # Dividing the array elements
#         L = arr[:mid]
#
#         # into 2 halves
#         R = arr[mid:]
#
#         # Sorting the first half
#         mergeSort(L)
#
#         # Sorting the second half
#         mergeSort(R)
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
#
# # Code to print the list
#
#
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
#
# # Driver Code
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")
#     printList(arr)
#     mergeSort(arr)
#     print("Sorted array is: ", end="\n")
#     printList(arr)
#
# # This code is contributed by Mayank Khanna






def sort(array=['t','s','a','p','z','f']):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0] # use first element as the pivoi
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

print(sort())