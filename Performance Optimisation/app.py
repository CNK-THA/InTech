import time
import numpy as np


#
# # Python program for implementation of Insertion Sort
#
# # Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Driver code to test above


start_time = time.time()
arr = np.random.randint(1,100,1000)
insertionSort(arr)
print("it took (seconds):", time.time() - start_time)

# print(arr)














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
#     # unsorted array22minimum element with
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






# def sort(array):
#     less = []
#     equal = []
#     greater = []

#     if len(array) > 1:
#         pivot = array[0] # use first element as the pivoi
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         # Don't forget to return something!
#         return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array

# array = [1,5,8,4,7,5,2]
# print(sort(array))




# def bubble_sort(our_list):
#     # We go through the list as many times as there are elements
#     for i in range(len(our_list)):
#         # We want the last pair of adjacent elements to be (n-2, n-1)
#         for j in range(len(our_list) - 1):
#             if our_list[j] > our_list[j+1]:
#                 # Swap
#                 our_list[j], our_list[j+1] = our_list[j+1], our_list[j]












# def countingSort(unsortedArray):
#     secondArray = [0] * (max(unsortedArray) + 1)
#     output = [0] * len(unsortedArray)
#     for element in unsortedArray:
#         secondArray[element] += 1
#     cumulative = 0
#     for i in range(0,len(secondArray)):
#         cumulative += secondArray[i]
#         secondArray[i] = cumulative
#     for element in unsortedArray:
#         output[secondArray[element] - 1] = element

#     return output


# unsortedArray = [9,3,6,5,7,2,1]
# print(countingSort(unsortedArray))











def linearSearch(array, x):
    index = 0
    for element in array:
        if element == x:
            return index
        index += 1
    return -1

# a = [1,2,3,4,5,6,7,8,9,10]
# a = [1,6,3,7,4,7,9,6,5,5,2,3]
# a = ['g','h','a','v','e']
# a = ['b','c','d','e','f','a','a']
# print(linearSearch(a, 'a'))




def binarySearch(array, startingIndex, endingIndex, x):
    if startingIndex == endingIndex: # we didn't found the element x
        return -1
    midPointIndex = (startingIndex + endingIndex) // 2
    midPointValue = array[midPointIndex]

    if x == midPointValue:
        return midPointIndex
    elif x < midPointValue:
        return binarySearch(array, 0, midPointIndex, x)
    elif x > midPointValue:
        return binarySearch(array, midPointIndex, len(array) - 1, x)
    
# a = [6,3,8,5,10,9,1,2,7]
# print(binarySearch(a, 0, len(a)-1, 2))


# import binarySearch from _____


def exponentialSearch(array,x):
    startingIndex = 0
    endingIndex = 0
    if array[startingIndex] == x:
        return startingIndex
    endingIndex += 1
    while endingIndex < len(array) and array[endingIndex] <= x:
        endingIndex *= 2
    return binarySearch(array, startingIndex, endingIndex, x)

# a = [1,2,3,4,5,6,7,8,9,10]
# print(exponentialSearch(a, 6))

def starTriangle(numberOfLine):
    currentLine = 1
    for x in range(0,numberOfLine):
        numberOfStars = currentLine + (x * 2)
        print(" " * (numberOfLine-x), "*" * numberOfStars)

starTriangle(10)