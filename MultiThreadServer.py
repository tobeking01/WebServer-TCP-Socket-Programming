import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 56011
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr):
    print("[New Connection] {} Connected.".format(addr))

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        print("[addr] {} connected.".format(addr))
        print("[msg] {} connected.".format(msg))
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(2)
    print("[LISTENING] Server is listening on port {} Connected".format(PORT))

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()

