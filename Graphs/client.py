# This file will be used for recieving files over socket connection.
import os
import socket

host = input("Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying to connect to socket.
sock.connect((host, 2222))
print("Connected Successfully")

# Send file details.
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

# Opening and reading file.
with open("./rec/" + file_name, "wb") as file:
    c = 0

    # Running the loop while file is recieved.
    while c <= int(file_size):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)



# Closing the socket.
sock.close()