Author: Tobechi onwenu
Title: MultiThreadServer.py

Description:

This module implements a simple TCP socket server that can handle multiple concurrent connections. The server uses threads to handle each client connection.

Imports
The module imports the following modules:

socket: This module provides the socket class, which is used to create and manage sockets.
threading: This module provides the Thread class, which is used to create and manage threads.
Variables
The module defines the following variables:

IP: The IP address of the server. This can be set to 'localhost' to listen for connections on the local machine, or to a specific IP address to listen for connections from a specific machine.
PORT: The port number that the server listens on.
ADDR: A tuple of two integers, (IP, PORT), that represents the address and port number of the server.
SIZE: The size of the messages that are sent between the server and the clients.
FORMAT: The encoding that is used to encode and decode messages.
DISCONNECT_MSG: A string that represents the message that a client sends to disconnect from the server.
Functions
The module defines the following functions:

handle_client(): This function handles a single client connection. It receives messages from the client and sends them back. The function terminates when the client sends a message that matches the DISCONNECT_MSG constant.
main(): This function starts the server. It creates a socket object, binds it to the specified address and port, and then enters a loop that waits for client connections. When a client connects, the loop creates a new thread to handle the client connection.
Usage
To use the socket_server_with_threads.py module, you must first import it into your code. You can then start the server by calling the main() function. For example:

import socket_server_with_threads

socket_server_with_threads.main()

The `main()` function will print the following messages to the console:

[STARTING] Server is starting...
[LISTENING] Server is listening on port 56011

The server will then listen for client connections. When a client connects, the server will print the following message to the console:

[New Connection] Client connected from {}

The server will then enter a loop that receives messages from the client and sends them back. The loop will terminate when the client sends a message that matches the DISCONNECT_MSG constant. When the loop terminates, the server will print the following message to the console:

[Client disconnected]

Code snippet

The server will then close the socket and return.
