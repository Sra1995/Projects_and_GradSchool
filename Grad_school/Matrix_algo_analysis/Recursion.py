"""
    This file runs Recursion algorithm on two generated matrices.
    before checking the matrices it will:
        A. Generate matrix A and B
    before running the algorithm it will check if they are
        1. not empty
        2. same length
    The matrices size will be stated in the code and can be changed from int to float and vice versa

    generating matrices I found on numpy.random.uniform.html 
    on Numpy.org website it explains how I could randomly generating numbers

    code for algorithm I found on geeksforgeeks 
    but I changed part of it to work with matrices I generated compared to their examples


"""

import random               # Import the random module to generate random numbers.
import numpy as np          # Import the numpy module to read .csv file that contains the

# Function to generate a matrix with random values
def generate_matrix(rows, cols):
    """
    This function "generate_matrix" generates the matrices.
    There are two lines that are identical but only onething is different.
    For generating integer matrix we use randint from random module
    For generating float matrix we use uniform from random module

    the function have two parameters (rows, cols)
    when given the an argument of e.g (1000,1000) it will generate matrix 1000x1000

    by default I turned one of the lines off so it doesn't produce error.
    all you need to switch from generating int to float or vice versa is switchting which line is a comment
    
    """
   # generate float between 0 and 10
    return [[random.uniform(0, 10) for _ in range(cols)] for _ in range(rows)] # Fill it with random float numbers between 0 and 10.

    # generate integer between 0 and 10
    #return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)] # Fill it with random integers between 1 and 10.

# Function to multiply two matrices
def multiply_matrices(A, B):
    """
    This function is performing recursion on two arguments that is given to it(A,B)

    first it check whether the input matrices are empty or have no rows/columns
    it does this by checking 4 conditions
    len(A) == 0 or len(A[0]) == 0 or len(B) == 0 or len(B[0]) == 0
    if any condition is true it will return "input the matrices are empty" 
    It would be uncessary to run the function if any of my inputs were empty as originally I
    tested with .csv file rather than generating within the code

    Second thing it will check if the matrices length are identical
    len(A[0]) != len(B) <-- this is the condition code
    if they are not equal it will return "Matrix dimensions are not compatible for multiplication."

    Third step is to generate a vessel to hold the result
    it will do this be generating a zeros based on length of A/B matrices

    4th step is to perform recursion algorithm on the matrices to multiply and get the result
    

    """
    # Check if input matrices are empty or have no rows/columns.
    if len(A) == 0 or len(A[0]) == 0 or len(B) == 0 or len(B[0]) == 0:
        return "Input matrices are empty."
    
    # Check if matrix dimensions are compatible for multiplication.
    if len(A[0]) != len(B):
        return "Matrix dimensions are not compatible for multiplication."
    
    # Initialize a result matrix with zeros.
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Perform matrix multiplication using three nested loops.
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                # Multiply corresponding elements of matrices A and B and
                # accumulate the result in the corresponding position in the result matrix.
                result[i][j] += A[i][k] * B[k][j]
    
    return result


"""
    Initically I wanted to run the code on .csv file however, after testing the time of generating matrices within the code 
    I found that generating matrices then performing the algorithm is much faster 
    Hence why below there are couple lines using numpy to import  the .csv file
    in essence you don't need Numpy for this code unless you are using a stored matrices
"""

#matrix_A = np.genfromtxt("project1/int/int1000x1000A.csv", delimiter=";")
#matrix_B = np.genfromtxt("project1/int/int1000x1000B.csv", delimiter=";")
# ran into issue of no result at size 1000x1000^2 so i thought generating would solve it. it didn't

# Generate two random 1000x1000 matrices
matrix_A = generate_matrix(1000, 1000)
matrix_B = generate_matrix(1000, 1000)

# Multiply the matrices
result_matrix = multiply_matrices(matrix_A, matrix_B)

# Printing a sample element from the result matrix (like element at row 0, col 0)
#print("Result:", result_matrix[0][0]) 

# Printing the entire result matrix
print(result_matrix)


