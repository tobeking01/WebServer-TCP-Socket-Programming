Author: Tobechi onwenu
Title. WebClient.py

Description:

To use the webclient.py module, you must first import it into your code. You can then run the module by passing the three required arguments as command line arguments. For example:

python webclient.py localhost 80 index.html

The webclient.py module will connect to the server localhost on port 80 and retrieve the file index.html. The module will then print the HTTP response.
This module implements a simple HTTP client that can be used to retrieve files from a remote server. The client takes three command line arguments:

server_host: The hostname or IP address of the server.
server_port: The port number of the server.
filename: The name of the file to retrieve.
The client will connect to the server, send an HTTP GET request for the specified file, and then print the HTTP response.

Imports
The module imports the following modules:

socket: This module provides the socket class, which is used to create and manage sockets.
sys: This module provides the argv variable, which contains the command line arguments.
Functions
The module defines the following functions:

http_client(): This function is the main function of the module. It takes three arguments: the server host, the server port, and the filename. The function connects to the server, sends an HTTP GET request for the specified file, and then prints the HTTP response.

