from multiprocessing import Queue,Process
import os,time,random
from multiprocessing import Pool
import multiprocessing
src="F:/python/1.txt"

def proc_send(pipe,urls):
    for url in urls:
        print("Process %s send :%s"%(os.getpid(),url))
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print("process %s rev : %s "%(os.getpid(),pipe.recv()))
        time.sleep(random.random()) 
    
if __name__=='__main__':
    pipe=multiprocessing.Pipe()
    p1=multiprocessing.Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(10)]))
    p2=multiprocessing.Process(target=proc_recv,args=(pipe[1],))  #定义pipe的conn1和conn2
    p1.start()
    p2.start()
    p1.join()
    p2.join()