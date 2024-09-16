/*
 CSC520 Computer Architecture
 Project1 - IEEE 754 Converter
 Programmers: Sajjad Alsaffar
 Professor: Dr. Jeonghwa Lee
 File Created: September 22th, 2023
 File Updated: September 27th, 2023
*/

#include <stdio.h>                                                                // Include the standard input/output library for input and output functions
#include <stdint.h>                                                               // Include the standard integer types library for fixed-size integer types
#include <string.h>                                                               // Include the string manipulation library for string-related functions

/*
    Function to convert a float to its hexadecimal representation
    Create a pointer to a 32-bit unsigned integer and point it to the memory where 'num' is stored
    Format 'num' as a hexadecimal string with 8 digits and 'a' character, and store it in 'hex'
*/
void floatToHex(float num, char hex[11]) {
    uint32_t* ptr = (uint32_t*)&num;                                              // Create a pointer to a 32-bit unsigned integer and point it to the memory where 'num' is stored
    snprintf(hex, 11, "0x%08X", *ptr);                                           // Format 'num' as a hexadecimal string with 8 digits, and store it in 'hex'
}

/*
   Function to convert a hexadecimal representation to a float

   Parameters:
   - hex: A character array containing the input hexadecimal representation (11 characters including the null terminator)

   Returns:
   - The floating-point number corresponding to the hexadecimal representation

   This function takes a hexadecimal string 'hex' and converts it into a floating-point number. The result is returned as a float.
*/
float hexToFloat(const char hex[11]) {
    uint32_t value;                                                              // Declare a 32-bit unsigned integer variable 'value'
    int numConverted = sscanf(hex, "0x%08X", &value);                            // Attempt to convert the 'hex' string to a 32-bit unsigned integer value

    if (numConverted == 1) {                                                     // If successful, reinterpret 'value' as a float and return it
        return *((float*)&value);
    }

    return 0.0f;                                                                 // Return 0.0 in case of conversion failure
}

/* 
   The main function provides a user interface for the IEEE 754 converter program. It allows the user to choose from the following options:

   - 'f': Convert float to hexadecimal
     - Prompts the user to enter a floating-point number and converts it to its hexadecimal representation.
   - 'h': Convert hexadecimal to float
     - Prompts the user to enter a hexadecimal representation and converts it to a floating-point number.
   - 'q': Quit the program
     - Exits the program when 'q' is entered.

   The program runs in an infinite loop, continuously prompting the user for their choice until 'q' is entered to quit.
*/
int main() {
    char choice;                                                                // Declare a character variable 'choice' to store user input
    
    while (1) {                                                                 // Infinite loop to continuously prompt the user to pick a choice
        printf("Enter 'f' to convert float to hexadecimal, 'h' to convert hexadecimal to float, or 'q' to quit: ");
        scanf(" %c", &choice);                                                  // Read a single character input from the user

        if (choice == 'q') {
            break;                                                              // Exit the loop and end the program if 'q' is entered
        } else if (choice == 'f') {
                                                                                // Option 'f': Convert float to hexadecimal
            float num;                                                          // Declare a float variable 'num' to store the user's float input
            printf("Enter a floating-point number: ");
            scanf("%f", &num);                                                  // Read a float input from the user and store it in 'num'

            char hex[11];                                                       // Declare a character array 'hex' to store the hexadecimal representation
            floatToHex(num, hex);                                               // Convert 'num' to hexadecimal and store it in 'hex'
            printf("Hexadecimal representation: %s\n", hex);                    // Print the hexadecimal representation
        } else if (choice == 'h') {
                                                                                // Option 'h': Convert hexadecimal to float
            char hex[11];                                                       // Declare a character array 'hex' to store the hexadecimal input
            printf("Enter a hexadecimal representation (e.g., 0x3E99999a **8 char after 0x ): ");
            scanf("%10s", hex);                                                 // Read up to 10 characters as hexadecimal input from the user and store it in 'hex'

            float num = hexToFloat(hex);                                        // Convert 'hex' to a float and store it in 'num'
            printf("Floating-point representation: %f\n", num);                 // Print the floating-point representation
        } else {
            printf("Invalid choice. Please enter 'f', 'h', or 'q' to quit.\n"); // Print an error message for invalid input
        }
    }

    return 0;                                                                   // Return 0 to indicate successful program execution
}
