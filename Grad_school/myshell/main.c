/*
CSC521 Operating Systems 
Project #1: – A MyShell Program
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 02/14/2024
Date modified: 03/08/2024
*/

#include "util.h"                                                                               // Utility functions for string manipulation and error handling.
#include "shell_commands.h"                                                                     // Functions for internal shell commands.

#include <stdio.h>                                                                              // Standard input/output operations (e.g., printf).
#include <stdlib.h>                                                                             // Standard library functions (e.g., memory allocation).
#include <string.h>                                                                             // String manipulation functions (e.g., strcmp).
#include <sys/types.h>                                                                          // Data types used in system calls.
#include <sys/wait.h>                                                                           // Functions and macros for process management.
#include <unistd.h>                                                                             // POSIX API for system calls (e.g., fork and exec).


void display_not_allowed_message(const char *command) {                                         // Display a message for disallowed commands
    fprintf(stderr, "Command '%s' is not allowed in MyShell.\n", command);
}

int main() {
    char *line;                                                                                 // User input
    char **arguments;                                                                           // User input parsed into arguments as an array of strings
    pid_t child_pid;                                                                            // Child process ID
    int status;                                                                                 // Child process status

    while (1) {                                                                                 // Infinite loop
                                                                                                // Display the command prompt with the current directory
        char *current_dir = getcwd(NULL, 0);                                                    // Get the current directory
        printf("%s/myshell) ", current_dir);                                                    // Display the command prompt
        free(current_dir);                                                                      // Free allocated memory

                                                                                                // Read user input
        line = read_line();                                                                     // Read a line from the user

                                                                                                // Parse arguments
        arguments = parse_arguments(line);                                                      // Parse the line into arguments

                                                                                                // Internal commands
        if (arguments[0] != NULL) {                                                             // Check if the user entered a command
            if (strcmp(arguments[0], "myecho") == 0) {                                          // Check if the user entered the myecho command
                myecho(arguments);                                                              // Execute the myecho command
                free(line);                                                                     // Free allocated memory
                free_arguments(arguments);                                                      // Free allocated memory
                continue;                                                                       // Skip the rest of the loop for myecho
            } else if (strcmp(arguments[0], "mycd") == 0) {                                     // Check if the user entered the mycd command
                mycd(arguments[1]);                                                             // Execute the mycd command
            } else if (strcmp(arguments[0], "myclr") == 0) {                                    // Check if the user entered the myclr command
                myclr();                                                                        // Execute the myclr command
            } else if (strcmp(arguments[0], "mydir") == 0) {                                    // Check if the user entered the mydir command
                mydir(arguments[1]);                                                            // Execute the mydir command
            } else if (strcmp(arguments[0], "myenviron") == 0) {                                // Check if the user entered the myenviron command
                myenviron();                                                                    // Execute the myenviron command
            } else if (strcmp(arguments[0], "myhelp") == 0) {                                   // Check if the user entered the myhelp command
                myhelp();                                                                       // Execute the myhelp command
            } else if (strcmp(arguments[0], "mypause") == 0) {                                  // Check if the user entered the mypause command
                mypause();                                                                      // Execute the mypause command
            } else if (strcmp(arguments[0], "myquit") == 0) {                                   // Check if the user entered the myquit command
                myquit();                                                                       // Execute the myquit command
            } else {
                                                                                                // Check for disallowed external commands that are similar to internal commands (e.g., myecho)
                if (strcmp(arguments[0], "cd") == 0 ||
                    strcmp(arguments[0], "clear") == 0 ||
                    strcmp(arguments[0], "ls") == 0 ||
                    strcmp(arguments[0], "printenv") == 0 ||
                    strcmp(arguments[0], "echo") == 0 ||
                    strcmp(arguments[0], "man") == 0 ||
                    strcmp(arguments[0], "info") == 0 ||
                    (strcmp(arguments[0], "read") == 0 && strcmp(arguments[1], "-p") == 0) ||
                    strcmp(arguments[0], "exit") == 0) {
                    display_not_allowed_message(arguments[0]);                                  // Display a message for disallowed commands
                } else {
                                                                                                // External command
                    child_pid = fork();                                                         // Create a child process
                    if (child_pid == 0) {                                                       // check Child process
                        execvp(arguments[0], arguments);                                        // Replace the current process with the specified external command
                        print_error("Command not found");                                       // Display error message if execvp fails
                        exit(EXIT_FAILURE);
                    } else if (child_pid < 0) {
                                                                                                // Fork error
                        print_error("Fork failed");                                             // Display error message if fork fails
                    } else {
                                                                                                // Parent process
                        waitpid(child_pid, &status, 0);                                         // Wait for the child process to complete
                    }
                }
            }
        }

                                                                                                // Free allocated memory
        free(line);                                                                             // Free allocated memory from the user input line
        free_arguments(arguments);                                                              // Free allocated memory from the user input arguments
    }

    return 0;                                                                                   // Exit the program
}
