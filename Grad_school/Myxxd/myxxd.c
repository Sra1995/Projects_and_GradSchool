#include <stdio.h>                                                      // Include the standard input/output library
#include <stdlib.h>                                                     // Include the standard library, atoi()
#include <string.h>                                                     // Include the string manipulation library strcmp()
#include <ctype.h>                                                      // Include the header for isprint function


void print_help() {
    printf("Usage: mxxd [options] [infile [outfile]]\n");               // Print the usage message
    printf("Options:\n");                                               // Print the options message
    printf("-v\t\tshow version string\n");                              // Print the option for showing version string
    printf("-h\t\tprint a summary of available commands and exit\n");   // Print the option for printing a summary of available commands and exit
    printf("-p\t\toutput in postscript continuous hexdump style\n");    // Print the option for outputting in postscript continuous hexdump style
    printf("-b\t\tswitch to bits (binary digits) dump\n");              // Print the option for switching to bits (binary digits) dump
    printf("-a\t\ttoggle autoskip\n");                                  // Print the option for toggling autoskip
    printf("-l len\t\tstop after writing <len> octets\n");              // Print the option for stopping after writing <len> octets
    printf("-g bytes\tseparate the output of every <bytes> bytes\n");   // Print the option for separating the output of every <bytes> bytes
}

void print_version() {
    printf("mxxd version 1.0\n");                                       // Print the version number
}
                                                                        // the hexdump function
void hexdump(FILE* infile, FILE* outfile, int postscript, int bits, int autoskip, int len, int groupsize) { 
    unsigned char buffer[16];                                           // Create a buffer to store the read bytes
    size_t bytesRead = 0;                                               // Initialize the variable to store the number of bytes read
    int totalBytesRead = 0;                                             // Initialize the variable to store the total number of bytes read
    int lineCount = 0;                                                  // Initialize the variable to store the line count

    while ((bytesRead = fread(buffer, 1, sizeof(buffer), infile)) > 0) { // Read bytes from the input file into the buffer
        totalBytesRead += bytesRead;                                    // Update the total number of bytes read

        if (len > 0 && totalBytesRead > len) {                          // Check if the total number of bytes read exceeds the specified length
            bytesRead -= (totalBytesRead - len);                        // Adjust the number of bytes read
            totalBytesRead = len;                                       // Update the total number of bytes read
        }

        if (postscript && bits) {
            printf("Error: Cannot specify both -p and -b options.\n");  // Print an error message
            return;
        }

        if (postscript) {
                                                                        // Output in postscript continuous hexdump style if -p selected
            for (size_t i = 0; i < bytesRead; i++) {
                fprintf(outfile, "%02x", buffer[i]);                    // Print the byte in hexadecimal format
            }
            fprintf(outfile, "\n");                                     // Print a new line
        } else if (bits) {
                                                                        // Output in bits (binary digits) dump if -b selected
            fprintf(outfile, "%08x: ", lineCount * 16);                 // Print the line number in hexadecimal format

            for (size_t i = 0; i < bytesRead; i++) {
                for (int j = 7; j >= 0; j--) {
                    fprintf(outfile, "%d", (buffer[i] >> j) & 1);       // Print each bit of the byte
                }

                fprintf(outfile, " ");                                  // Print a space after every group of bits
            }

            fprintf(outfile, " ");                                      // Print a space

            for (size_t i = 0; i < bytesRead; i++) {                    // Print the printable characters   
                if (isprint(buffer[i])) {                              // Check if the character is printable
                    fprintf(outfile, "%c", buffer[i]);                  // Print the printable character
                } else {
                    fprintf(outfile, ".");                              // Print a dot for non-printable characters
                }
            }

            fprintf(outfile, "\n");                                     // Print a new line

        } else {
                                                                        // Output in default hexdump style
            fprintf(outfile, "%08x  ", lineCount * 16);                 // Print the line number in hexadecimal format

            for (size_t i = 0; i < bytesRead; i += 2) {
                fprintf(outfile, "%02x%02x ", buffer[i], buffer[i + 1]); // Print the bytes in hexadecimal format

                if ((i + 2) % groupsize == 0) {
                    fprintf(outfile, " ");                                  // Print a space after every group of bytes
                }
            }

            if (autoskip && bytesRead < sizeof(buffer)) {              // Check if autoskip is enabled and the number of bytes read is less than the buffer size
                for (unsigned long i = bytesRead; i < sizeof(buffer); i++) {
                    fprintf(outfile, "   ");                                // Print spaces for the remaining bytes

                    if ((i + 1) % groupsize == 0) {                        // Check if the remaining bytes form a group
                        fprintf(outfile, " ");                              // Print a space after every group of bytes
                    }
                }
            }

            fprintf(outfile, " |");                                         // Print the separator

            for (size_t i = 0; i < bytesRead; i++) {                        // Print the printable characters
                if (isprint(buffer[i])) {
                    fprintf(outfile, "%c", buffer[i]);                      // Print the printable character
                } else {
                    fprintf(outfile, ".");                                  // Print a dot for non-printable characters
                }
            }

            fprintf(outfile, "|\n");                                        // Print a new line
        }

        lineCount++;                                                        // Increment the line count

        if (len > 0 && totalBytesRead >= len) {
            break;                                                          // Break the loop if the specified length is reached
        }
    }
}


int main(int argc, char* argv[]) {                                          // The main function
    FILE* infile = stdin;                                                   // Initialize the input file pointer to stdin
    FILE* outfile = stdout;                                                 // Initialize the output file pointer to stdout
    int postscript = 0;                                                     // Initialize the flag for postscript output to 0
    int bits = 0;                                                           // Initialize the flag for bits output to 0
    int autoskip = 0;                                                       // Initialize the flag for autoskip to 0
    int len = -1;                                                           // Initialize the length to -1
    int groupsize = 2;                                                      // Initialize the group size to 2

                                                                            // Parse command line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0) {                                   // Check if the -v option is selected
            print_version();                                                // Print the version string
            return 0;
        } else if (strcmp(argv[i], "-h") == 0) {                            // Check if the -h option is selected
            print_help();                                                   // Print the help message
            return 0;
        } else if (strcmp(argv[i], "-p") == 0) {                            // Check if the -p option is selected
            postscript = 1;                                                 // Set the postscript flag to 1
        } else if (strcmp(argv[i], "-b") == 0) {                            // Check if the -b option is selected
            bits = 1;                                                       // Set the bits flag to 1
        } else if (strcmp(argv[i], "-a") == 0) {                            // Check if the -a option is selected
            autoskip = 1;                                                   // Set the autoskip flag to 1
        } else if (strcmp(argv[i], "-l") == 0) {                            // Check if the -l option is selected
            if (i + 1 < argc) {
                len = atoi(argv[i + 1]);                                    // Get the length from the next argument
                i++;
            } else {                                                        // Check if the next argument(number) is missing
                printf("Error: Missing argument for -l option\n");          // Print an error message
                return 1;
            }
        } else if (strcmp(argv[i], "-g") == 0) {                            // Check if the -g option is selected
            if (i + 1 < argc) {
                groupsize = atoi(argv[i + 1]);                              // Get the group size from the next argument
                i++;
            } else {                                                        // Check if the next argument(number) is missing
                printf("Error: Missing argument for -g option\n");          // Print an error message
                return 1;
            }
        } else if (infile == stdin) {                                       // Check if the input file is stdin
            infile = fopen(argv[i], "rb");                                  // Open the input file in binary mode
            if (infile == NULL) {                                           // Check if the input file is opened successfully
                printf("Error: Failed to open input file\n");               // Print an error message
                return 1;
            }
        } else if (outfile == stdout) {                                     // Check if the output file is stdout
            outfile = fopen(argv[i], "wb");                                 // Open the output file in binary write mode
            if (outfile == NULL) {                                          // Check if the output file is opened successfully
                printf("Error: Failed to open output file\n");              // Print an error message
                return 1;
            }
        } else {
            printf("Error: Too many arguments\n");                          // Print an error message
            return 1;
        }
    }

    hexdump(infile, outfile, postscript, bits, autoskip, len, groupsize);    // Call the hexdump function

    if (infile != stdin) {                                                  // Check if the input file is not stdin
        fclose(infile);                                                     // Close the input file if it is not stdin
    }
    if (outfile != stdout) {                                                // Check if the output file is not stdout
        fclose(outfile);                                                    // Close the output file if it is not stdout
    }

    return 0;                                                               // Return 0 to indicate successful execution
}
