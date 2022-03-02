from gevent import monkey;monkey.patch_all()
import gevent
import urllib3



def f1():
    for i in range(5):
        print ('run func: f1, index: %s ' % i)
        gevent.sleep(0)


def f2():
    for i in range(5):
        print ('run func: f2, index: %s ' % i)
        gevent.sleep(0)


t1 = gevent.spawn(f1)
t2 = gevent.spawn(f2)
gevent.joinall([t1, t2])

# def run_task(url):
#     print("visit:%s"%url)
# try:
#     response=urllib3.urlopen(url)
#     data=response.read()
#     print('%d bytes received from %s'%(len(data),url))
# except Exception:
#     print('error')




# if __name__=='__main__':
#     urls=['https://www.baidu.com/','https://www.python.org/','https://github.com/']
#     greenlets=[gevent.spawn(run_task,url) for url in urls]
#     gevent.joinall(greenlets)