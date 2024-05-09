import socket

from _datetime import datetime

targetIP = input("Enter the target IP address: ")


def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"scanning the target{ip}")
        print(f"Start: {datetime.now()}")

        for port in range(0,90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0: # i.e no error
                print(f"Port {port} is Open")
            sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Could not connect to the server")


port_scan(targetIP)
