/*
CSC521 Operating Systems 
Project #1: – A MyShell Program
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 02/14/2024
Date modified: 03/08/2024
*/

#include "shell_commands.h"                                                                     // header file for shell commands
#include <stdio.h>                                                                              // Standard input/output operations (e.g., printf).
#include <stdlib.h>                                                                             // Standard library functions (e.g., memory allocation).
#include <string.h>                                                                             // String manipulation functions (e.g., strcmp).
#include <unistd.h>                                                                             // POSIX API for system calls (e.g., fork and exec).
#include <dirent.h>                                                                             // Directory manipulation functions (e.g., opendir and readdir).
#include <ctype.h>                                                                              // Character classification functions (e.g., isspace).


void mycd(char *directory) {                                                                    // Function to change the current working directory
    if (directory == NULL) {                                                                    // If no directory is provided
        char *current_dir = getcwd(NULL, 0);                                                    // Get the current working directory
        if (current_dir != NULL) {                                                              // If getting the current directory was successful
            printf("%s\n", current_dir);                                                        // Print the current directory
            free(current_dir);                                                                  // Free the memory allocated by getcwd
        } else {
            perror("getcwd");                                                                   // Print an error message if getcwd fails
        }
    } else {                                                                                    // If a directory is provided
        if (chdir(directory) == 0) {                                                            // Change the current working directory to the specified directory
            setenv("PWD", directory, 1);                                                        // Update the PWD environment variable to the new directory
        } else {
            perror("chdir");                                                                    // Print an error message if chdir fails
        }
    }
}

void myclr() {                                                                                  // Function to Clear the screen by printing escape sequence for clear screen
                                                                                                // ANSI escape code "\033[2J" clears the entire screen.
                                                                                                // ANSI escape code "\033[H" positions the cursor at the top-left corner of the screen.
    printf("\033[2J\033[H"); 
    fflush(stdout);                                                                             // Flush the standard output stream to ensure immediate display of the cleared screen.
}


void mydir(const char *directory) {                                                             // Function to list and print the contents of a directory
    DIR *dir;                                                                                   // Pointer to a directory stream
    struct dirent *entry;                                                                       // Pointer to a directory entry structure

                                                                                                // Open the directory
    dir = opendir(directory ? directory : ".");                                                 // If directory is NULL, open the current directory ("."), otherwise open the specified directory
    if (dir == NULL) {
        perror("Error opening directory");                                                      // Print an error message if opening the directory fails
        return;
    }

                                                                                                // Read and print directory contents, excluding "." and ".."
    while ((entry = readdir(dir)) != NULL) {                                                    // Read each directory entry
        if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {              // Exclude entries for "." and ".."
            printf("%s\t", entry->d_name);                                                      // Print the name of the directory entry
        }
    }

    printf("\n");                                                                               // Print a newline after listing all directory contents

    closedir(dir);                                                                              // Close the directory stream
}



void myenviron() {                                                                              // Function to print the environment variables
    extern char** environ;                                                                      // External reference to the array of environment variables

    for (char** env = environ; *env != NULL; ++env) {                                           // Iterate through each environment variable
        printf("%s\n", *env);                                                                   // Print the current environment variable
    }
}

void myecho(char **comment) {                                                                   // Function to echo and modify the output of the provided comments
    for (int i = 1; comment[i] != NULL; i++) {                                                  // Loop through each comment provided as arguments
        int j = 0;                                                                              // Initialize a variable to traverse each character in the comment
        while (comment[i][j] != '\0') {                                                         // Loop through each character in the current comment
            if (!isspace((unsigned char)comment[i][j])) {                                       // Check if the current character is not a whitespace character
                putchar(comment[i][j]);                                                         // Print the non-whitespace character
            } else {
                putchar(' ');                                                                   // Print a single space
                while (isspace((unsigned char)comment[i][j])) {                                 // Skip consecutive whitespace characters
                    j++;
                }
                j--;                                                                            // Adjust the index to account for the increment in the outer loop
            }
            j++;                                                                                // Move to the next character in the comment
        }
        putchar(' ');                                                                           // Print a space between comments
    }
    printf("\n");                                                                               // Print a newline after processing all comments
}


void myhelp() {                                                                                 // Function to display help information by executing the "more" command on a readme file
    system("more manual");                                                                      // Use the system command to execute "more readme"
}


void mypause() {                                                                                // Function to pause execution and wait for the user to press Enter
    printf("Press Enter to continue...");                                                       // Display a prompt for the user to press Enter
    while (getchar() != '\n');                                                                  // Wait for the user to press Enter by consuming characters until a newline is encountered
}

void myquit() {                                                                                 // Function to exit the program
    exit(0);                                                                                    // Terminate the program with exit status 0
}
