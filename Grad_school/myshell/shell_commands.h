/*
CSC521 Operating Systems 
Project #1: – A MyShell Program
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 02/14/2024
Date modified: 03/08/2024
*/

#ifndef SHELL_COMMANDS_H
#define SHELL_COMMANDS_H

                                                                        // Function declarations for internal commands
void mycd(char *directory);                                             // Change the current working directory
void myclr();                                                           // Clear the screen
void mydir(const char *directory);                                      // List and print the contents of a directory
void myenviron();                                                       // Print the environment variables
void myecho(char **comment);                                            // Echo and modify the output of the provided comments
void myhelp();                                                          // Display help information
void mypause();                                                         // Pause execution and wait for the user to press Enter
void myquit();                                                          // Exit the program

#endif
