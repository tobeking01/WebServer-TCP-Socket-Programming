import socket
import sys

def http_client(server_host, server_port, filename):

    # Create a TCP socket
    client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        client_socket .connect((server_host, server_port))

        # Send the HTTP request
        request = "GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n" % (filename, server_host)
        client_socket .sendall(request.encode())

        # Receive the HTTP response
        response = client_socket .recv(4096).decode()

        # Print the HTTP response
        print(response)
    except socket.error as e:
        print("Error")
    finally:
         # Close socket
        client_socket.close()

# Check if the script is run with the correct number of command line arguments
if len(sys.argv) != 4:
    print("Usage: python webclient.py server_host server_port filename")
else:
    # Parse the command line arguments
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

http_client(server_host, server_port, filename)
