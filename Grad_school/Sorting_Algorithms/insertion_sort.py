"""
Insertion sort Algorithm
resources used : programiz, Numpy.org

I had the option of generating unique integers without duplicates , but it was not stated in project 
so i left genrated integers to be completely random
"""

import numpy as np                          # import numpy module to use it to generate list of integers
import random                               # import random module to use it to generate list of random integers


data = np.random.randint(1, 2000001,65536)  # Generate an array with integers (from 1 to 2 million, size)


def insertionSort(array):
                                            # Iterate through the array, starting from the second element (index 1) to the end.
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
                                            # Compare key with each element on the left of it until an element smaller than it is found
                                            # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:    
            array[j + 1] = array[j]         # Shift elements to the right to make space for the key.
            j = j - 1                       # Move left to check the next element
        
                                            # Place key at after the element just smaller than it.
        array[j + 1] = key


# test data = [9, 5, 1, 4, 3]

                                            # perform insertion sort on data generated then print output of insertionsSort
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
