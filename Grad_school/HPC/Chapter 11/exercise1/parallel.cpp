#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <mpi.h>

using namespace std;

int parallel_binary_search(const vector<int>& arr, int target, int rank, int size) {
    int chunk_size = arr.size() / size;
    int start = rank * chunk_size;
    int end = (rank == size - 1) ? arr.size() : (rank + 1) * chunk_size;

    int low = start, high = end - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    const int n = 1 << 20;
    vector<int> sorted_list(n);

    if (rank == 0) {
        for (int i = 0; i < n; ++i) {
            sorted_list[i] = i;
        }
    }

    MPI_Bcast(sorted_list.data(), n, MPI_INT, 0, MPI_COMM_WORLD);

    srand(time(0) + rank);
    int found = 0;
    clock_t start = clock();
    for (int i = 0; i < 2000; ++i) {
        int target = rand() % n;
        if (parallel_binary_search(sorted_list, target, rank, size) != -1) {
            found++;
        }
    }

    int total_found;
    MPI_Reduce(&found, &total_found, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        clock_t end = clock();
        double duration = double(end - start) / CLOCKS_PER_SEC;
        cout << "Parallel search completed in " << duration << " seconds, "
             << total_found << " targets found." << endl;
    }

    MPI_Finalize();
    return 0;
}