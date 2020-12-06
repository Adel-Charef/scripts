import socket

server = socket.socket()
host = ""

req = """
put the Request Header and the form
"""

server.connect((host, 80))
server.send(req.encode('UTF-8'))
print(server.recv(1024).decode('UTF-8'))
