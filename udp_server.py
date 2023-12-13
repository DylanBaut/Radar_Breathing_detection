import socket

# Binding to 0.0.0.0 allows UDP connections to any address
# that the device is using
#change these to match breathing/not_breathing.py 
UDP_IP = "0.0.0.0"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Use Internet socket family
                     socket.SOCK_DGRAM) # Use UDP packets
addr = (UDP_IP, UDP_PORT)

sock.bind(addr)
print('Socket is bound to', addr)

while True:
    data, addr = sock.recvfrom(1024)    
    print('Received message:', data)
