from queue import Queue
import socket
import threading

target = "127.0.0.1"
queue = Queue()
open_ports = []
"""
 port 80 (HTTP) or port 443 (HTTPS) 21 (FTP), 22 (SSH), 25 (SMTP)
"""
# connect to a target on a specific port


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def get_ports(mode):
    # for standardized ports
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    # for reserved ports
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    # for the most important ports only
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    # to choose our ports manually
    elif mode == 4:
        ports = input("Enter your ports (separate by blank): ")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)


# get the port numbers from the queue, scan them and print the results
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open!")
            open_ports.append(port)
        else:
            print(f"Port {port} is closed!")


# let's create start and manage our threads
def main(threads, mode):
    get_ports(mode)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    print("The open ports are: ", open_ports)


if __name__ == "__main__":
    main(100, 1)
