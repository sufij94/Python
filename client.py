import socket

SER_ADDR = input("Enter server IP address: ")
SER_PORT = int(input("Enter server port: "))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SER_ADDR, SER_PORT))
print("Connecition Established")

message = input("Message to send: ")
my_sock.sendall(message.encode())
my_sock.close()
