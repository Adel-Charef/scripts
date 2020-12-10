import getpass
import telnetlib
import os

# This script can change the hostname of a switch

HOST = "IP_ADDRESS"
user = input("Enter username: ")
password = getpass.getpass("Enter Password: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"PASSWORD\n")
tn.write(b"conf t\n")
tn.write(b"hostname ANOTHERNAME\n")
tn.write(b"exit\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
