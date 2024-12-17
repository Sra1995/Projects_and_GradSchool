import time
import random
from multiprocessing import Pool

# Function to merge two sorted halves
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Sequential merge sort function (used in parallel processes)
def sequential_merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left_sorted = sequential_merge_sort(left)
    right_sorted = sequential_merge_sort(right)
    return merge(left_sorted, right_sorted)

# Top-level parallel merge sort function
def parallel_merge_sort(array):
    if len(array) <= 1:
        return array

    # Split array into 4 parts to be handled in parallel
    n = len(array)
    quarters = [array[i * n // 4: (i + 1) * n // 4] for i in range(4)]

    # Use a pool to process the 4 parts in parallel
    with Pool(processes=4) as pool:
        sorted_quarters = pool.map(sequential_merge_sort, quarters)

    # Sequentially merge the 4 sorted parts
    first_half = merge(sorted_quarters[0], sorted_quarters[1])
    second_half = merge(sorted_quarters[2], sorted_quarters[3])
    return merge(first_half, second_half)

# Timing function
def time_function(func, array):
    start_time = time.time_ns()  # Time in nanoseconds
    sorted_array = func(array)
    end_time = time.time_ns()  # Time in nanoseconds
    return sorted_array, end_time - start_time

if __name__ == '__main__':
    # Generate an array of 1,000,000 random integers between 1 and 1,000,000 or other sizes for other marks
    array = [random.randint(1, 1000000) for _ in range(1000000)] 

    # Print the array (first 20 elements for brevity)
    print("Original array (first 20 elements):", array[:20])

    # Normal merge sort
    normal_sorted, normal_time = time_function(sequential_merge_sort, array.copy())
    print(f"\nTime taken by normal merge sort: {normal_time/1000} nanoseconds")

    # Parallel merge sort
    parallel_sorted, parallel_time = time_function(parallel_merge_sort, array.copy())
    print(f"Time taken by parallel merge sort: {parallel_time/1000} nanoseconds")

    # Displaying the first 20 elements of the sorted arrays for brevity
    print("\nSorted array (first 20 elements):", parallel_sorted[:20])