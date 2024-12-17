#include <iostream>                                                                             // standard input/output stream objects
#include <vector>                                                                               // vector library for dynamic arrays
#include <ctime>                                                                                // time library for time functions

using namespace std;

int serial_binary_search(const vector<int>& arr, int target) {                                  // function to perform serial binary search
    int low = 0, high = arr.size() - 1;                                                         // init low and high values variables
    while (low <= high) {                                                                       // while loop to iterate through the array to find the target
        int mid = low + (high - low) / 2;                                                       // calculate the mid value
        if (arr[mid] == target) return mid;                                                     // if the mid value is equal to the target return the mid value
        if (arr[mid] < target) low = mid + 1;                                                   // if the mid value is less than the target set the low value to mid + 1
        else high = mid - 1;                                                                    // if the mid value is greater than the target set the high value to mid - 1
    }
    return -1;                                                                                  // Target not found
}

int main() {                                                                                    // main function for the program
                                                                                                // Create sorted list of 2^20 items
    const int n = 1 << 20;                                                                      // a constant int n with value 2^20
    vector<int> sorted_list(n);                                                                 // a vector of int with size n
    for (int i = 0; i < n; ++i) {                                                               // for loop to iterate through the vector
        sorted_list[i] = i;                                                                     // set the value of the vector at index i to i
    }

                                                                                                // Search 2000 random items
    srand(time(0));                                                                             // Seed for randomness
    int found = 0;                                                                              // variable to store the number of items found
    clock_t start = clock();                                                                    // Start the clock to measure the duration of the search
    for (int i = 0; i < 2000; ++i) {                                                            // for loop to iterate through 2000 random items
        int target = rand() % n;                                                                // Generate a random target
        if (serial_binary_search(sorted_list, target) != -1) {                                  // Perform binary search and check if the target is found
            found++;                                                                            // Increment the found count
        }
    }
    clock_t end = clock();                                                                      // End the clock once the search is completed
    double duration = double(end - start) / CLOCKS_PER_SEC;                                     // Calculate the duration of the search
    cout << "Serial search completed in " << duration << " seconds." << endl;                   // Output the duration of the search
}