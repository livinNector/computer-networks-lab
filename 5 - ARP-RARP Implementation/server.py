import socket
UDP_IP = "localhost"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
ip=["172.16.1.9","172.16.1.8"]
mac=["6A:08:AA:C2","8A:BC:E3:FA"]
arp = dict(zip(ip,mac))
while True:
    data, addr = sock.recvfrom(1024)
    ip_addr = data.decode('utf-8')
    if data: break
    
print("Received message:",ip_addr)
print("the MAC address is: ",arp[ip_addr])
