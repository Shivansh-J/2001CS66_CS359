import socket
import sys

fake_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]  
port = int(sys.argv[2])

try:
    fake_client.connect((host, port))
    fake_client.close()
    c.connect((host, port))  
    print("Connected successfully to the server.")
except socket.error as message:
    print("Error found in connecting socket: " + str(message))
    exit(0)

while True:  
    inp = input("Enter mesage to be evaluated ")
    c.send(inp.encode())
    answer = c.recv(1024)
    print("Server replied: " + answer.decode())
    inp = input("Wanna move forward ? Y/N\n")
    if (inp == "N"):
        break

c.close()
