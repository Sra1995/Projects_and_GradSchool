public class MatrixMultiplyThreaded {
    private static final int NUM_THREADS = 8;                        // Define number of threads (fixed at 8)
    private static int[][] result;                                   // Shared result matrix for threads

    public static int[][] multiply(int[][] A, int[][] B) {           // Threaded matrix multiplication method
        int n = A.length;                                            // Matrix size (assuming square matrices)
        result = new int[n][n];                                      // Initialize result matrix with zeroes

        Thread[] threads = new Thread[NUM_THREADS];                  // Create an array to hold threads
        int rowsPerThread = n / NUM_THREADS;                         // Rows handled by each thread

        for (int i = 0; i < NUM_THREADS; i++) {                      // Create and start threads
            final int startRow = i * rowsPerThread;                  // Starting row for this thread
            final int endRow = (i == NUM_THREADS - 1) ? n : startRow + rowsPerThread; // End row for this thread

            threads[i] = new Thread(() -> {                          // Lambda function for thread's task
                for (int row = startRow; row < endRow; row++) {      // Loop over assigned rows
                    for (int j = 0; j < n; j++) {                    // Loop through columns of B
                        result[row][j] = 0;                          // Initialize cell to 0
                        for (int k = 0; k < n; k++) {                // Loop through columns of A / rows of B
                            result[row][j] += A[row][k] * B[k][j];   // Perform multiplication and sum
                        }
                    }
                }
            });
            threads[i].start();                                      // Start the thread
        }

        for (Thread thread : threads) {                              // Join threads to ensure all finish
            try {
                thread.join();                                       // Wait for thread to finish
            } catch (InterruptedException e) {                       // Handle possible interruption
                e.printStackTrace();
            }
        }

        return result;                                               // Return the resulting matrix
    }

    public static int getNumThreads() {                              // Getter method for NUM_THREADS
        return NUM_THREADS;
    }
}