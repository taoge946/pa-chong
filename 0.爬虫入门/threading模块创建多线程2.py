import threading
import random,time


class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls=urls
    def run(self):
        print("current %s is running..."%(threading.current_thread().name))
        for url in self.urls:
            print('%s ----->>>%s'%(threading.current_thread().name,url))
            time.sleep(random.random())
        print('%s ended '%threading.current_thread().name)


if __name__=='__main__':
    print('%s is running ..'%threading.current_thread().name)
    t1=myThread(name='thread1',urls=['url_1','url_2','url_3'])
    t2=myThread(name='thread2',urls=['url_4','url_5','url_6'])
    t1.start()
    t2.start()
    t1.join()
    t2.join()