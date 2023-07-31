# WebServer-TCP-Socket-Programming
The basics of socket programming for TCP connections in Python: how to create a socket, bind it to a specific address and port, as well as send and receive an HTTP packet. You will also learn some basics of HTTP header format in Python3.

You will develop a web server that handles one HTTP request at a time. Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client.

Code
Attached you will find the skeleton code for the Web server. You are to complete the skeleton code. The places where you need to fill in code are marked with #Fill in start and #Fill in end. Each place may require one or more lines of code.

Part 1: Running the Server
Put the attached HTML file (named HelloWorld.html) in the same directory in which the server webserver.py runs. Run the server program. Determine the IP address of the host that is running the server (e.g., 128.238.251.26 or localhost). From another host, open a browser and provide the corresponding URL. For example: http://128.238.251.26:6789/HelloWorld.html. You can open a browser in the same host where the server runs and use the following http://localhost:6789/HelloWorld.html.

‘HelloWorld.html’ is the name of the file you placed in the server directory. Note also the use of the port number after the colon. You need to replace this port number with the port number that was assigned to you. In the above example, we have used port number 6789. The browser should then display the contents of HelloWorld.html. If you omit “:6789”, the browser will assume port 80 (why?), and you will get the web page from the server only if your server is listening at port 80.

Then try to get a file that is not present on the server (e.g., test.html). You should get a “404 File Not Found” message.
Skeleton Python Code
Skeleton Python Code for the Web Server is attached.

Part 2: The client program
Write your own HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. You can assume that the HTTP request sent is a GET method. The client should take command line arguments specifying the server IP address or hostname, the port at which the server is listening, and the HTTP file name (e.g., test.html or HelloWorld.html). The following is an input command format to run the client. webclient.py <server_host> <server_port> <filename>

E.g.,
python3 webclient.py localhost 6789 HelloWorld.html

Bonus Exercise (10%)
Currently, the webserver handles only one HTTP request at a time. Implement a multithreaded server that is capable of serving multiple requests simultaneously. Using threading, create a main thread in which your modified server listens for clients at a fixed port. When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread. There will be a separate TCP connection in a separate thread for each request/response pair.
