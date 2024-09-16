import sys                                                                      # For command-line arguments
import os                                                                       # For checking if output file exists

def word_lines(input_file, output_file):                                        # function takes inputfile and outputfile as arguments
    Word_Dict = {}                                                              # Create an empty dictionary to store the word occurrences
    with open(input_file, 'r') as input:                                        # Open input file for reading
        line_number = 1                                                         # Initialize line number counter
        for line in input:                                                      # Iterate over each line in the list
            words = [x for x in line.split()]                                   # Split the line into words using space as the separator and store them in a list
            for value in words:                                                 # Iterate over the words in the list
                if value in Word_Dict:                                          # If the word is not in the dictionary, add it with an empty list as its value
                    Word_Dict[value].append(line_number)                        # Append the line number to the list of line numbers for the word
                else:
                    Word_Dict[value] = [line_number]                            # If the word is not in the dictionary, add it with an empty list as its value
            line_number += 1                                                    # Increment line number counter


    if os.path.exists(output_file):                                             # if the output file exists, print a warning message
        print("Output file already exists. It will be overwritten.")

    with open(output_file, 'w') as output:                                      # Open output file for writing
        for x in Word_Dict.keys():                                              # Iterate over the items in the dictionary, sorted alphabetically
            output.write(f"{x} = {' '.join(map(str, Word_Dict[x]))}\n")         # Write the word, number of lines, and line numbers to the output file

    print("Processing completed. Check the output in", output_file)             # Print a success message

def main():                                                                     # Main function
    if len(sys.argv) != 3:                                                      # if the number of arguments is not equal to 3, print an error message
        print("Usage: python3 myprogram.py input.txt output.txt")
        print("You have entered", len(sys.argv), "arguments")                   # print message stating the number of arguments entered, which is not 3
        print("please try again")
        sys.exit(1)                                                             # Exit the program

    input_file = sys.argv[1]                                                    # Get input file name from command-line arguments
    output_file = sys.argv[2]                                                   # Get output file name from command-line arguments

    word_lines(input_file, output_file)                                         # Count word occurrences and write to output file

if __name__ == "__main__":                                                      # if the file is run directly, run the main function
    main()                                                                      # Call the main function
