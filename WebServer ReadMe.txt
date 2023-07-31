
Author: Tobechi onwenu
Title. WebServer.py

Description:
This module implements a simple HTTP server that serves static files from a specified directory. The server listens on the specified port and returns the requested file if it exists, or a 404 error if the file does not exist.

Imports
The module imports the following modules:

socket: This module provides the socket class, which is used to create and manage sockets.
sys: This module provides the exit() function, which is used to terminate the program.
Variables
The module defines the following variables:

serverHost: The hostname or IP address of the server. This can be set to 'localhost' to listen for connections on the local machine, or to a specific IP address to listen for connections from a specific machine.
serverPort: The port number that the server listens on.
root: The directory that contains the static files that the server will serve.
Functions
The module defines the following functions:

main(): This function starts the server. It creates a socket object, binds it to the specified port, and then enters a loop that waits for client connections. When a client connects, the loop calls the handle_client() function to handle the client connection.
handle_client(): This function handles a single client connection. It receives a HTTP request from the client and returns the requested file if it exists, or a 404 error if the file does not exist.
Usage
To use the simple_http_server module, you must first import it into your code. You can then start the server by calling the main() function. For example:

import simple_http_server

simple_http_server.main()

The `main()` function will print the following messages to the console:

[STARTING] Server is starting...
[LISTENING] Server is listening on port 56011

The server will then listen for client connections. When a client connects, the server will print the following message to the console:

[New Connection] Client connected from {}

The server will then send the requested file to the client. If the file does not exist, the server will send a 404 error to the client.

