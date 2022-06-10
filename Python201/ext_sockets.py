import socket

"""
ip = socket.gethostbyname('247ctf.com')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 80))
s.sendall(b"HEAD / HTTP/1.1\r\nHost: 247ctf.com\r\n\r\n")
print(s.recv(1024).decode())
"""

for port in [22, 80, 139, 443, 445, 8080]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print("{} is open!".format(port))
    else:
        print("{} is closed!".format(port))
    
    s.close()
