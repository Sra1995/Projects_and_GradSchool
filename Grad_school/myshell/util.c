/*
CSC521 Operating Systems 
Project #1: – A MyShell Program
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 02/14/2024
Date modified: 03/08/2024
*/

#include "util.h"                                                                   // Include the header file "util.h" for function prototypes
#include <stdio.h>                                                                  // Include the standard input/output library
#include <stdlib.h>                                                                 // Include the standard library for memory allocation functions
#include <string.h>                                                                 // Include the string manipulation library


void print_error(const char *message) {                                             // Function to print an error message to the standard error stream
    fprintf(stderr, "Error: %s\n", message);                                        // Print the error message to the standard error stream
}

char* read_line() {                                                                 // Function to read a line from the standard input
    char *line = NULL;                                                              // Initialize a pointer to store the input line
    size_t bufsize = 0;                                                             // Initialize the buffer size for getline to dynamically allocate memory

    getline(&line, &bufsize, stdin);                                                // Use getline to read a line from the standard input

                                                                                    // Remove the newline character, if present
    size_t len = strlen(line);                                                      // Get the length of the input line
    if (len > 0 && line[len - 1] == '\n') {                                         // Check if the last character is a newline
        line[len - 1] = '\0';                                                       // Replace the newline character with null terminator
    }

    return line;                                                                    // Return the pointer to the input line
}

char** parse_arguments(char *line) {                                                // Function to parse arguments from a given input line
    const char *delimiter = " \t\r\n\a";                                            // Define a set of delimiters for tokenizing the input line
    char **arguments = malloc(sizeof(char*) * MAX_ARGS);                            // Allocate memory for an array of strings to store arguments
    if (!arguments) {                                                               // Check if memory allocation fails
        print_error("Memory allocation error");                                     // Print an error message
        exit(EXIT_FAILURE);                                                         // Exit the program with a failure status
    }

    int index = 0;                                                                  // Initialize an index for the arguments array
    char *token = strtok(line, delimiter);                                          // Tokenize the input line using the specified delimiters
    while (token != NULL) {                                                         // Iterate through the tokens
        arguments[index] = strdup(token);                                           // Allocate memory and copy the token to the arguments array
        if (!arguments[index]) {                                                    // Check if memory allocation fails
            print_error("Memory allocation error");                                 // Print an error message
            exit(EXIT_FAILURE);                                                     // Exit the program with a failure status
        }

        index++;                                                                    // Move to the next index in the arguments array
        token = strtok(NULL, delimiter);                                            // Get the next token
    }

    arguments[index] = NULL;                                                        // Null-terminate the array

    return arguments;                                                               // Return the array of arguments
}

void free_arguments(char **arguments) {                                             // Function to free the memory allocated for the arguments array
    for (int i = 0; arguments[i] != NULL; i++) {                                    // Iterate through the arguments array
        free(arguments[i]);                                                         // Free the memory allocated for each argument
    }
    free(arguments);                                                                // Free the memory allocated for the arguments array itself
}
