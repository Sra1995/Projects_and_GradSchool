/*
CSC521 Operating Systems 
Project #2: – Short Term Scheduling
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 03/11/2024
Date modified: 03/27/2024
*/

#ifndef UTILS_H                                                // Include guard to prevent multiple inclusion of the header file
#define UTILS_H

#define min(a, b) ((a) < (b) ? (a) : (b))                       // Macro to find the minimum of two values

typedef struct {                                               // Definition of the Process structure
    int arrivalTime;                                           // Arrival time of the process
    int serviceTime;                                           // Service time of the process
    int finishTime;                                            // Finish time of the process
    int turnaroundTime;                                        // Turnaround time of the process
    int waitingTime;                                           // Waiting time of the process
    int remainingTime;                                         // Remaining time of the process
    int startTime;                                             // Start time of the process
} Process;

typedef struct {                                               // Definition of the ProcessNode structure
    Process *process;                                          // Pointer to a Process structure
    int remainingTime;                                         // Remaining time of the process
} ProcessNode;

int readProcessesFromFile(const char *filename, Process **processes);  // Function prototype to read processes from a file

#endif
