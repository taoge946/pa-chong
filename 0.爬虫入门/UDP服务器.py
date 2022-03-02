import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.1.109',9999))#链接指定IP的服务器
print('BInd UDP server on 9999...')
while True:
    data,addr=s.recvfrom(1024)
    print('Receive From:%s:%s'%addr)
    s.sendto(b'hello!%s' % data ,addr)