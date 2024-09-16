"""
Quick sort Algorithm
resources used : programiz, Numpy.org

I had the option of generating unique integers without duplicates , but it was not stated in project 
so i left genrated integers to be completely random
"""

import numpy as np                                  # import numpy module to use it to generate list of integers
import random                                       # import random module to use it to generate list of random integers


                                                    # Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size                             # Initialize the output array with zeros
    count = [0] * 10                                # Create a count array to store the count of elements for each digit (0-9)

                                                    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place                   # Get the digit at the given place for each element
        count[index % 10] += 1                      # Increment the count for the corresponding digit

                                                    # Calculate cumulative count to determine the correct positions of elements
    for i in range(1, 10):
        count[i] += count[i - 1]

                                                    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place                   # Get the digit at the given place for the current element
        output[count[index % 10] - 1] = array[i]    # Place the element in the output array
        count[index % 10] -= 1                      # Decrement the count for the digit
        i -= 1

    for i in range(0, size):                        # Copy the sorted elements from the output array back to the original array
        array[i] = output[i]


                                                    # Main function to implement radix sort
def radixSort(array):
                                                    # Get maximum element
    max_element = max(array)

                                                    # Apply counting sort to sort elements based on place value.
    place = 1                                       # Initialize the place value (starting from the least significant digit)
    while max_element // place > 0:                 # Apply counting sort to sort elements based on their place values (from least significant to most significant)
        countingSort(array, place)                  # Sort the array based on the current place value
        place *= 10                                 # Move to the next place value (tens, hundreds, thousands, etc.)


data = np.random.randint(1, 2000001,65536)          # Generate an array with integers (from 1 to 2 million, size)
radixSort(data)                                     # Perform radixsort on generated array
print(data)                                         # Display output of radixSort()
