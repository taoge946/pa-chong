import threading
import random,time

def thread_run(urls):
    print('current  %s is running'%threading.current_thread().name)
    for url in urls:
        print ('%s---->>%s'%(threading.current_thread().name,url))
        time.sleep(random.random())
    print('%s ended '%(threading.current_thread().name))

if __name__=='__main__':
    print('%s is running ..'%threading.current_thread().name)
    t1=threading.Thread(target=thread_run,args=(['url_1','url_2','url_3'],))
    t2=threading.Thread(target=thread_run,args=(['url_4','url_5','url_6'],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()