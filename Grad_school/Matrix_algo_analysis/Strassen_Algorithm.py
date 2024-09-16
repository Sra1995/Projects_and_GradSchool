"""
    This file runs Strassen algorithm on two generated matrices.
    before checking the matrices it will:
        A. Generate matrix A and B
    before running the algorithm it will check if they are
        1. same length
        2. if matrice size is very small it will padd it
    The matrices size will be stated in the code and can be changed from int to float and vice versa

    generating matrices I found on numpy.random.uniform.html 
    on Numpy.org website it explains how I could randomly generating numbers

    code for algorithm I found on geeksforgeeks 
    but I changed part of it to work with matrices I generated compared to their examples


"""

import numpy as np          # Import the numpy module to read .csv file that contains the
import random               # Import the random module to generate random numbers.

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

    some debugging found on stackoverflow(padding)
    
    """
    # generate float numbers between 0 and 10.
    return [[random.uniform(0, 10) for _ in range(cols)] for _ in range(rows)]

    # generate integers between 1 and 10.
    #return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

def matrix_multiply_strassen(mat1, mat2):
    """
    This function is to perform Strassen alogirthm to multiply two matrices

    Step one: 
    check if length of first matrix is equal to matrix 2

    Step two:
    padd the matrix if the size is very small( I ran into issue of incorrect multiplication but this fixed it)

    step 3:
    perform strassen algorithm
        A. split the size into two piece get a11,a12.. etc and b11,b12,.. etc
        B. Get all 7 Ps 
        C. compute c11,c12 .. etc
        D. glue the answers together
        E. return the result matrix called result with same size as matrix A&B

    """
    # Check if the dimensions are compatible for multiplication
    if len(mat1[0]) != len(mat2):
        raise ValueError("Matrix dimensions are not compatible for multiplication.")
    
    # Padding to ensure dimensions are powers of 2
    size = max(len(mat1), len(mat2), len(mat1[0]), len(mat2[0]))
    size = 2 ** (size - 1).bit_length()
    
    # Pad the matrices with zeros
    mat1_padded = np.pad(mat1, ((0, size - len(mat1)), (0, size - len(mat1[0]))), mode='constant')
    mat2_padded = np.pad(mat2, ((0, size - len(mat2)), (0, size - len(mat2[0]))), mode='constant')
    
    # If the matrices are small, use a simple method (e.g., numpy.dot)
    if size <= 64:
        return np.dot(mat1_padded, mat2_padded)
    else:
        # Divide the matrices into submatrices
        mid = size // 2
        a11 = mat1_padded[:mid, :mid]
        a12 = mat1_padded[:mid, mid:]
        a21 = mat1_padded[mid:, :mid]
        a22 = mat1_padded[mid:, mid:]
        
        b11 = mat2_padded[:mid, :mid]
        b12 = mat2_padded[:mid, mid:]
        b21 = mat2_padded[mid:, :mid]
        b22 = mat2_padded[mid:, mid:]
        
        # Recursive calls for the submatrices
        p1 = matrix_multiply_strassen(a11 + a22, b11 + b22)
        p2 = matrix_multiply_strassen(a21 + a22, b11)
        p3 = matrix_multiply_strassen(a11, b12 - b22)
        p4 = matrix_multiply_strassen(a22, -b11 + b21)
        p5 = matrix_multiply_strassen(a11 + a12, b22)
        p6 = matrix_multiply_strassen(-a21 + a11, b11 + b12)
        p7 = matrix_multiply_strassen(a12 - a22, b21 + b22)
        
        # Compute submatrices of the result
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 - p2 + p3 + p6
        
        # Combine submatrices to get the result
        result = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
        
        return result[:len(mat1), :len(mat2[0])]

# Import matrices from CSV files (replace file paths within double quotes as needed)
#matrix1 = np.genfromtxt("project1/int/int1000x1000A.csv", delimiter=";")
#matrix2 = np.genfromtxt("project1/int/int1000x1000B.csv", delimiter=";")

matrix1 = generate_matrix(1000, 1000)
matrix2 = generate_matrix(1000, 1000)

# Perform matrix multiplication
result = matrix_multiply_strassen(matrix1, matrix2)
print(result)
