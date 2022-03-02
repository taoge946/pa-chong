import threading
import random,time
mylock=threading.RLock()
num=0

class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)
    def run(self):
        global num
        while True:
            mylock.acquire()
            print("%s locked,number= %d "%(threading.current_thread().name,num))
            if num>=4:
                mylock.release()
                print("%s release,number= %d "%(threading.current_thread().name,num))
                break
            num+=1
            print("%s release,number= %d "%(threading.current_thread().name,num))
            mylock.release()



if __name__=='__main__':
    print('%s is running ..'%threading.current_thread().name)
    t1=myThread('thread1')
    t2=myThread('thread2')
    t1.start()
    t2.start()