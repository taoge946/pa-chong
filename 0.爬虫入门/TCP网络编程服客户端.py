import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.109',9999))#链接指定IP的服务器
print('-->>'+s.recv(1024).decode('utf-8'))
s.send(b'Hello i am client!')#这个b必须有，不然会报错
print('-->>'+s.recv(1024).decode('utf-8'))
s.send(b'exit')#在服务器端规定了只要收到exit就关闭连接
s.close()