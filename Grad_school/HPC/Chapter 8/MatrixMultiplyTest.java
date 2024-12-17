import java.util.Random;

public class MatrixMultiplyTest {                                           

    public static boolean areEqual(int[][] matrix1, int[][] matrix2) {      // Helper method to compare two matrices takes two arrays
        int n = matrix1.length;                                             // variable n is the length of the matrix
        for (int i = 0; i < n; i++) {                                       // loop through the rows of the matrix
            for (int j = 0; j < n; j++) {                                   // loop through the columns of the matrix
                if (matrix1[i][j] != matrix2[i][j]) {                       // if the values of the two matrices are not equal
                    return false;                                           // return false
                }
            }
        }
        return true;                                                        // return true if the matrices are equal
    }

    public static boolean verifyCorrectness() {                             // Helper method to verify correctness of both versions
                                                                            // Define small, known matrices and expected output
        int[][] A = {{1, 2}, {3, 4}};                                       // Define small, known matrices and expected output
        int[][] B = {{2, 0}, {1, 2}};                                       // Define small, known matrices and expected output
        int[][] expected = {{4, 4}, {10, 8}};                               // Calculated manually: A * B
        
                                                                            // Run both versions on this small input
        int[][] serialResult = MatrixMultiplySerial.multiply(A, B);
        int[][] threadedResult = MatrixMultiplyThreaded.multiply(A, B);
        
                                                                            // Check if both versions match the expected correct result
        return areEqual(serialResult, expected) && areEqual(threadedResult, expected);
    }

                                                                            // Generates an n x n matrix filled with random integers (0-9)
    public static int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];                                     // Create a new matrix of size n x n
        Random rand = new Random();                                         // Create a new random object idk java is weird
        
        for (int i = 0; i < n; i++) {                                       // Loop through the rows of the matrix
            for (int j = 0; j < n; j++) {                                   // Loop through the columns of the matrix
                matrix[i][j] = rand.nextInt(10);                      // Random values between 0 and 9
            }
        }
        return matrix;                                                      // Return the matrix
    }

    public static void main(String[] args) {                                // Main method
        if (verifyCorrectness()) {
            System.out.println("Serial and Threaded versions are verified as correct on a known example.");
        } else {
            System.out.println("Serial and/or Threaded versions failed on a known example. Review implementation.");
            return;
        }
        
        // Proceed with larger 4096x4096 matrix tests
        int n = 4096;
        int[][] A = generateMatrix(n);
        int[][] B = generateMatrix(n);

        long start = System.nanoTime();                                         // Start the timer in nanoseconds
        int[][] serialResult = MatrixMultiplySerial.multiply(A, B);             // Run the serial version
        long end = System.nanoTime();                                           // End the timer in nanoseconds
        System.out.println("Serial Time (ms): " + (end - start) / 1_000_000);   // Print the time taken in milliseconds

        start = System.nanoTime();                                              // Start the timer in nanoseconds
        int[][] threadedResult = MatrixMultiplyThreaded.multiply(A, B);         // Run the threaded version
        end = System.nanoTime();                                                // End the timer in nanoseconds
        System.out.println("Threaded Time (ms): " + (end - start) / 1_000_000); // Print the time taken in milliseconds
                                                                                // if the two matrices are equal state that otherwise state that they are not
        if (areEqual(serialResult, threadedResult)) {
            System.out.println("Both methods give the same result for the large matrix.");
        } else {
            System.out.println("Results differ for the large matrix.");
        }

        int cores = Runtime.getRuntime().availableProcessors();                 // Get the number of available cores of the system
        System.out.println("Number of Cores: " + cores);                        // Print the number of cores
                                                                                // if the number of threads is less than the number of cores state that more threads could be used
        if (MatrixMultiplyThreaded.getNumThreads() < cores) {
            System.out.println("We could use more threads to better utilize available cores.");
        } else {
            System.out.println("Using optimal or close-to-optimal threads for available cores.");
        }
    }
}