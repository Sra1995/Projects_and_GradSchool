#include <iostream>
#include <vector>
#include <algorithm>
#include <mpi.h>

using namespace std;

// Serial Bubble Sort
void bubbleSortSerial(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Parallel Bubble Sort (using MPI)
void bubbleSortParallel(vector<int>& arr, int rank, int size) {
    int n = arr.size();
    int local_n = n / size;
    vector<int> local_arr(local_n);

    MPI_Scatter(arr.data(), local_n, MPI_INT, local_arr.data(), local_n, MPI_INT, 0, MPI_COMM_WORLD);

    // Perform local bubble sort on each processor
    for (int i = 0; i < local_n - 1; i++) {
        for (int j = 0; j < local_n - i - 1; j++) {
            if (local_arr[j] > local_arr[j + 1]) {
                swap(local_arr[j], local_arr[j + 1]);
            }
        }
    }

    // Gather sorted subarrays back to root
    MPI_Gather(local_arr.data(), local_n, MPI_INT, arr.data(), local_n, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        // Final sort on root processor to combine segments
        bubbleSortSerial(arr);
    }
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int n = 1000; // Array size
    vector<int> arr(n);
    double time_serial = 0.0;  // Declare time_serial here

    if (rank == 0) {
        for (int i = 0; i < n; i++) {
            arr[i] = rand() % 1000;
        }

        // Serial Bubble Sort (only on rank 0 for comparison)
        vector<int> arr_serial = arr;
        double start_serial = MPI_Wtime();
        bubbleSortSerial(arr_serial);
        double end_serial = MPI_Wtime();
        time_serial = end_serial - start_serial;
        cout << "Time taken for Serial Bubble Sort: " << time_serial << " seconds" << endl;
    }

    // Parallel Bubble Sort
    vector<int> arr_parallel = arr;
    double start_parallel = MPI_Wtime();
    bubbleSortParallel(arr_parallel, rank, size);
    double end_parallel = MPI_Wtime();
    double time_parallel = end_parallel - start_parallel;

    if (rank == 0) {
        cout << "Time taken for Parallel Bubble Sort: " << time_parallel << " seconds" << endl;
        cout << "Speedup: " << (time_serial / time_parallel) << endl;
    }

    MPI_Finalize();
    return 0;
}