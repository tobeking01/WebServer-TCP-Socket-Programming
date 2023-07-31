Author: Tobechi onwenu
Title: MultiThreadClient.py

Description:

socket_client.py
This module implements a simple TCP socket client that connects to a server on the specified IP address and port. The client sends messages to the server and receives messages back.

Imports
The module imports the following modules:

socket: This module provides the socket class, which is used to create and manage sockets.
Variables
The module defines the following variables:

IP: The IP address of the server. This can be set to 'localhost' to connect to the server on the local machine, or to a specific IP address to connect to a specific server.
PORT: The port number that the server listens on.
ADDR: A tuple of two integers, (IP, PORT), that represents the address and port number of the server.
SIZE: The size of the messages that are sent between the client and the server.
FORMAT: The encoding that is used to encode and decode messages.
DISCONNECT_MSG: A string that represents the message that the client sends to disconnect from the server.
Functions
The module defines the following functions:

main(): This function starts the client. It creates a socket object, connects it to the specified address and port, and then enters a loop that sends messages to the server and receives messages back. The loop terminates when the client sends a message that matches the DISCONNECT_MSG constant.
Usage
To use the socket_client.py module, you must first import it into your code. You can then start the client by calling the main() function. For example:

import socket_client

socket_client.main()

Code snippet

The `main()` function will print the following messages to the console:

Use code with caution. Learn more
[CONNECTED] Client connected to server at port {}: {}

The client will then enter a loop that sends messages to the server and receives messages back. The user can enter messages to send to the server by typing them into the console. The server will then print the messages that the client sends to it. The loop will terminate when the client sends a message that matches the DISCONNECT_MSG constant. When the loop terminates, the client will print the following message to the console:

[DISCONNECTED] Client disconnected from server
The client will then close the socket and return.
