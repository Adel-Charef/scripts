import socket
import requests
import sys
import ipaddress

public = "http://httpbin.org/ip"
ip_api = "http://ip-api.com/json/{0}"

static_ip = socket.gethostbyname(socket.gethostname())
public_ip = requests.get(public).json()['origin']


def ip_valid(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False


try:
    ip = str(sys.argv[1])
    if not ip_valid(ip):
        ip = socket.gethostbyname(ip)
except IndexError:
    ip = static_ip


def main(ip):
    print("Static Ip Address:", static_ip)
    print("Public Ip Address:", public_ip)

    data = requests.get(ip_api.format(ip)).json()

    for d in data:
        print(d, ":", data[d])
    print()


if __name__ == "__main__":
    main(ip)
