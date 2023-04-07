import socket
import sys


def create_socket():
    try:
        global host  
        global port  
        global s  
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
    except socket.error as message:
        print("Socket Creation Error: " + str(message))
        exit(0)


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))
        s.bind((host, port))
        s.listen(0)  
    except socket.error as message:
        print("Socket Binding Error: " + str(message))
        exit(0)


def calculate(message):
    try:
        result = eval(str(message))  
    except:
        result = "Please enter a valid expression."
    return result


def socket_accept():
    global address
    connection, address = s.accept()  
    print("Connection has been established with " +
          address[0] + ":" + str(address[1]))
    send_commands(connection)
    connection.close()
    print("Connection has been closed with " +
          address[0] + ":" + str(address[1]))


def send_commands(connection):
    while True:  
        data = connection.recv(1024)  
        if not data:
            break
        message = data.decode()  
        result = calculate(message)
        print("Equation received [" + message + "] from " +
              address[0] + ":" + str(address[1]))
        output = str(result)
        connection.send(output.encode())  
        print("Result sent to " + address[0] + ":" + str(address[1]))


def main():
    create_socket()
    bind_socket()
    while 1:  
        socket_accept()


if __name__ == "__main__":
    main()
