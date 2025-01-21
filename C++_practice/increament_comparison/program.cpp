#include <iostream>
#include <chrono>

// Function to increment a variable using postfix increment (i++) in a while loop
// This function measures the time it takes to perform the increment operation n times
void basic_increment_postfix(int n) {
    // Start the timer using high-resolution clock for precise timing
    auto start = std::chrono::high_resolution_clock::now();

    int i = 0; // Initialize the counter variable
    while (i < n) {
        i++; // Increment the variable using postfix syntax
    }

    // Stop the timer after the loop completes
    auto end = std::chrono::high_resolution_clock::now();
    // Calculate the duration in nanoseconds
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

    // Output the results: final value of i and time taken
    std::cout << "Postfix Increment (i++):\n";
    std::cout << "Final value: " << i << "\n";
    std::cout << "Time taken: " << duration.count() << " nanoseconds\n";
}

// Function to increment a variable using prefix increment (++i) in a while loop
// This function measures the time it takes to perform the increment operation n times
void basic_increment_prefix(int n) {
    // Start the timer using high-resolution clock for precise timing
    auto start = std::chrono::high_resolution_clock::now();

    int i = 0; // Initialize the counter variable
    while (i < n) {
        ++i; // Increment the variable using prefix syntax
    }

    // Stop the timer after the loop completes
    auto end = std::chrono::high_resolution_clock::now();
    // Calculate the duration in nanoseconds
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

    // Output the results: final value of i and time taken
    std::cout << "Prefix Increment (++i):\n";
    std::cout << "Final value: " << i << "\n";
    std::cout << "Time taken: " << duration.count() << " nanoseconds\n";
}

// Function to increment a variable using postfix increment (i++) in a for loop
// This function measures the time it takes to perform the increment operation n times
void basic_increment_postfix_for(int n) {
    // Start the timer using high-resolution clock for precise timing
    auto start = std::chrono::high_resolution_clock::now();

    int i = 0; // Initialize the counter variable
    for (i = 0; i < n; i++) {
        // Postfix increment happens as part of the loop
    }

    // Stop the timer after the loop completes
    auto end = std::chrono::high_resolution_clock::now();
    // Calculate the duration in nanoseconds
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

    // Output the results: final value of i and time taken
    std::cout << "Postfix Increment with for loop (i++):\n";
    std::cout << "Final value: " << i << "\n";
    std::cout << "Time taken: " << duration.count() << " nanoseconds\n";
}

// Function to increment a variable using prefix increment (++i) in a for loop
// This function measures the time it takes to perform the increment operation n times
void basic_increment_prefix_for(int n) {
    // Start the timer using high-resolution clock for precise timing
    auto start = std::chrono::high_resolution_clock::now();

    int i = 0; // Initialize the counter variable
    for (i = 0; i < n; ++i) {
        // Prefix increment happens as part of the loop
    }

    // Stop the timer after the loop completes
    auto end = std::chrono::high_resolution_clock::now();
    // Calculate the duration in nanoseconds
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

    // Output the results: final value of i and time taken
    std::cout << "Prefix Increment with for loop (++i):\n";
    std::cout << "Final value: " << i << "\n";
    std::cout << "Time taken: " << duration.count() << " nanoseconds\n";
}

// Main function: Entry point of the program
int main() {
    int n = 1000000000; // Hardcoded value for the number of increments

    std::cout << "Starting with n = " << n << "\n\n"; // Display initial message

    // Call the function to measure postfix increment performance using while loop
    basic_increment_postfix(n);
    std::cout << "\n"; // Separate the outputs for clarity

    // Call the function to measure prefix increment performance using while loop
    basic_increment_prefix(n);
    std::cout << "\n"; // Separate the outputs for clarity

    // Call the function to measure postfix increment performance using for loop
    basic_increment_postfix_for(n);
    std::cout << "\n"; // Separate the outputs for clarity

    // Call the function to measure prefix increment performance using for loop
    basic_increment_prefix_for(n);

    return 0; // Indicate successful program termination - alanturing
}
