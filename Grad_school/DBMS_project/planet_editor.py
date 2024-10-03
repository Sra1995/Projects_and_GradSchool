"""
CSC570 DataBase Management Systems
project - Programming Assignment 5
Programmer: Sajjad Alsaffar
Professor: Dr. Girard
Date created: 04/12/2024
Date of last modification: 04/28/2024
"""

import sys                                                                                                                                                  # import sys for sys.exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel, QDialog, QFormLayout # import required classes
import socket                                                                                                                                               # import socket module
from PyQt5.QtGui import QIcon                                                                                                                               # import QIcon for adding icons to buttons

class PlanetEditor(QMainWindow):                                                                                # Create a class for the main window
    def __init__(self):
        super().__init__()                                                                                      # Call the parent class constructor
        self.setWindowTitle("Planet Editor")                                                                    # Set the window title
        self.setGeometry(100, 100, 400, 300)                                                                    # Set the window default geometry it can be resized as needed

                                                                                                                # Create a central widget
        central_widget = QWidget(self)                                                                          # Create a central widget
        self.setCentralWidget(central_widget)                                                                   # Set the central widget

                                                                                                                # Create a vertical layout
        layout = QVBoxLayout(central_widget)

                                                                                                                # Create buttons
        self.add_button = QPushButton(QIcon("add_icon.png"), "Add Planet", self)                                # Add button
        self.update_button = QPushButton(QIcon("edit_icon.png"), "Update Planet", self)                         # update button
        self.delete_button = QPushButton(QIcon("delete_icon.png"), "Delete Planet", self)                       # Delete button
        self.refresh_button = QPushButton(QIcon("refresh_icon.png"), "Refresh", self)                           # refresh button

                                                                                                                # Create a horizontal layout for buttons instead of being vertical 
        button_layout = QHBoxLayout()                                                                           # Create a horizontal layout
        button_layout.addWidget(self.add_button)                                                                # Add the add button
        button_layout.addWidget(self.update_button)                                                             # Add the update button
        button_layout.addWidget(self.delete_button)                                                             # Add the delete button
        button_layout.addWidget(self.refresh_button)                                                            # Add the refresh button

        layout.addLayout(button_layout)                                                                         # Add the button layout to the main layout

                                                                                                                # Create a list widget to display planet names
        self.planet_list = QListWidget(self)                                                                    # Create a list widget
        layout.addWidget(self.planet_list)                                                                      # Add the list widget to the main layout

                                                                                                                # Connect buttons to actions
        self.add_button.clicked.connect(self.add_planet)                                                        # Connect the add button to the add_planet method
        self.update_button.clicked.connect(self.update_planet)                                                  # Connect the update button to the update_planet method
        self.delete_button.clicked.connect(self.delete_planet)                                                  # Connect the delete button to the delete_planet method
        self.refresh_button.clicked.connect(self.retrieve_planets)                                              # Connect to retrieve_planets

                                                                                                                # Initialize planets (retrieve from server)
        self.retrieve_planets()

    def retrieve_planets(self):                                                                                 # Create a method to retrieve planets from the server
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:                            # Create a socket object
                client_socket.connect(('localhost', 8089))                                                      # Connect to the server
                client_socket.sendall(b"GET_ALL_PLANETS")                                                       # Send a request to the server to get all planets
                response = client_socket.recv(1024).decode()                                                    # Receive the response from the server and decode it
                planets = response.split("\n")                                                                  # Split the response into a list of planets
                self.planet_list.clear()                                                                        # Clear existing list
                self.planet_list.addItems(planets)                                                              # Add the planets to the list widget
        except Exception as e:                                                                                  # If an error occurs, print the error
            print(f"Error retrieving planets: {e}")

    def add_planet(self):                                                                                       # Create a method to add a planet
        dialog = PlanetDialog(self)                                                                             # Create a dialog to get planet details
        if dialog.exec_():                                                                                      # If the dialog is accepted
            new_planet = dialog.get_values()                                                                    # Get the values from the dialog and store them in new_planet
            if new_planet:                                                                                      # If new_planet is not empty
                request = f"ADD_PLANET {new_planet[0]}, {new_planet[1]}, {new_planet[2]}, {new_planet[3]}"      # Create a request to add the planet
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:                    # Create a socket object
                        client_socket.connect(('localhost', 8089))                                              # Connect to the server
                        client_socket.sendall(request.encode())                                                 # encode and Send the request to the server
                        response = client_socket.recv(1024).decode()                                            # Receive the response from the server and decode it
                        if response == "Planet added successfully.":                                            # If the response is "Planet added successfully."
                            self.planet_list.addItem(', '.join(new_planet))                                     # Add the new planet to the list widget
                        else:                                                                                   # If the response is not "Planet added successfully."
                            print(f"Error adding planet: {response}")                                           # Print an error message
                except Exception as e:                                                                          # If an error occurs, print the error
                    print(f"Error adding planet: {e}")


    def update_planet(self):                                                                                    # Create a method to update a planet
        selected_item = self.planet_list.currentItem()                                                          # Get the currently selected item
        if selected_item:                                                                                       # If an item is selected
            dialog = PlanetDialog(self, selected_item.text().split(', '))                                       # Create a dialog to get planet details
            if dialog.exec_():                                                                                  # If the dialog is accepted
                updated_planet = dialog.get_values()                                                            # Get the values from the dialog and store them in updated_planet
                if updated_planet:                                                                              # If updated_planet is not empty
                    request = f"UPDATE_PLANET {updated_planet[0]}, {updated_planet[1]}, {updated_planet[2]}, {updated_planet[3]}"               # Create a request to update the planet
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:                # Create a socket object
                            client_socket.connect(('localhost', 8089))                                          # Connect to the server
                            client_socket.sendall(request.encode())                                             # encode and Send the request to the server
                            response = client_socket.recv(1024).decode()                                        # Receive the response from the server and decode it
                            if response == "Planet updated successfully.":                                      # If the response is "Planet updated successfully."
                                selected_item.setText(', '.join(updated_planet))                                # Update the selected item with the new planet details
                            else:                                                                               # If the response is not "Planet updated successfully."
                                print(f"Error updating planet: {response}")
                    except Exception as e:                                                                      # If an error occurs, print the error
                        print(f"Error updating planet: {e}")

    def delete_planet(self):                                                                                    # Create a method to delete a planet
        selected_item = self.planet_list.currentItem()                                                          # Get the currently selected item
        if selected_item:                                                                                       # If an item is selected
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:                        # Create a socket object
                    client_socket.connect(('localhost', 8089))                                                  # Connect to the server
                    planet_id = int(selected_item.text().split(',')[0].strip('()'))                             # Correctly extract the planet_id
                    request = f"DELETE_PLANET {planet_id}"                                                      # Create a request to delete the planet
                    client_socket.sendall(request.encode())                                                     # encode and Send the request to the server
                    response = client_socket.recv(1024).decode()                                                # Receive the response from the server and decode it
                    if response == "Planet deleted successfully.":                                              # If the response is "Planet deleted successfully."
                        self.planet_list.takeItem(self.planet_list.row(selected_item))                          # Remove the selected item from the list widget
                    else:                                                                                       # If the response is not "Planet deleted successfully."
                        print(f"Error deleting planet: {response}")
            except Exception as e:                                                                              # If an error occurs, print the error
                print(f"Error deleting planet: {e}")







class PlanetDialog(QDialog):                                                                                    # Create a class for the dialog window
    def __init__(self, parent=None, default_values=None):                                                       # Create a constructor for the dialog window
        super().__init__(parent)                                                                                # Call the parent class constructor
        self.setWindowTitle("Planet Details")                                                                   # Set the window title
        self.setGeometry(100, 100, 200, 200)                                                                    # Set the window default geometry it can be resized as needed

                                                                                                                # Create a form layout
        form_layout = QFormLayout(self)

                                                                                                                # Create input fields for adding/editing planets
        self.planet_id_input = QLineEdit(self)                                                                  # Create a QLineEdit widget for the planet ID
        self.planet_name_input = QLineEdit(self)                                                                # Create a QLineEdit widget for the planet name
        self.planet_location_input = QLineEdit(self)                                                            # Create a QLineEdit widget for the planet location
        self.planet_owner_id_input = QLineEdit(self)                                                            # Create a QLineEdit widget for the planet owner ID
        form_layout.addRow("ID:", self.planet_id_input)                                                         # Add the input fields to the form layout
        form_layout.addRow("Planet Name:", self.planet_name_input)                                              # Add the input fields to the form layout
        form_layout.addRow("Location:", self.planet_location_input)                                             # Add the input fields to the form layout
        form_layout.addRow("Owner ID:", self.planet_owner_id_input)                                             # Add the input fields to the form layout

                                                                                                                # Set default values
        if default_values:                                                                                      # If default values are provided
            self.planet_id_input.setText(default_values[0])                                                     # Set the default values in the input fields
            self.planet_name_input.setText(default_values[1])                                                   # Set the default values in the input fields
            self.planet_location_input.setText(default_values[2])                                               # Set the default values in the input fields
            self.planet_owner_id_input.setText(default_values[3])                                               # Set the default values in the input fields

                                                                                                                # Create buttons
        self.add_button = QPushButton("Add", self)                                                              # Create a QPushButton widget for the add button
        self.cancel_button = QPushButton("Cancel", self)                                                        # Create a QPushButton widget for the cancel button

                                                                                                                # Connect buttons to actions
        self.add_button.clicked.connect(self.accept)                                                            # Connect the add button to the accept method
        self.cancel_button.clicked.connect(self.reject)                                                         # Connect the cancel button to the reject method

                                                                                                                # Add buttons to layout
        button_layout = QHBoxLayout()                                                                           # Create a horizontal layout for the buttons
        button_layout.addWidget(self.add_button)                                                                # Add the add button to the layout
        button_layout.addWidget(self.cancel_button)                                                             # Add the cancel button to the layout
        form_layout.addRow(button_layout)                                                                       # Add the button layout to the form layout

    def get_values(self):                                                                                       # Create a method to get the values from the input fields
        return (self.planet_id_input.text(), self.planet_name_input.text(), self.planet_location_input.text(), self.planet_owner_id_input.text())       # Return the values from the input fields as a tuple



if __name__ == "__main__":                                                                                     # If the script is run directly
    app = QApplication(sys.argv)                                                                               # Create an application instance
    window = PlanetEditor()                                                                                    # Create an instance of the main window
    window.show()                                                                                              # Show the main window
    sys.exit(app.exec_())                                                                                      # Execute the application
