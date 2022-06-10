import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 8080))
s.listen()

while True:
    connect, addr = s.accept()
    connect.send(b"You connected!")
    connect.close()
