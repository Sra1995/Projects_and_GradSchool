#****************************************************************
# DFA Simulator
# Author: Sajjad Alsaffar
#
# Purpose: This program simulates a Deterministic Finite Automaton (DFA).
# It reads a DFA definition from a file (DFA.txt) and evaluates strings
# provided by the user. The output is a computation trace and an
# indication of whether the string is accepted or rejected by the DFA.
#****************************************************************

def load_dfa(filename):                                                                     # function to load the DFA from a text file
    """Loads the DFA from a text file."""
    with open(filename, 'r') as file:                                                       # while the file is open as read only do the below
        # First line: number of states
        num_states = int(file.readline().strip())                                           # read the first line and strip the white spaces

        # Second line: accepting states
        accepting_states = set(map(int, file.readline().strip().split()))                   # read the second line and strip the white spaces

        # Third line: alphabet symbols
        alphabet = file.readline().strip().split()                                          # read the third line and strip the white spaces

        # Fourth and subsequent lines: transition table
        transitions = []                                                                    # create an empty list to store the transitions
        for _ in range(num_states):                                                         # loop through the number of states
            transitions.append(list(map(int, file.readline().strip().split())))             # append the transitions to the list and strip the white spaces

    return num_states, accepting_states, alphabet, transitions                              # return the number of states, accepting states, alphabet and transitions

def evaluate_string(dfa, input_string):                                                     # function to evaluate the string takes the DFA and the input string
    """Evaluates whether the input string is accepted or rejected by the DFA."""
    num_states, accepting_states, alphabet, transitions = dfa                               # unpack the DFA
    current_state = 0                                                                       # Start at the initial state

    computation_trace = [(current_state, input_string)]                                     # Store the computation trace in a list

    for char in input_string:                                                               # Loop through the input string
        if char not in alphabet:                                                            # Check if the character is in the alphabet
            print(f"{current_state},{input_string} -> INVALID INPUT")                       # If not the input is not alphabet like 234 or b233, return "REJECTED"
            return "REJECTED"                                                               # Invalid input so return "REJECTED"
        else:                                                                               # If the character is in the alphabet
            char_index = alphabet.index(char)                                               # Get the index of the character in the alphabet
            current_state = transitions[current_state][char_index]                          # Update the current state based on the transition table
            input_string = input_string[1:]                                                 # Remove the first character from the input string by slicing
            computation_trace.append((current_state, input_string))                         # Append the current state and remaining input to the computation trace

    # Output computation trace
    print(">>>Computation…")                                                                # Print the computation....
    for i, (state, remaining_input) in enumerate(computation_trace):                        # Loop through the computation trace by index and the state and remaining input 
        if i < len(computation_trace) - 1:                                                  # if the index is less than the length of the computation trace - 1
            print(f"{state},{remaining_input} -> {computation_trace[i+1][0]},{computation_trace[i+1][1] if computation_trace[i+1][1] else '{e}'}")      # print the state, remaining input and the next state and remaining input
    
    # Check if the final state is an accepting state
    if current_state in accepting_states:                                                   # If the current state is in the accepting states return "ACCEPTED"
        return "ACCEPTED"                                                                   # If the current state is in the accepting states return "ACCEPTED"
    else:
        return "REJECTED"                                                                   # If the current state is not in the accepting states return "REJECTED"

def main():                                                                                 # Main function to run the program
    # Load the DFA from file
    print(">>>Loading DFA.txt...")                                                          # Print the loading message
    dfa = load_dfa('DFA.txt')                                                               # Load the DFA from the file

    while True:                                                                             # Loop until the user enters "quit"
        # Prompt user for input string
        input_string = input(">>>Please enter a string to evaluate: ").strip()              # Prompt the user to enter a string to evaluate and strip the white spaces
        if input_string.lower() == "quit":                                                  # If the user enters "quit" break the loop
            print(">>>Goodbye!")                                                            # Print goodbye message
            break                                                                           # Exit the loop

        # Evaluate the input string
        result = evaluate_string(dfa, input_string)                                         # Evaluate the input string
        print(result)                                                                       # Print the result

if __name__ == "__main__":                                                                  # if the script is run directly
    main()                                                                                  # Run the main function