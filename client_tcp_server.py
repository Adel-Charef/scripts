#! /usr/bin/python3
# trying to esablish a connection with client

import socket


s = socket.socket()
host = socket.gethostname()
port = 1245
s.bind((host, port))

s.listen()
while True:
    c, addr = s.accept()
    print("Got a connection from",addr)
    c.send(b"Thank you for connecting")
    c.close()

