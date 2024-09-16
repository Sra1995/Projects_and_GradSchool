/*
CSC521 Operating Systems 
Project #2: – Short Term Scheduling
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 03/11/2024
Date modified: 03/27/2024
*/
#ifndef ALGORITHMS_H                                                                // Include guard
#define ALGORITHMS_H                                                                // Include guard

#include "utils.h"                                                                  // Include utils.h for Process struct

void fcfs(Process *processes, int numProcesses);                                    // Function prototype for fcfs
void rr(Process *processes, int numProcesses, int quantumSize);                     // Function prototype for rr
void spn(Process *processes, int numProcesses);                                     // Function prototype for spn
void srt(Process *processes, int numProcesses);                                     // Function prototype for srt
void calculateAndDisplayAverages(Process *processes, int numProcesses);             // Function prototype for calculateAndDisplayAverages

#endif                                                                              // Include guard
