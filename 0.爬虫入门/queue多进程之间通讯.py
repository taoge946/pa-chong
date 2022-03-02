from multiprocessing import Queue,Process
import os,time,random
from multiprocessing import Pool
src="F:/python/1.txt"

def proc_write(q,urls):
    print("Process %s is writing.."%os.getpid())
    for url in urls:
        q.put(url)
        print("Put %s to queue.."%url)
        time.sleep(random.random())

def proc_read(q):
    print("Process %s is reading .."%os.getpid())
    while True:
        url=q.get(True)
        print("get %s in queue"%url)



if __name__=='__main__':
    q=Queue() #在父进程中创建queue
    proc_writer1=Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
    proc_writer2=Process(target=proc_write,args=(q,['url_4','url_5','url_6']))
    proc_reader1=Process(target=proc_read,args=(q,))
    proc_writer1.start()
    proc_writer2.start()#启动写的子进程
    proc_reader1.start()#启动读的子进程

    proc_writer1.join()
    proc_writer2.join()#等待proc——write结束

    proc_reader1.terminate()#因为是死循环无法等待结束只能强行终止
    
    

