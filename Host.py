import socket
import multiprocessing
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            clientconn, clientadd = s.accept()
            with clientconn:
                print(f"Connected by {clientadd}")
                while True: 
                    datatosend = input("=>")
                    clientconn.sendall(datatosend.encode())
                    result = clientconn.recv(4084)
                    print(result.decode())
main()
