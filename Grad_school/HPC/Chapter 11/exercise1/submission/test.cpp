#include <stdio.h>                                                                                      // Standard I/O library
#include <stdlib.h>                                                                                     // Standard library for memory allocation, etc.
#include <mpi.h>                                                                                        // MPI library for parallel processing
#include <math.h>                                                                                       // Math library
#include <time.h>                                                                                       // Time library for random seed

#define ARRAY_SIZE (1 << 28)                                                                            // 2^28 elements
#define NUM_SEARCHES 2000                                                                               // Number of searches to perform
#define MASTER 0                                                                                        // Master process rank

                                                                                                        // Function prototypes
int binary_search(int *array, int size, int target);                                                    // Binary search function prototype
void generate_sorted_array(int *array, int size);                                                       // Function to generate a sorted array

int main(int argc, char **argv) {
    int rank, size;                                                                                     // Variables to store rank and size of MPI processes
    MPI_Init(&argc, &argv);                                                                             // Initialize MPI
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);                                                               // Get the rank of the process
    MPI_Comm_size(MPI_COMM_WORLD, &size);                                                               // Get the number of processes

    if (size != 4) {                                                                                    // Check if the number of processes is 4
        if (rank == MASTER) {                                                                           // Only the master process prints the error message
            fprintf(stderr, "This program requires exactly 4 processes.\n");
        }
        MPI_Finalize();                                                                                 // Finalize MPI
        return EXIT_FAILURE;                                                                            // Exit with failure
    }

    int *array = NULL;                                                                                  // Pointer to the array (only used by the master process)
    int local_size = ARRAY_SIZE / size;                                                                 // Size of the local array for each process
    int *local_array = (int *)malloc(local_size * sizeof(int));                                         // Allocate memory for the local array

    if (rank == MASTER) {                                                                               // Only the master process generates the sorted array
        array = (int *)malloc(ARRAY_SIZE * sizeof(int));                                                // Allocate memory for the array
        generate_sorted_array(array, ARRAY_SIZE);                                                       // Generate the sorted array
    }

                                                                                                        // Scatter the array to all processes
    MPI_Scatter(array, local_size, MPI_INT, local_array, local_size, MPI_INT, MASTER, MPI_COMM_WORLD);

    int targets[NUM_SEARCHES];                                                                          // Array to store search targets
    if (rank == MASTER) {                                                                               // Only the master process generates the search targets
        srand(time(NULL));                                                                              // Seed the random number generator
        for (int i = 0; i < NUM_SEARCHES; i++) {                                                        // Generate random search targets
            targets[i] = rand() % ARRAY_SIZE;                                                           // Random target within the array size
        }
    }

                                                                                                        // Broadcast targets to all processes
    MPI_Bcast(targets, NUM_SEARCHES, MPI_INT, MASTER, MPI_COMM_WORLD);

                                                                                                        // Perform parallel binary search
    int local_results[NUM_SEARCHES] = {0};                                                              // Array to store local search results
    double start_time = MPI_Wtime();                                                                    // Start timer for parallel search

    for (int i = 0; i < NUM_SEARCHES; i++) {                                                            // Perform binary search for each target
        local_results[i] = binary_search(local_array, local_size, targets[i]);                          // Store result
    }

    int global_results[NUM_SEARCHES] = {0};                                                             // Array to store global search results
    MPI_Reduce(local_results, global_results, NUM_SEARCHES, MPI_INT, MPI_LOR, MASTER, MPI_COMM_WORLD);  // Reduce results to master

    double end_time = MPI_Wtime();                                                                      // End timer for parallel search

                                                                                                        // Serial binary search for comparison (run only on MASTER)
    if (rank == MASTER) {
        double serial_start_time = MPI_Wtime();                                                         // Start timer for serial search
        for (int i = 0; i < NUM_SEARCHES; i++) {                                                        // Perform binary search for each target
            binary_search(array, ARRAY_SIZE, targets[i]);                                               // Perform search
        }
        double serial_end_time = MPI_Wtime();                                                           // End timer for serial search

        printf("Serial binary search time: %f seconds\n", serial_end_time - serial_start_time);         // Print serial search time
        printf("Parallel binary search time: %f seconds\n", end_time - start_time);                     // Print parallel search time

                                                                                                        // Clean up
        free(array);                                                                                    // Free the array
    }

    free(local_array);                                                                                  // Free the local array
    MPI_Finalize();                                                                                     // Finalize MPI
    return EXIT_SUCCESS;                                                                                // Exit successfully
}

                                                                                                        // Binary search function
int binary_search(int *array, int size, int target) {
    int low = 0, high = size - 1;                                                                       // Initialize low and high indices
    while (low <= high) {                                                                               // While there are elements to search
        int mid = low + (high - low) / 2;                                                               // Calculate mid index
        if (array[mid] == target) {                                                                     // If target is found
            return 1;                                                                                   // Return 1 (found)
        } else if (array[mid] < target) {                                                               // If target is greater than mid element
            low = mid + 1;                                                                              // Search in the right half
        } else {                                                                                        // If target is less than mid element
            high = mid - 1;                                                                             // Search in the left half
        }
    }
    return 0;                                                                                           // Return 0 (not found)
}

                                                                                                        // Generate a sorted array
void generate_sorted_array(int *array, int size) {
    for (int i = 0; i < size; i++) {                                                                    // Fill the array with sorted values
        array[i] = i;                                                                                   // Assign value
    }
}
