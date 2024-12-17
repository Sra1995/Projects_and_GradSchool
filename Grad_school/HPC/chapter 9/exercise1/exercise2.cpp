#include <iostream>
#include <vector>
#include <algorithm>
#include <mpi.h>

using namespace std;

// Function to find median of 3 values
int medianOfThree(int a, int b, int c) {
    vector<int> vals = {a, b, c};                             // Store values in vector
    sort(vals.begin(), vals.end());                           // Sort vector
    return vals[1];                                           // Return middle element (median)
}

// MPI Function to find median using 3-value pivot approach
int findMedianMPI(vector<int>& arr, int rank, int size) {
    int n = arr.size();
    int local_n = n / size;                                   // Divide array across processes
    vector<int> local_arr(local_n);

    MPI_Scatter(arr.data(), local_n, MPI_INT, local_arr.data(), local_n, MPI_INT, 0, MPI_COMM_WORLD);

    // Find median of local data on each process
    sort(local_arr.begin(), local_arr.end());                 // Sort local array
    int local_median = local_arr[local_n / 2];                // Choose middle element as local median

    // Gather medians from all processes to root
    vector<int> medians(size);
    MPI_Gather(&local_median, 1, MPI_INT, medians.data(), 1, MPI_INT, 0, MPI_COMM_WORLD);

    int global_median = 0;
    if (rank == 0) {
        // Use 3-value pivot approach to select median of medians
        if (size >= 3) {
            global_median = medianOfThree(medians[0], medians[size / 2], medians[size - 1]);
        } else {
            global_median = medians[0];                       // Default to single median if only 1 process
        }
        cout << "Chosen Median: " << global_median << endl;
    }
    return global_median;
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    vector<int> sorted_data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};  // Sorted list for testing
    vector<int> unsorted_data = {10, 6, 7, 3, 1, 9, 2, 8, 4, 5}; // Unsorted list for testing

    if (rank == 0) {
        cout << "Testing with Sorted Data: ";
        for (int val : sorted_data) cout << val << " ";
        cout << endl;
    }
    findMedianMPI(sorted_data, rank, size);                     // Test with sorted data

    if (rank == 0) {
        cout << "\nTesting with Unsorted Data: ";
        for (int val : unsorted_data) cout << val << " ";
        cout << endl;
    }
    findMedianMPI(unsorted_data, rank, size);                   // Test with unsorted data

    MPI_Finalize();
    return 0;
}