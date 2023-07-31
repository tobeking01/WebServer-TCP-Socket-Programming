# import socket module
from socket import *
import sys  # In order to terminate the program

# AF_INET = ipv4, SOCK_STREAM = TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# print("Socket Created!!")
# Prepare a sever socket
# Fill in start
serverHost = "localhost"
serverPort = 56011
# Bind host and port to socket
serverSocket.bind((serverHost, serverPort))
# Listen to the server
serverSocket.listen(5)
# print('Socket now listening')
# Fill in end
while True:
    # accept information from address
    # clientSocket, address = socket.accept()

    # Establish the connection
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    # print('Source address is:' + str(addr))
    # confirm establishment
    # print(f"Connection from {addr} has been established!")
    # print('The server is ready to receive')
    try:
        # Receive message from the socket
        message = connectionSocket.recv(4096)  # Fill in start #Fill in end
        print("****** Message ******")
        # print('Socket message is:', message.split()[0], message.split()[1])
        print('Message is:' + str(message))
        # obtain the file name carried by the HTTP request message
        filename = message.split()[1]
        # print("****** filename ******")
        # print('Filename is:' + str(filename))
        f = open(filename[1:], 'rb')
        outputData = f.readlines()
        # print("****** outputData ******")
        # print(outputData)
        # Send the HTTP response header line to the socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\n\n".encode())
        connectionSocket.send("\n".encode())
        # Fill in end
        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i])
        connectionSocket.send("\n".encode())
        connectionSocket.close()
        print("Connection closed!")
    except IOError:
        # Send HTTP response code and message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 File Not Found\n".encode())
        connectionSocket.send("Content-Type: text/html\n".encode())
        connectionSocket.send("\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 File Not Found</h1></body></html><\n>".encode())

# Close the client connection socket
serverSocket.close()


sys.exit()  # Terminate the program after sending the corresponding data
