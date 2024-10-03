"""
CSC570 DataBase Management Systems
project - Programming Assignment 5
Programmer: Sajjad Alsaffar
Professor: Dr. Girard
Date created: 04/12/2024
Date of last modification: 04/28/2024
"""

import socket                                                                                                                   # Import socket module
import mysql.connector                                                                                                          # Import mysql.connector module
from mysql.connector import Error                                                                                               # Import Error module

                                                                                                                                # Database configuration 
DB_CONFIG = {
    "host": "",# removed it for security reasons
    "user": "",# removed it for security reasons
    "passwd": "",# removed it for security reasons
    "database": "" # removed it for security reasons
}

class DatabaseConnector:                                                                                                        # DatabaseConnector class
    def __init__(self):                                                                                                         # Constructor
        self.connection = None                                                                                                  # Initialize connection to None

    def connect(self):                                                                                                          # Connect method
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)                                                              # Connect to the database using the configuration
            print("Database connection established.")                                                                           # Print message to indicate successful connection
        except Error as e:                                                                                                      # Catch any errors
            print(f"Database connection error: {e}")                                                                            # Print error message

    def execute_query(self, query, params=None):                                                                                # Execute_query method
        try:
            cursor = self.connection.cursor(prepared=True)                                                                      # Create a cursor object
            print(f"Executing query: {query} with parameters: {params}")                                                        # Debugging line
            cursor.execute(query, params)                                                                                       # Execute the query
            return cursor.fetchall()                                                                                            # Return the result of the query
        except Error as e:                                                                                                      # Catch any errors
            print(f"Error executing query: {e}")                                                                                # Print error message
            return None                                                                                                         # Return None if an error occurs

    def commit_changes(self):                                                                                                   # Commit_changes method
        try:
            self.connection.commit()                                                                                            # Commit the changes
            print("Changes committed successfully.")                                                                            # Print message to indicate successful commit
        except Error as e:                                                                                                      # Catch any errors
            print(f"Error committing changes: {e}")                                                                             # Print error message


    def close(self):                                                                                                            # Close method
        if self.connection:                                                                                                     # Check if the connection is not None
            self.connection.close()                                                                                             # Close the connection
            print("Database connection closed.")                                                                                # Print message to indicate successful closure

def sanitize_input(input_str):                                                                                                  # Sanitize_input function
    return input_str.strip()                                                                                                    # Strip any leading or trailing whitespace


def handle_request(request, db_connector):                                                                                      # Handle_request function
    sanitized_request = sanitize_input(request)                                                                                 # Sanitize the input request
    parts = sanitized_request.split(maxsplit=1)                                                                                 # Split the request into two parts
    action = parts[0].upper()                                                                                                   # Convert the first part to uppercase
    params = parts[1] if len(parts) > 1 else ""                                                                                 # Get the second part if it exists, otherwise set it to an empty string

    if action == "GET_ALL_PLANETS":                                                                                             # Check if the action is GET_ALL_PLANETS
        query = "SELECT * FROM planet"                                                                                          # Define the query
        result = db_connector.execute_query(query)                                                                              # Execute the query
        if result:                                                                                                              # Check if the result is not None
            return "\n".join(map(str, result))                                                                                  # Return the result as a string
        else:                                                                                                                   # If the result is None
            return "No planets found."                                                                                          # Return a message indicating no planets were found

    elif action.startswith("ADD_PLANET"):                                                                                       # Check if the action starts with ADD_PLANET
        parts = [p.strip("',()") for p in params.split()]                                                                       # Split the parameters and strip any unwanted characters
        planet_id = int(parts[0])                                                                                               # Extract the planet_id correctly
        planet_name = parts[1]                                                                                                  # Extract the planet_name correctly
        location = parts[2]                                                                                                     # Extract the location correctly
        owner_id = int(parts[3])                                                                                                # Extract the owner_id correctly
        query = "INSERT INTO planet (id, planet_name, location, owner) VALUES (?, ?, ?, ?)"                                     # Define the query
        db_connector.execute_query(query, (planet_id, planet_name, location, owner_id))                                         # Execute the query
        db_connector.commit_changes()                                                                                           # Commit the changes
        return "Planet added successfully."                                                                                     # Return a message indicating the planet was added successfully
    
    elif action.startswith("DELETE_PLAYER"):                                                                                    # Check if the action starts with DELETE_PLAYER
        owner_id = params.strip()                                                                                               # Extract the owner_id correctly
        query = "DELETE FROM player WHERE id = ?"                                                                               # Define the query
        db_connector.execute_query(query, (owner_id,))                                                                          # Execute the query
        db_connector.commit_changes()                                                                                           # Commit the changes
        return "Player and related planets deleted successfully."                                                               # Return a message indicating the player and related planets were deleted successfully



    elif action.startswith("UPDATE_PLANET"):                                                                                    # Check if the action starts with UPDATE_PLANET
        parts = [p.strip() for p in params.split(',')]                                                                          # Split the parameters and strip any unwanted characters
        planet_id = int(parts[0].split()[0].strip("('"))                                                                        # Extract the planet_id correctly
        new_name = parts[1].strip("'")                                                                                          # Extract the new_name correctly
        new_location = parts[2].strip("'")                                                                                      # Extract the new_location correctly
        new_owner_id = int(parts[3].strip("')"))                                                                                # Extract the new_owner_id correctly
        query = "UPDATE planet SET planet_name = ?, location = ?, owner = ? WHERE id = ?"                                       # Define the query
        db_connector.execute_query(query, (new_name, new_location, new_owner_id, planet_id))                                    # Execute the query
        db_connector.commit_changes()                                                                                           # Commit the changes
        return "Planet updated successfully."                                                                                   # Return a message indicating the planet was updated successfully



    elif action.startswith("DELETE_PLANET"):                                                                                    # Check if the action starts with DELETE_PLANET
        planet_id = params.strip()                                                                                              # Extract the planet_id correctly
        query = "DELETE FROM planet WHERE id = ?"                                                                               # Define the query
        print(f"Executing query: {query} with parameters: {planet_id}")                                                         # Debugging line
        result = db_connector.execute_query(query, (planet_id,))                                                                # Execute the query
        if result is None:                                                                                                      # Check if the result is None
            print("Delete query failed.")                                                                                       # Debugging line
        else:                                                                                                                   # If the result is not None
            db_connector.commit_changes()                                                                                       # Commit the changes
        return "Planet deleted successfully."                                                                                   # Return a message indicating the planet was deleted successfully


    else:                                                                                                                       # If the action is not recognized
        return "Invalid request. Supported actions: GET_ALL_PLANETS, ADD_PLANET, UPDATE_PLANET, DELETE_PLANET"                  # Return a message indicating the request is invalid


def server_program():                                                                                                           # Server_program function
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                            # Create a socket object
    try:
        serversocket.bind(('localhost', 8089))                                                                                  # Bind the socket to the address and port
        serversocket.listen(5)                                                                                                  # Listen for incoming connections
        print("Server is listening on port 8089")                                                                               # Print message to indicate the server is listening
    except socket.error as e:                                                                                                   # Catch any errors
        print(f"Socket error: {e}")                                                                                             # Print error message
        return

    db_connector = DatabaseConnector()                                                                                          # Create a DatabaseConnector object
    db_connector.connect()                                                                                                      # Connect to the database

    while True:                                                                                                                 # Infinite loop to keep the server running
        try:
            connection, address = serversocket.accept()                                                                         # Establish a connection with the client
            print(f"Connection established with {address}")                                                                     # Print message to indicate successful connection
            while True:                                                                                                         # Infinite loop to keep the connection open
                buf = connection.recv(1024)                                                                                     # Receive data from the client
                if len(buf) > 0:                                                                                                # Check if the data is not empty
                    sanitized_request = sanitize_input(buf.decode())                                                            # Sanitize the input
                    response = handle_request(sanitized_request, db_connector)                                                  # Handle the request
                    connection.send(response.encode())                                                                          # Encode and Send the response to the client
                else:                                                                                                           # If the data is empty
                    break                                                                                                       # Break the loop
        except Error as e:                                                                                                      # Catch any errors
            print(f"Error: {e}")                                                                                                # Print error message for database errors
            break
        except socket.error as e:                                                                                               # Catch any errors
            print(f"Socket error: {e}")                                                                                         # Print error message for socket errors
            break

    db_connector.close()                                                                                                        # Close the database connection

if __name__ == "__main__":                                                                                                      # Check if the script is being run directly
    server_program()                                                                                                            # Run the server program
