import os                                                                                   # for checking if file exists
import csv                                                                                  # for reading the rotor files
import string                                                                               # for ascii_uppercase
import time                                                                                 # for the cool animation :D so so cool *sarcastic*

class Rotor:                                                                                # The rotor class is used to represent the rotors in an Enigma machine
    def __init__(self, wiring):
        self.wiring = wiring
        self.position = 0

    def forward(self, char): 
        index = (ord(char) - ord('A') + self.position) % 26
        return self.wiring[index]

    def backward(self, char):
        index = (self.wiring.index(char) - self.position) % 26
        return chr(index + ord('A'))

class Reflector:                                                                            # The reflector class is used to represent the reflector in an Enigma machine
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        return self.wiring[ord(char) - ord('A')]

class Plugboard:                                                                            # The plugboard class is used to represent the plugboard in an Enigma machine
    def __init__(self):
        self.mapping = dict(zip(string.ascii_uppercase, string.ascii_uppercase))

    def add_pair(self, pair):
        char1, char2 = pair[0], pair[1]
        
        if char1 in self.mapping and char2 in self.mapping:
            # Update mapping with new pairs
            self.mapping[char1] = char2
            self.mapping[char2] = char1
            print(f"Plugboard pair {char1} -> {char2} added.")
        else:
            print("Invalid plugboard pair. Both characters must be in the alphabet and not already paired.")

    def process(self, char):
        if char in self.mapping:
            return self.mapping[char]
        else:
            return char



class EnigmaMachine:                                                                        # The EnigmaMachine class is used to represent the Enigma machine
    def __init__(self, rotor_filenames, reflector_wiring):
        self.rotors = [self.load_rotor(filename) for filename in rotor_filenames]
        self.reflector = Reflector(reflector_wiring)
        self.plugboard = Plugboard()

    def load_rotor(self, filename):
        try:
            # Check if the file exists in the provided path
            if not os.path.exists(filename):
                # If the file doesn't exist, try to find it in the same directory as the script
                script_dir = os.path.dirname(os.path.realpath(__file__))
                filename = os.path.join(script_dir, filename)

                if not os.path.exists(filename):
                    raise FileNotFoundError

            with open(str(filename), 'r') as file:                                          # Convert filename to string
                reader = csv.reader(file)
                wiring = next(reader)[0]                                                    # Assuming the wiring is in the first row of the CSV
            return Rotor(wiring)

        except FileNotFoundError:
            print(f"Error: Rotor file '{filename}' not found.")
            return None

    def set_rotor_positions(self, positions):
        for i, position in enumerate(positions):
            self.rotors[i].position = position

    def add_plugboard_pair(self, pair):
        self.plugboard.add_pair(pair)

    def view_plugboard(self):
        print("Current plugboard pairs:")
        for char, mapped_char in self.plugboard.mapping.items():
            print(f"{char} -> {mapped_char}")

    def remove_plugboard_pair(self, char):
        if char in self.plugboard.mapping:
            mapped_char = self.plugboard.mapping[char]
            del self.plugboard.mapping[char]
            del self.plugboard.mapping[mapped_char]
            print(f"Plugboard pair {char} -> {mapped_char} removed.")
        else:
            print(f"Plugboard pair for {char} not found.")

    def encrypt(self, message):
        encrypted_message = ''
        for char in message:
            # Plugboard
            char = self.plugboard.process(char)

            # Rotors forward
            for rotor in self.rotors:
                char = rotor.forward(char)

            # Reflector
            char = self.reflector.reflect(char)

            # Rotors backward
            for rotor in reversed(self.rotors):
                char = rotor.backward(char)

            # Plugboard
            char = self.plugboard.process(char)

            encrypted_message += char
        return encrypted_message

    def decrypt(self, message):
        # The decryption process is the same as encryption in an Enigma machine
        return self.encrypt(message)



# Cool animation for the program name 
def print_letter_by_letter(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

    print()

# static after first run, just so we don't have to see it everytime as we go through options
def print_static_header():
    black = "\u001b[48;5;0m  \u001b[0m"  # Black background
    red = "\u001b[48;5;196m  \u001b[0m"    # Red background
    yellow = "\u001b[48;5;226m  \u001b[0m"  # Yellow background

    print("\n\n╔════════════════════════════════════╗")
    print("║   ",black+black+black,"              ",black+black+black,"   ║")
    print("║   ",red+red+red,"Enigma Machine",red+red+red,"   ║")
    print("║   ",yellow+yellow+yellow,"              ",yellow+yellow+yellow,"   ║")
    print("╚════════════════════════════════════╝")



def main():                                                                                 # Main function that will run on start of program
    rotor_filenames = []
    reflector_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    enigma = EnigmaMachine(rotor_filenames, reflector_wiring)
    first_run = True

    while True:                                                                             # Loop that will run until the user exits the program
        if first_run:
            print_letter_by_letter("Engima Machine turning on... ")
            print_letter_by_letter("Engima Machine is ready to use! \n", delay=0.03)
            print_static_header()
            first_run = False
        else:
            print_static_header()
        print("1. Set up rotors")
        print("2. Add plugboard pair")                                                      # the plugboard will rest upon setting up rotors, so add after rotors
        print("3. View plugboard pairs")
        print("4. Remove plugboard pair")
        print("5. Encrypt a message")
        print("6. Decrypt a message")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            rotor_filenames = []
            for i in range(3):
                filename = input(f"Enter full path for rotor {i+1} file: ")
                enigma_rotor = enigma.load_rotor(filename)
                if enigma_rotor:
                    rotor_filenames.append(filename)                                        # Add filename to list of rotor filenames
                else:
                    # If loading rotor failed, reset rotor_filenames
                    rotor_filenames = []
                    break

            if rotor_filenames:
                enigma = EnigmaMachine(rotor_filenames, reflector_wiring)

                positions = [int(input(f"Enter initial position for rotor {i+1} (0-25): ")) for i in range(3)]
                enigma.set_rotor_positions(positions)
                print("Rotors set up successfully!")

        elif choice == '2':
            pair = input("Enter plugboard pair (e.g., 'AB'): ").upper()
            enigma.add_plugboard_pair(pair)

        elif choice == '3':
            enigma.view_plugboard()

        elif choice == '4':
            char_to_remove = input("Enter the character to remove from plugboard pair: ").upper()
            enigma.remove_plugboard_pair(char_to_remove)

        elif choice == '5':
            if not enigma.rotors:
                print("Please set up rotors first.")
                continue

            message = input("Enter the message to encrypt: ").upper()
            encrypted_message = enigma.encrypt(message)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '6':
            if not enigma.rotors:
                print("Please set up rotors first.")
                continue

            message = input("Enter the message to decrypt: ").upper()
            decrypted_message = enigma.decrypt(message)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '7':
            print("Exiting Enigma Machine... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
