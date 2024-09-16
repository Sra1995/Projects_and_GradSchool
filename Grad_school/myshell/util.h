/*
CSC521 Operating Systems 
Project #1: – A MyShell Program
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 02/14/2024
Date modified: 03/08/2024
*/

// util.h
#ifndef UTIL_H
#define UTIL_H

#define MAX_ARGS 64                                                     // Define the maximum number of command-line arguments
                                                                        // Function prototypes
void print_error(const char *message);                                  // Print an error message to the standard error stream
char* read_line();                                                      // Read a line from the standard input
char** parse_arguments(char *line);                                     // Parse arguments from a given input line
void free_arguments(char **arguments);                                  // Free the memory allocated for the arguments array

#endif
