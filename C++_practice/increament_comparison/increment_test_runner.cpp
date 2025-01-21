#include <iostream>
#include <chrono>
#include <vector>
#include <numeric>
#include <cmath>
#include "increment_timer.cpp" // Include the file with increment functions

// Function to calculate the average of a vector of times
double calculate_average(const std::vector<long long>& times) {
    return static_cast<double>(std::accumulate(times.begin(), times.end(), 0LL)) / times.size();
}

// Function to calculate the standard deviation of a vector of times
double calculate_stdev(const std::vector<long long>& times, double average) {
    double sum = 0.0;
    for (const auto& time : times) {
        sum += (time - average) * (time - average);
    }
    return std::sqrt(sum / times.size());
}

int main() {
    const int n = 1000000000; // Number of increments
    const int runs = 10000; // Number of times to repeat each test

    // Vectors to store times for each test
    std::vector<long long> postfix_while_times;
    std::vector<long long> prefix_while_times;
    std::vector<long long> postfix_for_times;
    std::vector<long long> prefix_for_times;

    for (int i = 0; i < runs; ++i) {
        // Measure postfix increment with while loop
        auto start = std::chrono::high_resolution_clock::now();
        basic_increment_postfix(n);
        auto end = std::chrono::high_resolution_clock::now();
        postfix_while_times.push_back(std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count());

        // Measure prefix increment with while loop
        start = std::chrono::high_resolution_clock::now();
        basic_increment_prefix(n);
        end = std::chrono::high_resolution_clock::now();
        prefix_while_times.push_back(std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count());

        // Measure postfix increment with for loop
        start = std::chrono::high_resolution_clock::now();
        basic_increment_postfix_for(n);
        end = std::chrono::high_resolution_clock::now();
        postfix_for_times.push_back(std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count());

        // Measure prefix increment with for loop
        start = std::chrono::high_resolution_clock::now();
        basic_increment_prefix_for(n);
        end = std::chrono::high_resolution_clock::now();
        prefix_for_times.push_back(std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count());
    }

    // Calculate statistics for each test
    double postfix_while_avg = calculate_average(postfix_while_times);
    double prefix_while_avg = calculate_average(prefix_while_times);
    double postfix_for_avg = calculate_average(postfix_for_times);
    double prefix_for_avg = calculate_average(prefix_for_times);

    double postfix_while_stdev = calculate_stdev(postfix_while_times, postfix_while_avg);
    double prefix_while_stdev = calculate_stdev(prefix_while_times, prefix_while_avg);
    double postfix_for_stdev = calculate_stdev(postfix_for_times, postfix_for_avg);
    double prefix_for_stdev = calculate_stdev(prefix_for_times, prefix_for_avg);

    // Output the results
    std::cout << "Performance Statistics for Increment Tests (" << runs << " runs):\n";

    std::cout << "\nPostfix Increment (while loop):\n";
    std::cout << "Average time: " << postfix_while_avg << " ns\n";
    std::cout << "Standard deviation: " << postfix_while_stdev << " ns\n";

    std::cout << "\nPrefix Increment (while loop):\n";
    std::cout << "Average time: " << prefix_while_avg << " ns\n";
    std::cout << "Standard deviation: " << prefix_while_stdev << " ns\n";

    std::cout << "\nPostfix Increment (for loop):\n";
    std::cout << "Average time: " << postfix_for_avg << " ns\n";
    std::cout << "Standard deviation: " << postfix_for_stdev << " ns\n";

    std::cout << "\nPrefix Increment (for loop):\n";
    std::cout << "Average time: " << prefix_for_avg << " ns\n";
    std::cout << "Standard deviation: " << prefix_for_stdev << " ns\n";

    return 0;
}
