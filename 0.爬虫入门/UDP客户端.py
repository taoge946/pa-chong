import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'hello',b'world']:
    s.sendto(data,('192.168.1.109',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()