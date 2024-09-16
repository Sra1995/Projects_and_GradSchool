import numpy as np                                                                                  # Importing numpy library for numerical calculations
from math import gcd                                                                                # Importing gcd function from math library for finding greatest common divisor

                                                                                                    # Function to perform modular exponentiation
def mod_exp(base, exponent, modulus):                                                               # takes 3 arguments: base, exponent and modulus
    result = 1                                                                                      # Initialize result as 1 so that we can multiply it with base
    for _ in range(exponent):                                                                       # Loop to multiply base with result exponent times
        result = (result * base) % modulus                                                          # Multiply base with result and take modulus with respect to modulus
    return result                                                                                   # Function to perform modular exponentiation

                                                                                                    # Function to find the period using classical approach
def find_period(a, N):                                                                              # takes 2 arguments: a and N
    x = 1                                                                                           # Initialize x as 1
    results = []                                                                                    # List to store the results of a^x mod N
    while True:                                                                                     # Loop infinitly to find the period
        result = mod_exp(a, x, N)                                                                   # Calculate a^x mod N
        print(f"{a}^{x} mod {N} = {result}")                                                        # Print the result of a^x mod N for each x so that we can see the pattern
        if result in results:                                                                       # Check if the result is already in the list
            break                                                                                   # If the result is already in the list, then we have found the period
        results.append(result)                                                                      # Append the result to the list
        x += 1                                                                                      # Increment x by 1
    print(f"Period found: {x - 1}")                                                                 # Print the period found
    return x - 1                                                                                    # Function to find the period using classical approach

                                                                                                    # Function to factorize the number using the period found
def shors_algorithm(N, a):                                                                          # takes 2 arguments: N and a
    print(f"\nRunning Shor's algorithm for N = {N} and a = {a}")                                    # Print the values of N and a
    
                                                                                                    # Step 1: Find the period of the function
    period = find_period(a, N)                                                                      # Find the period of the function using classical approach and store it in period variable
    
    if period % 2 != 0:                                                                             # Check if the period is odd
        print(f"Period {period} is odd. Cannot proceed.")                                           # If the period is odd, then we cannot proceed
        return None, None                                                                           # Return None, None if the period is odd so that we can try with different a value

    print(f"Period (r) is {period}. Proceeding with finding factors.")                              # Print the period found and proceed with finding the factors

                                                                                                    # Step 2: Compute the potential factors
    exp_half_period = mod_exp(a, period // 2, N)                                                    # Compute a^(r/2) mod N part of the algorithm
    factor1 = gcd(exp_half_period - 1, N)                                                           # Compute gcd(a^(r/2) - 1, N) part of the algorithm
    factor2 = gcd(exp_half_period + 1, N)                                                           # Compute gcd(a^(r/2) + 1, N) part of the algorithm

    print(f"Computed values: a^(r/2) mod N = {exp_half_period}")                                    # Print the computed values for a^(r/2) mod N
    print(f"gcd(a^(r/2) - 1, N) = gcd({exp_half_period} - 1, {N}) = {factor1}")                     # Print the computed values for first factor
    print(f"gcd(a^(r/2) + 1, N) = gcd({exp_half_period} + 1, {N}) = {factor2}")                     # Print the computed values for second factor

                                                                                                    # Check if the factors are trivial
    if factor1 == 1 or factor1 == N:                                                                # if factor1 is 1 or N, then it is trivial
        print(f"Factor {factor1} is trivial. Cannot use.")                                          # Print that factor1 is trivial
        return None, None                                                                           # Return None, None if factor1 is trivial so that we can try with different a value
    if factor2 == 1 or factor2 == N:                                                                # if factor2 is 1 or N, then it is trivial
        print(f"Factor {factor2} is trivial. Cannot use.")                                          # Print that factor2 is trivial
        return None, None                                                                           # Return None, None if factor2 is trivial so that we can try with different a value

    return factor1, factor2                                                                         # Return the factors found


N = 77                                                                                              # Number to be factored

                                                                                                    # List of potential a values to try
a_values = [2, 3, 5, 7, 10]

                                                                                                    # Run Shor's algorithm with multiple values of a to see if we can find the factors
for a in a_values:                                                                                  # Loop to try different a values
    factor1, factor2 = shors_algorithm(N, a)                                                        # Run Shor's algorithm with the given N and a values
    if factor1 and factor2:                                                                         # Check if the factors are found
        print(f"\nThe factors of {N} using a={a} are {factor1} and {factor2}.")                     # Print the factors found
                                                                                                    # Additional check to ensure the factors are correct
        if factor1 * factor2 == N:                                                                  # Check if the factors are correct like if 77 = 7 * 11 in this case
            print(f"Verification: {factor1} * {factor2} = {N}")                                     # Print the verification of the factors
        else:                                                                                       # If the factors are not correct
            print("The factors found are not correct.")                                             # Print that the factors found are not correct
        break                                                                                       # Break the loop if factors are not trivial
else:                                                                                               # If the loop completes without finding the factors
    print(f"\nFailed to find non-trivial factors for {N} using the given a values.")                # Print that the factors are not found
