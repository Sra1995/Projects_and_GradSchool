/*
CSC521 Operating Systems 
Project #2: – Short Term Scheduling
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 03/11/2024
Date modified: 03/27/2024
*/
#include "utils.h"
#include <stdio.h>
#include <stdlib.h>

int readProcessesFromFile(const char *filename, Process **processes) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Error opening input file");
        exit(EXIT_FAILURE);
    }

    // Count the number of lines in the file
    int numProcesses = 0;
    char ch;
    while (!feof(file)) {
        ch = fgetc(file);
        if (ch == '\n') {
            numProcesses++;
        }
    }
    rewind(file);

    // Allocate memory for processes
    *processes = (Process *)malloc(numProcesses * sizeof(Process));

    // Read processes from the file
    for (int i = 0; i < numProcesses; i++) {
        fscanf(file, "%d %d", &((*processes)[i].arrivalTime), &((*processes)[i].serviceTime));
    }

    fclose(file);
    return numProcesses;
}
