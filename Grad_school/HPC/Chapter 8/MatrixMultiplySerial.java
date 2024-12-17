public class MatrixMultiplySerial {

    public static int[][] multiply(int[][] A, int[][] B) {           // Serial matrix multiplication method
        int n = A.length;                                            // Matrix size (assuming square matrices)
        int[][] result = new int[n][n];                              // Initialize result matrix with zeroes

        for (int i = 0; i < n; i++) {                                // Loop through rows of A
            for (int j = 0; j < n; j++) {                            // Loop through columns of B
                result[i][j] = 0;                                    // Initialize each cell in result to 0
                for (int k = 0; k < n; k++) {                        // Loop through columns of A / rows of B
                    result[i][j] += A[i][k] * B[k][j];               // Perform multiplication and sum
                }
            }
        }
        return result;                                               // Return the resulting matrix
    }
}