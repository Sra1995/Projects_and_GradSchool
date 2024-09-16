"""
    This file runs Nested Loop algorithm on two generated matrices.
    before checking the matrices it will:
        A. Generate matrix A and B
    before running the algorithm it will check if they are
        1. same length
    The matrices size will be stated in the code and can be changed from int to float and vice versa

    generating matrices I found on numpy.random.uniform.html 
    on Numpy.org website it explains how I could randomly generating numbers

    code for algorithm I found on geeksforgeeks 
    but I changed part of it to work with matrices I generated compared to their examples


"""

import numpy as np
import random

# Function to generate a matrix with random float values between 0 and 10
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
    
    # Generate Floats between 0 and 10
    #return [[random.uniform(0, 10) for _ in range(cols)] for _ in range(rows)]

    # Generate integers between 0 and 10
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]


def matrix_multiply_nested(mat1, mat2):
    """
    This function is performing Nested Loop algorithm on two arguments that is given to it(A,B)

    first step it will check if the matrices length are identical
    len(A[0]) != len(B) <-- this is the condition code
    if they are not equal it will return "Matrix dimensions are not compatible for multiplication."

    Second step is to generate a vessel to hold the result
    it will do this be generating a zeros based on length of A/B matrices

    3rd step is to perform Nested Loop algorithm on the matrices to multiply and return the result into the vessel we
    created earlier called "result"
    

    """
    # Check if the dimensions are compatible for multiplication
    if len(mat1[0]) != len(mat2):
        raise ValueError("Matrix dimensions are not compatible for multiplication.")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    # Iterate through rows of mat1
    for i in range(len(mat1)):
        # Iterate through columns of mat2
        for j in range(len(mat2[0])):
            # Iterate through elements of mat2 (or rows of mat1)
            for k in range(len(mat2)):
                # Multiply corresponding elements and accumulate the result
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result


"""
    Initically I wanted to run the code on .csv file however, after testing the time of generating matrices within the code 
    I found that generating matrices then performing the algorithm is much faster 
    Hence why below there are couple lines using numpy to import  the .csv file
    in essence you don't need Numpy for this code unless you are using a stored matrices
"""
# Import matrices from CSV files (replace file paths as needed)
#matrix1 = np.genfromtxt("project1/int/int1000x1000A.csv", delimiter=";")
#matrix2 = np.genfromtxt("project1/int/int1000x1000B.csv", delimiter=";")


matrix1 = generate_matrix(1000, 1000)
matrix2 = generate_matrix(1000, 1000)

# Perform matrix multiplication
result = matrix_multiply_nested(matrix1, matrix2)

# Printing the entire result matrix
print(result)
