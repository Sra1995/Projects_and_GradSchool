"""
Quick sort Algorithm
resources used : programiz, Numpy.org

I had the option of generating unique integers without duplicates , but it was not stated in project 
so i left genrated integers to be completely random
"""

import numpy as np                              # import numpy module to use it to generate list of integers
import random                                   # import random module to use it to generate list of random integers


                                                # function to find the partition position
def partition(array, low, high):

                                                # choose the rightmost element as pivot
  pivot = array[high]

                                                # pointer for greater element
  i = low - 1

                                                # traverse through all elements
                                                # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
                                                # if element smaller than pivot is found
                                                # swap it with the greater element pointed by i
      i = i + 1

                                                # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

                                                # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

                                                # return the position from where partition is done
  return i + 1

                                                # function to perform quicksort
def quickSort(array, low, high):
  if low < high:

                                                # find pivot element such that
                                                # element smaller than pivot are on the left
                                                # element greater than pivot are on the right
    pi = partition(array, low, high)

                                                # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

                                                # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

data = np.random.randint(1, 2000001,65536)      # Generate an array with integers (from 1 to 2 million, size)
size = len(data)

quickSort(data, 0, size - 1)                    # Perform quicksort function on generated array

print('Sorted Array in Ascending Order:')
print(data)                                     # Display output/result of quicksort


