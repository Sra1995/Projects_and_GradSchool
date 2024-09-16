/*
CSC521 Operating Systems 
Project #2: – Short Term Scheduling
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 03/11/2024
Date modified: 03/27/2024
*/

#include "algorithms.h"                                                                             // Include the header file for algorithms
#include <stdio.h>                                                                                  // Include the standard input/output library
#include <stdlib.h>                                                                                 // Include the standard library
#include <limits.h>                                                                                 // Include the limits library for INT_MAX

void fcfs(Process *processes, int numProcesses) {                                                   // First Come First Serve
    FILE *outputFile = fopen("output.dat", "w");                                                    // Open the output file for writing
    if (!outputFile) {                                                                              // Check if the output file is not opened
        perror("Error opening output file");                                                        // Print an error message
        exit(EXIT_FAILURE);                                                                         // Exit the program with failure status
    }

    int currentTime = 0;                                                                            // Initialize the current time to 0

    for (int i = 0; i < numProcesses; i++) {                                                        // Loop through all processes
        processes[i].startTime = currentTime;                                                       // Set the start time of the process to the current time

                                                                                                    // Update process details
        processes[i].finishTime = currentTime + processes[i].serviceTime;                           // Calculate the finish time of the process
        processes[i].waitingTime = currentTime - processes[i].arrivalTime;                          // Calculate the waiting time of the process
        processes[i].turnaroundTime = processes[i].waitingTime + processes[i].serviceTime;          // Calculate the turnaround time of the process

        if (processes[i].waitingTime < 0) {
                                                                                                    // If waiting time becomes negative, set it to 0
            processes[i].waitingTime = 0;
        }

        if (processes[i].turnaroundTime < 0) {
                                                                                                    // If turnaround time becomes negative, set it to service time
            processes[i].turnaroundTime = processes[i].serviceTime;
        }

                                                                                                    // Print process details to output file
        fprintf(outputFile, "%d runs %d-%d: A=%d, S=%d, W=%d, F=%d, T=%d\n",
                i + 1, processes[i].startTime, processes[i].finishTime,
                processes[i].arrivalTime, processes[i].serviceTime,
                processes[i].waitingTime, processes[i].finishTime, processes[i].turnaroundTime);

                                                                                                    // Update current time for the next process
        currentTime = processes[i].finishTime;                                                      // set the current time to the finish time of the process
    }

    fclose(outputFile);                                                                             // Close the output file
}

void rr(Process *processes, int numProcesses, int quantumSize) {                                    // Round Robin
    FILE *outputFile = fopen("output.dat", "w");                                                    // Open the output file for writing
    if (!outputFile) {                                                                              // Check if the output file is not opened
        perror("Error opening output file");                                                        // Print an error message
        exit(EXIT_FAILURE);                                                                         // Exit the program with failure status
    }

    int currentTime = 0;                                                                            // Initialize the current time to 0

    for (int i = 0; i < numProcesses; i++) {                                                        // Loop through all processes
        processes[i].startTime = currentTime;                                                       // Set the start time of the process to the current time


        int remainingTime = processes[i].serviceTime;                                               // Calculate remaining time for the process

                                                                                                    // Execute the process until it finishes or quantum expires
        while (remainingTime > 0) {
            int executionTime = (remainingTime > quantumSize) ? quantumSize : remainingTime;

                                                                                                    // Update process details
            processes[i].finishTime = currentTime + executionTime;                                  // Calculate the finish time of the process
            processes[i].waitingTime += currentTime - processes[i].arrivalTime;                     // Accumulate waiting time
            processes[i].turnaroundTime = processes[i].waitingTime + processes[i].serviceTime;      // Calculate the turnaround time of the process

                                                                                                    // Print process details to output file
            fprintf(outputFile, "%d runs %d-%d: A=%d, S=%d, W=%d, F=%d, T=%d\n",
                    i + 1, processes[i].startTime, processes[i].finishTime,
                    processes[i].arrivalTime, processes[i].serviceTime,
                    processes[i].waitingTime, processes[i].finishTime, processes[i].turnaroundTime);

                                                                                                    // Update remaining time for the process
            remainingTime -= executionTime;

                                                                                                    // Update current time for the next process
            currentTime = processes[i].finishTime;
        }
    }

    fclose(outputFile);                                                                             // Close the output file
}

void spn(Process *processes, int numProcesses) {                                                    // Shortest Process Next(SPN)
    FILE *outputFile = fopen("output.dat", "w");                                                    // Open the output file for writing
    if (!outputFile) {                                                                              // Check if the output file is not opened
        perror("Error opening output file");                                                        // Print an error message
        exit(EXIT_FAILURE);                                                                         // Exit the program with failure status
    }

    int currentTime = 0;                                                                            // Initialize the current time to 0

    for (int i = 0; i < numProcesses; i++) {                                                        // Loop through all processes
        processes[i].startTime = currentTime;                                                       // Set the start time of the process to the current time

                                                                                                    // Update process details
        processes[i].finishTime = currentTime + processes[i].serviceTime;                           // Calculate the finish time of the process
        processes[i].waitingTime = currentTime - processes[i].arrivalTime;                          // Calculate the waiting time of the process
        processes[i].turnaroundTime = processes[i].waitingTime + processes[i].serviceTime;          // Calculate the turnaround time of the process

        if (processes[i].waitingTime < 0) {
                                                                                                    // If waiting time becomes negative, set it to 0
            processes[i].waitingTime = 0;
        }

        if (processes[i].turnaroundTime < 0) {
                                                                                                    // If turnaround time becomes negative, set it to service time
            processes[i].turnaroundTime = processes[i].serviceTime;
        }

                                                                                                    // Print process details to output file
        fprintf(outputFile, "%d runs %d-%d: A=%d, S=%d, W=%d, F=%d, T=%d\n",
                i + 1, processes[i].startTime, processes[i].finishTime,
                processes[i].arrivalTime, processes[i].serviceTime,
                processes[i].waitingTime, processes[i].finishTime, processes[i].turnaroundTime);

                                                                                                    // Update current time for the next process
        currentTime = processes[i].finishTime;
    }

    fclose(outputFile);                                                                             // Close the output file
}

void srt(Process *processes, int numProcesses) {                                                    // Shortest Remaining Time(SRT)
    FILE *outputFile = fopen("output.dat", "w");                                                    // Open the output file for writing
    if (!outputFile) {                                                                              // Check if the output file is not opened
        perror("Error opening output file");                                                        // Print an error message
        exit(EXIT_FAILURE);                                                                         // Exit the program with failure status
    }

                                                                                                    // Initialize remainingTime for each process
    for (int i = 0; i < numProcesses; i++) {
        processes[i].remainingTime = processes[i].serviceTime;
    }

    int currentTime = 0;                                                                            // Initialize the current time to 0
    int completedProcesses = 0;                                                                     // Initialize the number of completed processes to 0

    while (completedProcesses < numProcesses) {                                                     // Loop until all processes are completed
        int shortestIndex = -1;                                                                     // Initialize the index of the shortest process to -1
        int shortestRemainingTime = INT_MAX;                                                        // Initialize the shortest remaining time to the maximum integer value

                                                                                                    // Find the process with the shortest remaining time
        for (int i = 0; i < numProcesses; i++) {
            if (processes[i].arrivalTime <= currentTime && processes[i].remainingTime > 0) {        // Check if the process has arrived and has remaining time
                if (processes[i].remainingTime < shortestRemainingTime) {
                    shortestIndex = i;                                                              // Set the index of the shortest process to the current index
                    shortestRemainingTime = processes[i].remainingTime;                             // Set the shortest remaining time to the remaining time of the current process
                }
            }
        }

        if (shortestIndex == -1) {                                                                  // Check if no process is found
            currentTime++;                                                                          // Increment the current time
            continue;                                                                               // Continue to the next iteration
        }

        Process *shortestProcess = &processes[shortestIndex];                                       // Get the shortest process

                                                                                                    // Update waiting time for processes that haven't started yet
        for (int i = 0; i < numProcesses; i++) {
            if (i != shortestIndex && processes[i].arrivalTime <= currentTime && processes[i].remainingTime > 0) {  // Check if the process has arrived and has remaining time
                processes[i].waitingTime++;                                                         // Increment the waiting time of the process
            }
        }

                                                                                                    // Execute the shortest process for one unit of time
        shortestProcess->startTime = currentTime;                                                   // Set the start time of the process to the current time
        shortestProcess->remainingTime--;                                                           // Decrement the remaining time of the process
        currentTime++;                                                                              // Increment the current time

        if (shortestProcess->remainingTime == 0) {                                                  // Check if the process has finished
                                                                                                    // Process completed
            shortestProcess->finishTime = currentTime;                                              // Set the finish time of the process to the current time
            shortestProcess->turnaroundTime = shortestProcess->finishTime - shortestProcess->arrivalTime;   // Calculate the turnaround time of the process
            shortestProcess->waitingTime = shortestProcess->turnaroundTime - shortestProcess->serviceTime;  // Calculate the waiting time of the process
            completedProcesses++;                                                                   // Increment the number of completed processes

                                                                                                    // Print process details to output file
            fprintf(outputFile, "%d runs %d-%d: A=%d, S=%d, W=%d, F=%d, T=%d\n",
                    shortestIndex + 1, shortestProcess->startTime, shortestProcess->finishTime,
                    shortestProcess->arrivalTime, shortestProcess->serviceTime,
                    shortestProcess->waitingTime, shortestProcess->finishTime, shortestProcess->turnaroundTime);
        }
    }

    fclose(outputFile);                                                                             // Close the output file
}





void calculateAndDisplayAverages(Process *processes, int numProcesses) {                            // Calculate and display global averages
                                                                                                    // Calculate and display global averages
    int totalTurnaroundTime = 0;                                                                    // Initialize the total turnaround time to 0
    int totalWaitingTime = 0;                                                                       // Initialize the total waiting time to 0

    for (int i = 0; i < numProcesses; i++) {                                                        // Loop through all processes
        totalTurnaroundTime += processes[i].turnaroundTime;                                         // Accumulate the turnaround time
        totalWaitingTime += processes[i].waitingTime;                                               // Accumulate the waiting time
    }

    double avgTurnaroundTime = (double)totalTurnaroundTime / numProcesses;                          // Calculate the average turnaround time
    double avgNormalizedTurnaroundTime = (double)totalTurnaroundTime / numProcesses;                // Calculate the average normalized turnaround time
    double avgWaitingTime = (double)totalWaitingTime / numProcesses;                                // Calculate the average waiting time

    printf("Average turnaround time = %.2f\n", avgTurnaroundTime);                                  // Print the average turnaround time
    printf("Average normalized turnaround time = %.2f\n", avgNormalizedTurnaroundTime);             // Print the average normalized turnaround time
    printf("Average waiting time = %.2f\n", avgWaitingTime);                                        // Print the average waiting time
}

