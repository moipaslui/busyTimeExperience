import socket

HOST = "127.0.0.1"
PORT = 4545

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))
c.send("Bonjoure\n")
from_server = c.recv(4096)

c.close()
print(from_server)