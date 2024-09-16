/*
CSC521 Operating Systems 
Lab #2: Command Line Calculator
Programmers: Sajjad Alsaffar
Professor: Dr. Lee
Date created: 01/25/2023
Date modified: 01/28/2023
*/

#include <stdio.h> 
#include <stdlib.h>                                                                                         // for atoi
#include <string.h>                                                                                         // for strcmp
#include <ctype.h>                                                                                          // for isdigit

int is_valid_integer(const char *str) {                                                                     // function to validate if all characters in a string are digits != 123abc456
                                                                                                            // Check if the string is empty or null
    if (str == NULL || *str == '\0') {                                                                      // if the string is empty or null
        return 0;                                                                                           // Return 0 to indicate an error (empty or null string)
    }

                                                                                                            // Handle optional negative sign
    if (*str == '-' || *str == '+') {                                                                       // if the first character is a negative or positive sign
        str++;                                                                                              // Move to next character in string
    }

    while (*str != '\0') {                                                                                  // while the string is not empty
        if (!isdigit(*str)) {                                                                               // if the character is not a digit
            return 0;                                                                                       // Return 0 to indicate an error (non-digit character found)
        }
        str++;                                                                                              // Move to the next character in the string
    }

    return 1;                                                                                               // Return 1 to indicate success (all characters are digits)
}

int main(int argc, char *argv[]) {
                                                                                                            // Check if the correct number of command line arguments are provided
    if (argc != 4) {                                                                                        // 4 arguments are needed ./program num1 num2 operator
        printf("Usage: %s <num1> <num2> <operator>\n", argv[0]);
        return 1;                                                                                           // exit with error
    }

    // Validate num1 and num2
    if (!is_valid_integer(argv[1]) || !is_valid_integer(argv[2])) {
        fprintf(stderr, "Invalid input for num1 or num2. Please enter valid integers.\n");
        return 1;
    }

                                                                                                            // Convert command line arguments to integers
    int num1 = atoi(argv[1]);                                                                               // atoi converts first string to integer num1
    int num2 = atoi(argv[2]);                                                                               // atoi converts second string to integer num2

                                                                                                            // Check if conversion was successful
    if (num1 == 0 && argv[1][0] != '0') {                                                                   // argv[1][0] != '0' checks if the first character of the string is not 0
        printf("Invalid input for num1. Please enter a valid integer.\n");
        return 1;                                                                                           // exit with error
    }
    if (num2 == 0 && argv[2][0] != '0') {                                                                   // argv[2][0] != '0' checks if the first character of the string is not 0
        printf("Invalid input for num2. Please enter a valid integer.\n");
        return 1;                                                                                           // exit with error
    }

                                                                                                            // Get the operator
    char *operator = argv[3];                                                                               // Get the operator from the command line +,-,*,/,%,//

                                                                                                            // Perform the operation based on the selected operator
    if (strcmp(operator, "+") == 0) {                                                                       // strcmp compares the string operator with the string "+"
        printf("%d + %d = %d\n", num1, num2, num1 + num2);                                                  // adds num1 to num2 and display the result
    } else if (strcmp(operator, "-") == 0) {                                                                // strcmp compares the string operator with the string "-"
        printf("%d - %d = %d\n", num1, num2, num1 - num2);                                                  // subtracts num2 from num1 and display the result
    } else if (strcmp(operator, "*") == 0) {                                                                // strcmp compares the string operator with the string "*"
        printf("%d * %d = %d\n", num1, num2, num1 * num2);                                                  // multiplies num1 by num2 and display the result
    } else if (strcmp(operator, "/") == 0) {                                                                // strcmp compares the string operator with the string "/"
        if (num2 == 0) {                                                                                    // Check for division by zero
            printf("Division by zero is not allowed.\n");                                                   // Display error message division by zero is not allowed
            return 1;                                                                                       // exit with error
        }
        printf("%d / %d = %.2f\n", num1, num2, (float)num1 / num2);                                         // divides num1 by num2 and display the result as float 2 decimal places as requested
    } else if (strcmp(operator, "%") == 0) {                                                                // strcmp compares the string operator with the string "%"
        if (num2 == 0) {                                                                                    // Check for division by zero
            printf("Modulo by zero is not allowed.\n");                                                     // Display error message modulo by zero is not allowed
            return 1;                                                                                       // exit with error
        }
        printf("%d %% %d = %d\n", num1, num2, num1 % num2);                                                 // calculates the remainder of num1 divided by num2 and display the result
    } else if (strcmp(operator, "//") == 0) {                                                               // strcmp compares the string operator with the string "//"
        if (num2 == 0) {                                                                                    // Check for division by zero
            printf("Integer division by zero is not allowed.\n");                                           // Display error message integer division by zero is not allowed
            return 1;                                                                                       // exit with error
        }
        printf("%d // %d = %d\n", num1, num2, num1 / num2);                                                 // calculates the integer division of num1 by num2 and display the result as integer no decimal places
    } else {
        printf("Invalid operator. Supported operators are +, -, *, /, %%, //.\n");                          // Display error message invalid operator
        printf("Note: depending on shell being used for multiplication you might need to do '*' \n");       // Display Note message for multiplication
        return 1;                                                                                           // exit with error
    }

    return 0;                                                                                               // exit with success
}




/*
Notes for programmer:
checks:
1. letters and note numbers
2. negative numbers need to work aka converted
3. division by zero and modulo by zero don't allow it
4. integer division and float division use %d and %.2f
5. switch case would work if we are only using +,-,*,/,% and not //
6. * works in switch case but not // 
7. * in command line needs to be escaped with \*

]printf("Operator ASCII value: %d\n", *operator);                                                        // prints the ASCII value of the operator

int correct_modulo(int x, int y) {
    return (x % y + y) % y;
} produce % result as python - C is different as it follows the sign of the number being divided and not the divisor

switch case for operators works until '//' this need to include a space in the command line argument to work properly but this will make the program have more than 4 arguments and will not work as requested
*/