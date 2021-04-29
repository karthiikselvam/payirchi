import os
import socket

# Creating a socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 2222))
sock.listen(5)
print("Host Name: ", sock.getsockname())

# Accepting the connection.
client, addr = sock.accept()

# Getting file details.
file_name = input("File Name:")
file_size = os.path.getsize(file_name)

# Sending file_name and detail.
client.send(file_name.encode())
client.send(str(file_size).encode())

# Opening file and sending data.
with open(file_name, "rb") as file:
    c = 0

    # Running loop while c != file_size.
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)


# Cloasing the socket.
sock.close()