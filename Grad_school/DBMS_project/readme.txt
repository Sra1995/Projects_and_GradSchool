"""
CSC570 DataBase Management Systems
project - Programming Assignment 5
Programmer: Sajjad Alsaffar
Professor: Dr. Girard
Date created: 04/12/2024
Date of last modification: 04/28/2024
"""

Description:
    This program is a simple database management system that allows the user to interact with a database
    using a simple command line interface. The program allows the user to insert data into a table, delete data from a table, update data in a table.
    The program uses MySQL as the database management system.

How to run:
1. run the server.py first then the planet_editor.py. 
    -   if you ran planet_editor.py that is fine but you will need to click refresh to connect to the server.
    -   the server will display messages to show that it is running and connected to the database and to make it easy to see what is going on.
    -   the planet_editor.py will display a window with a table that will show the data in the database.


Notes:
    - I have attached screenshots to showcase that the program as intended for my part which is display 2/part II display the planets.



SQL Injection Prevention in the Code

Overview:
The code is designed to prevent SQL injection attacks, a common security vulnerability in database applications. It achieves this through the following mechanisms:

1. Parameterized Queries (Prepared Statements):
   - All SQL queries executed by the program utilize parameterized queries, also known as prepared statements.
   - Parameterized queries separate SQL code from user input, preventing malicious input from altering the query's logic.

2. Parameterized Cursor Initialization:
   - When creating cursor objects for executing SQL queries, the code sets 'prepared=True'.
   - This parameterized cursor initialization ensures that the cursor supports parameterized queries, enabling safe handling of user input.

Example:
Suppose a client sends input containing a potential SQL injection attempt:
input_request = "DELETE_PLAYER '; DROP TABLE planet; --"
The program safely handles this request using parameterized queries, mitigating the risk of SQL injection attacks.

Key Points:
- Parameterized queries prevent SQL injection attacks by treating user input as data rather than executable SQL code.
- Setting 'prepared=True' when initializing cursor objects ensures support for parameterized queries, enhancing the security of database operations.
- By utilizing parameterized queries throughout the code, the program effectively guards against SQL injection vulnerabilities.
