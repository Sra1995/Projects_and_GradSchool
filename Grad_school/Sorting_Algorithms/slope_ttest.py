"""
Using python to perform slope, pvalue, ttest on data

I used a lot of resources from the internet stackoverflow, stackexchange, SciPy.org, pandas.pydata.org, copilate to fix code
"""
import pandas as pd
import numpy as np
from scipy import stats

import pandas as pd

# Define the data for Insertion-Sort
insertion_data = {
    'Algorithm': ['Insertion-Sort'] * 60,
    'size': ['128'] * 20 + ['1024'] * 20 + ['65536'] * 20,
    'execution time in (seconds)': [
        0.225, 0.13, 0.155, 0.158, 0.156, 0.173, 0.165, 0.169, 0.15, 0.146, 0.162, 0.157, 0.164, 0.148, 0.177, 0.156, 0.173, 0.147, 0.145, 0.16,
        0.216, 0.187, 0.208, 0.206, 0.219, 0.19, 0.187, 0.2, 0.181, 0.205, 0.202, 0.198, 0.199, 0.193, 0.21, 0.192, 0.186, 0.214, 0.193, 0.199,
        170.57, 170.561, 169.918, 171.407, 170.323, 170.151, 170.025, 169.942, 170.389, 170.415, 170.562, 169.449, 169.659, 169.707, 169.847, 170.221, 169.57, 170.304, 169.531, 168.85,
    ]
}

# Define the data for QuickSort
quicksort_data = {
    'Algorithm': ['QuickSort'] * 60,
    'size': ['128'] * 20 + ['1024'] * 20 + ['65536'] * 20,
    'execution time in (seconds)': [
        0.13, 0.126, 0.133, 0.126, 0.117, 0.132, 0.138, 0.13, 0.134, 0.119, 0.134, 0.141, 0.133, 0.142, 0.124, 0.133, 0.142, 0.13, 0.132, 0.132,
        0.138, 0.134, 0.139, 0.135, 0.13, 0.136, 0.13, 0.15, 0.13, 0.153, 0.121, 0.132, 0.13, 0.128, 0.135, 0.15, 0.135, 0.143, 0.138, 0.144,
        0.435, 0.422, 0.434, 0.411, 0.45, 0.395, 0.417, 0.392, 0.406, 0.448, 0.433, 0.435, 0.419, 0.435, 0.423, 0.416, 0.431, 0.421, 0.413, 0.423
    ]
}

# Define the data for Radix+Counting Sort
radix_data = {
    'Algorithm': ['Radix+Counting Sort'] * 60,
    'size': ['128'] * 20 + ['1024'] * 20 + ['65536'] * 20,
    'execution time in (seconds)': [
        0.168, 0.123, 0.12, 0.12, 0.13, 0.133, 0.135, 0.135, 0.122, 0.134, 0.135, 0.139, 0.128, 0.134, 0.132, 0.132, 0.128, 0.134, 0.124, 0.124,
        0.14, 0.132, 0.137, 0.134, 0.127, 0.133, 0.139, 0.142, 0.143, 0.121, 0.146, 0.126, 0.134, 0.129, 0.141, 0.135, 0.128, 0.125, 0.134, 0.136,
        0.408, 0.416, 0.413, 0.415, 0.418, 0.409, 0.411, 0.435, 0.42, 0.419, 0.398, 0.432, 0.417, 0.407, 0.408, 0.404, 0.429, 0.423, 0.405, 0.413
    ]
}

# Combine all the data into a single DataFrame
df = pd.concat([pd.DataFrame(insertion_data), pd.DataFrame(quicksort_data), pd.DataFrame(radix_data)], ignore_index=True)

# Print the first few rows of the combined DataFrame
print(df.head())


# Separate the data by algorithm and data size
insertion_data = df[(df['Algorithm'] == 'Insertion-Sort')]
quick_data_128 = df[(df['Algorithm'] == 'QuickSort') & (df['size'] == '128')]
radix_data = df[(df['Algorithm'] == 'Radix+Counting Sort')]

# Part 3: Calculate Expected vs. Actual Slopes
# Calculate expected slopes based on O() for Insertion, QuickSort (128), and Radix+Counting (128 to 1024 and 1024 to 65536)
expected_slope_insertion = (1024 - 128) / (128**2 - 1024**2)
expected_slope_quick_128 = (1024 - 128) / (128**2 - 1024**2)
expected_slope_radix_128_1024 = (1024 - 128) / (128**1 - 1024**1)
expected_slope_radix_1024_65536 = (65536 - 1024) / (1024**1 - 65536**1)

# Prepare actual time data and scale
insertion_time_128 = insertion_data[insertion_data['size'] == '128']['execution time in (seconds)']
quick_time_128 = quick_data_128['execution time in (seconds)']
radix_time_128 = radix_data[radix_data['size'] == 128]['execution time in (seconds)']
radix_time_1024 = radix_data[radix_data['size'] == 1024]['execution time in (seconds)']
radix_time_65536 = radix_data[radix_data['size'] == 65536]['execution time in (seconds)']

# Scale the times by a factor to ensure they are greater than 1
scaling_factor = 1000
insertion_time_128_scaled = insertion_time_128 * scaling_factor
quick_time_128_scaled = quick_time_128 * scaling_factor
radix_time_128_scaled = radix_time_128 * scaling_factor
radix_time_1024_scaled = radix_time_1024 * scaling_factor
radix_time_65536_scaled = radix_time_65536 * scaling_factor

# Calculate actual slopes
actual_slope_insertion = (insertion_time_128_scaled.mean() - insertion_time_128_scaled.max()) / (128 - 1024)
actual_slope_quick_128 = (quick_time_128_scaled.mean() - quick_time_128_scaled.max()) / (128 - 1024)
actual_slope_radix_128_1024 = (radix_time_128_scaled.mean() - radix_time_1024_scaled.max()) / (128 - 1024)
actual_slope_radix_1024_65536 = (radix_time_1024_scaled.mean() - radix_time_65536_scaled.max()) / (1024 - 65536)

# Print the results
print("Expected Slope for Insertion: ", expected_slope_insertion)
print("Actual Slope for Insertion: ", actual_slope_insertion)
print("Expected Slope for QuickSort (128): ", expected_slope_quick_128)
print("Actual Slope for QuickSort (128): ", actual_slope_quick_128)
print("Expected Slope for Radix+Counting (128 to 1024): ", expected_slope_radix_128_1024)
print("Actual Slope for Radix+Counting (128 to 1024): ", actual_slope_radix_128_1024)
print("Expected Slope for Radix+Counting (1024 to 65536): ", expected_slope_radix_1024_65536)
print("Actual Slope for Radix+Counting (1024 to 65536): ", actual_slope_radix_1024_65536)

# Part 4: Perform T-Tests
# Perform t-test for data size = 65536
t_statistic_insertion_vs_quick = stats.ttest_ind(insertion_time_128_scaled, quick_time_128_scaled)
t_statistic_insertion_vs_radix = stats.ttest_ind(insertion_time_128_scaled, radix_time_65536_scaled)
t_statistic_quick_vs_radix = stats.ttest_ind(quick_time_128_scaled, radix_time_65536_scaled)

# Print the t-test results
print("T-Test Results (Data Size = 65536):")
print("Insertion vs. Quick: ", t_statistic_insertion_vs_quick)
print("Insertion vs. Radix+Counting: ", t_statistic_insertion_vs_radix)
print("Quick vs. Radix+Counting: ", t_statistic_quick_vs_radix)
