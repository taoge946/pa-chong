import socket
import threading
import time

def dealclient(sock,addr):
    print('Accept new connection from %s:%s'%addr)
    sock.send(b'Hello I am server')
    while True:
        data=sock.recv(1024)#获取客户端所发送的数据
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':#若接收到的客户端所发的数据位'exit'则直接关闭连接
            break
        print('-->>%s!'%data.decode('utf-8'))
        sock.send(('lop_msg:%s!'%data.decode('utf-')).encode('utf-8'))
    sock.close()
    print('connetion from %s:%s closed'%addr)

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#建立TCPsocket
    s.bind(('192.168.1.109',9999))#绑定树莓派本机的IP作为服务器端,9999是端口号。
    s.listen(5)#.listen()使该socket处于监听链接请求的状态
    print('waiting for connection...')
    while True:
        sock,addr=s.accept()#接收一个新链接，sock为这次连接的套接字，addr为IP地址
        t=threading.Thread(target=dealclient,args=(sock,addr))#创建一个线程用来处理TCP链接
        t.start()