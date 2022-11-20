import socket
UDP_IP = "localhost"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("Input a command to run:") 
    if message.lower().strip()== 'exit':
        break
    sock.sendto(message.encode("utf-8"), (UDP_IP, UDP_PORT))
