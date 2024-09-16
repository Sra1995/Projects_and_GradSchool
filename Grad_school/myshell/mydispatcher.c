/*
CSC521 Operating Systems 
Project #2: – Short Term Scheduling
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 03/11/2024
Date modified: 03/27/2024
*/
#include <stdio.h>                                                                                  // Include the standard input/output library
#include <stdlib.h>                                                                                 // Include the standard library
#include "utils.h"                                                                                  // Include the utils header file
#include "algorithms.h"                                                                             // Include the algorithms header file
#include <string.h>                                                                                 // Include the string library

int main(int argc, char *argv[]) {                                                                  // Main function with command line arguments
    if (argc != 3 && argc != 4) {                                                                   // Check if the number of arguments is not 3 or 4
        printf("Usage: %s <input.dat> <scheduling_policy> [<quantum_size>]\n", argv[0]);            // Print the usage message
        exit(EXIT_FAILURE);                                                                         // Exit the program with failure status
    }

    char *inputFile = argv[1];                                                                      // Get the input file name from command line argument
    char *schedulingPolicy = argv[2];                                                               // Get the scheduling policy from command line argument
    int quantumSize = -1;                                                                           // Default quantum size

                                                                                                    // If RR is selected, check if a quantum size is provided
    if (argc == 4 && strcmp(schedulingPolicy, "RR") == 0) {                                         // Check if the scheduling policy is RR and a quantum size is provided
        quantumSize = atoi(argv[3]);                                                                // Convert the quantum size from string to integer
        if (quantumSize <= 0) {                                                                     // Check if the quantum size is not positive
            printf("Quantum size must be a positive integer.\n");                                   // Print an error message
            exit(EXIT_FAILURE);                                                                     // Exit the program with failure status
        }
    }

                                                                                                    // Read processes from input file
    Process *processes;                                                                             // Declare a pointer to Process structure
    int numProcesses = readProcessesFromFile(inputFile, &processes);                                // Read processes from input file and get the number of processes

                                                                                                    // Choose and execute scheduling algorithm
    if (strcmp(schedulingPolicy, "FCFS") == 0) {                                                    // Check if the scheduling policy is FCFS
        fcfs(processes, numProcesses);                                                              // Execute the FCFS scheduling algorithm
    } else if (strcmp(schedulingPolicy, "RR") == 0) {                                               // Check if the scheduling policy is RR
        rr(processes, numProcesses, quantumSize);                                                   // Execute the RR scheduling algorithm
    } else if (strcmp(schedulingPolicy, "SPN") == 0) {                                              // Check if the scheduling policy is SPN
        spn(processes, numProcesses);                                                               // Execute the SPN scheduling algorithm
    } else if (strcmp(schedulingPolicy, "SRT") == 0) {                                              // Check if the scheduling policy is SRT
        srt(processes, numProcesses);                                                               // Execute the SRT scheduling algorithm
    } else {
        printf("Invalid scheduling policy. Use one of FCFS, RR, SPN, or SRT.\n");                   // Print an error message
        exit(EXIT_FAILURE);                                                                         // Exit the program with failure status
    }

                                                                                                    // Calculate and display global averages
    calculateAndDisplayAverages(processes, numProcesses);                                           // Calculate and display the global averages

                                                                                                    // Clean up allocated memory
    free(processes);                                                                                // Free the allocated memory for processes

    return 0;                                                                                       // Return 0 to indicate successful program execution
}
