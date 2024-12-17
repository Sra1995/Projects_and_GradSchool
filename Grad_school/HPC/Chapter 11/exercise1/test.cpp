#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <math.h>
#include <time.h>

#define ARRAY_SIZE (1 << 28) // 2^20 elements
#define NUM_SEARCHES 2000
#define MASTER 0

// Function prototypes
int binary_search(int *array, int size, int target);
void generate_sorted_array(int *array, int size);

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 4) {
        if (rank == MASTER) {
            fprintf(stderr, "This program requires exactly 4 processes.\n");
        }
        MPI_Finalize();
        return EXIT_FAILURE;
    }

    int *array = NULL;
    int local_size = ARRAY_SIZE / size;
    int *local_array = (int *)malloc(local_size * sizeof(int));

    if (rank == MASTER) {
        // Generate a sorted array on the master process
        array = (int *)malloc(ARRAY_SIZE * sizeof(int));
        generate_sorted_array(array, ARRAY_SIZE);
    }

    // Scatter the array to all processes
    MPI_Scatter(array, local_size, MPI_INT, local_array, local_size, MPI_INT, MASTER, MPI_COMM_WORLD);

    int targets[NUM_SEARCHES];
    if (rank == MASTER) {
        // Generate random search targets
        srand(time(NULL));
        for (int i = 0; i < NUM_SEARCHES; i++) {
            targets[i] = rand() % ARRAY_SIZE;
        }
    }

    // Broadcast targets to all processes
    MPI_Bcast(targets, NUM_SEARCHES, MPI_INT, MASTER, MPI_COMM_WORLD);

    // Perform parallel binary search
    int local_results[NUM_SEARCHES] = {0};
    double start_time = MPI_Wtime();

    for (int i = 0; i < NUM_SEARCHES; i++) {
        local_results[i] = binary_search(local_array, local_size, targets[i]);
    }

    int global_results[NUM_SEARCHES] = {0};
    MPI_Reduce(local_results, global_results, NUM_SEARCHES, MPI_INT, MPI_LOR, MASTER, MPI_COMM_WORLD);

    double end_time = MPI_Wtime();

    // Serial binary search for comparison (run only on MASTER)
    if (rank == MASTER) {
        double serial_start_time = MPI_Wtime();
        for (int i = 0; i < NUM_SEARCHES; i++) {
            binary_search(array, ARRAY_SIZE, targets[i]);
        }
        double serial_end_time = MPI_Wtime();

        printf("Serial binary search time: %f seconds\n", serial_end_time - serial_start_time);
        printf("Parallel binary search time: %f seconds\n", end_time - start_time);

        // Clean up
        free(array);
    }

    free(local_array);
    MPI_Finalize();
    return EXIT_SUCCESS;
}

// Binary search function
int binary_search(int *array, int size, int target) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (array[mid] == target) {
            return 1; // Target found
        } else if (array[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return 0; // Target not found
}

// Generate a sorted array
void generate_sorted_array(int *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = i;
    }
}
