/*****************************************************************
* Program: DFA Simulator
* Author: Sajjad
* 
* Purpose:
* This program simulates a Deterministic Finite Automaton (DFA).
* It reads a DFA definition from a file (DFA.txt), then evaluates
* input strings provided by the user. It outputs a computation 
* trace for each string and indicates whether the string is accepted
* or rejected by the DFA. The program handles invalid input 
* characters and can be terminated by entering "Quit".
* 
* Input:
* The DFA is loaded from a file in the following format:
* - Line 1: Number of states.
* - Line 2: Space-separated list of accepting states.
* - Line 3: Space-separated alphabet characters.
* - Lines 4+: Transition table for each state and alphabet character.
* 
* Output:
* The program prints the DFA computation trace for each string 
* and whether the string is "ACCEPTED" or "REJECTED".
* 
*****************************************************************/

#include <iostream>                                                                             // cin, cout standard input/output
#include <fstream>                                                                              // file input/output operations
#include <vector>                                                                               // dynamic arrays better than static arrays in this case
#include <set>                                                                                  // set data structure for accepting states
#include <string>                                                                               // string data type for input strings

using namespace std;                                                                            // standard namespace for cin, cout, etc.just C++ thingy

struct DFA {                                                                                    // struct for DFA 
    int num_states;                                                                             // number of states
    set<int> accepting_states;                                                                  // set of accepting states
    vector<char> alphabet;                                                                      // alphabet symbols
    vector<vector<int>> transitions;                                                            // transition table
};

                                                                                                // Function to load the DFA from a file
DFA load_dfa(const string& filename) {                                                          // argument is filename of the file to be loaded
    ifstream file(filename);                                                                    // file object to read the file
    DFA dfa;                                                                                    // DFA object to store the DFA
    if (!file) {                                                                                // error check in case file is not found
        cerr << "Error loading DFA file!" << endl;                                              // print error message and endline
        exit(1);                                                                                // exit the program with error code 1
    }

                                                                                                // First line: number of states
    file >> dfa.num_states;                                                                     // read the number of states from the file

                                                                                                // Second line: accepting states
    int state;                                                                                  // state variable to store the accepting states
    while (file.peek() != '\n') {                                                               // peek() function returns the next character in the input sequence without extracting it
        file >> state;                                                                          // read the state from the file
        dfa.accepting_states.insert(state);                                                     // insert the state into the set of accepting states
    }

                                                                                                // Third line: alphabet symbols
    char symbol;                                                                                // symbol variable to store the alphabet symbols
    while (file >> symbol && symbol != '\n') {                                                  // read the symbol from the file and check if it is not a newline character
        dfa.alphabet.push_back(symbol);                                                         // add the symbol to the alphabet
    }

                                                                                                // Fourth and subsequent lines: transition table
    dfa.transitions.resize(dfa.num_states, vector<int>(dfa.alphabet.size()));                   // resize the transition table to the number of states and alphabet size
    for (int i = 0; i < dfa.num_states; ++i) {                                                  // loop through the states to read the transitions
        for (int j = 0; j < dfa.alphabet.size(); ++j) {                                         // loop through the alphabet to read the transitions
            file >> dfa.transitions[i][j];                                                      // read the transition from the file
        }
    }

    return dfa;                                                                                 // return the DFA object
}

                                                                                                // Function to evaluate the string against the DFA
string evaluate_string(const DFA& dfa, const string& input_string) {                            // arguments are DFA object and input string
    int current_state = 0;                                                                      // current state is initialized to 0 (start state)
    string remaining_input = input_string;                                                      // remaining input is the input string

    cout << ">>>Computation…" << endl;                                                          // print computation... and endline
    for (size_t i = 0; i < input_string.size(); ++i) {                                          // loop through the input string characters
        char current_char = input_string[i];                                                    // current character is the character at index i
        
                                                                                                // Check if the character is part of the alphabet
        auto it = find(dfa.alphabet.begin(), dfa.alphabet.end(), current_char);                 // find the character in the alphabet
        if (it == dfa.alphabet.end()) {                                                         // if the character is not found
            cout << current_state << "," << remaining_input << " -> INVALID INPUT" << endl;     // print the current state, remaining input, and INVALID INPUT
            return "REJECTED";                                                                  // return REJECTED as the input is invalid
        }

        int char_index = distance(dfa.alphabet.begin(), it);                                    // get the index of the character in the alphabet
        int next_state = dfa.transitions[current_state][char_index];                            // get the next state from the transition table
        cout << current_state << "," << remaining_input << " -> " << next_state << "," << remaining_input.substr(1) << endl;            // print the current state, remaining input, next state, and remaining input without the first character

                                                                                                // Update current state and remaining input
        current_state = next_state;                                                             // update the current state to the next state (transition)
        remaining_input = remaining_input.substr(1);                                            // update the remaining input by removing the first character of the input string
    }

                                                                                                // Check if final state is an accepting state
    if (dfa.accepting_states.count(current_state)) {                                            // check if the final state is an accepting state
        return "ACCEPTED";                                                                      // return ACCEPTED if the final state is an accepting state
    } else {                                                                                    // if the final state is not an accepting state
        return "REJECTED";                                                                      // return REJECTED
    }
}

int main() {
                                                                                                // Load the DFA from file
    cout << ">>>Loading DFA.txt…" << endl;                                                      // print Loading DFA.txt and endline
    DFA dfa = load_dfa("DFA.txt");                                                              // load the DFA from the file DFA.txt

    while (true) {                                                                              // infinite loop to run program until user enters Quit
                                                                                                // Prompt user for input string
        cout << ">>>Please enter a string to evaluate: ";                                       // print Please enter a string to evaluate:
        string input_string;                                                                    // input string variable
        getline(cin, input_string);                                                             // get the input string from the user c++ equivalent of scanf in this case

        if (input_string == "Quit") {                                                           // check if the input string is Quit
            cout << ">>>Goodbye!" << endl;                                                      // print Goodbye! and endline
            break;                                                                              // break the loop to exit the program
        }

                                                                                                // Evaluate the input string
        string result = evaluate_string(dfa, input_string);                                     // evaluate the input string against the DFA
        cout << result << endl;                                                                 // print the result (ACCEPTED or REJECTED) and endline
    }

    return 0;                                                                                   // return 0 to indicate successful program execution just like C
}