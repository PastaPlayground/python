# Python3 Program for recursive binary search.
# Returns index of x in arr if present, else -1

# l = first index
# r = last index
# x = element to find
import random


def binarySearch(arr, l, r, x):
    if r >= l:

        # find mid point of array
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


arr = []
n = 0
for i in range(0, 100):
    n += 1
    arr.append(n)
# arr = [2, 3, 4, 10, 40, 50, 90, 110, 30]

# sort the array
arr.sort()
# print(f"Array of given numbers: {arr}") 
x = int(input("Find index of number: "))

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
