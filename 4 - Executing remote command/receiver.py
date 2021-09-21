
import socket
import subprocess
UDP_IP = "localhost"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT)) #
while True:
    data = sock.recv(1024)
    if not data:
        print("Exiting...")
        break
    command=data.decode("utf-8")
    print("Executing ", command)
    subprocess.run(command.split())
