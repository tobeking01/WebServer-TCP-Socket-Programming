import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 56011
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print("[CONNECTED] Client connected to server at port {}:".format(PORT))

    connected = True
    while connected:
        msg = input("Please enter a message (string in quotes): ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print("[SERVER] message is: {}".format(msg))

if __name__ == "__main__":
    main()
