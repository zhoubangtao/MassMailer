#coding:utf-8

#Python的线程池实现

import Queue
import threading
import sys
import time
import urllib

#替我们工作的线程池中的线程
class MyThread(threading.Thread):
 def __init__(self, workQueue, resultQueue,timeout=30, **kwargs):
  threading.Thread.__init__(self, kwargs=kwargs)
  #线程在结束前等待任务队列多长时间
  self.timeout = timeout
  self.setDaemon(True)
  self.workQueue = workQueue
  self.resultQueue = resultQueue
  self.start()

 def run(self):
  while True:
   try:
    #从工作队列中获取一个任务
    callable, args, kwargs = self.workQueue.get(timeout=self.timeout)
    #我们要执行的任务
    res = callable(args, kwargs)
    #报任务返回的结果放在结果队列中
    self.resultQueue.put(res+" | "+self.getName())
   except Queue.Empty: #任务队列空的时候结束此线程
    break
   except :
    print sys.exc_info()
    raise

class ThreadPool:
 def __init__( self, num_of_threads=10):
  self.workQueue = Queue.Queue()
  self.resultQueue = Queue.Queue()
  self.threads = []
  self.__createThreadPool( num_of_threads )

 def __createThreadPool( self, num_of_threads ):
  for i in range( num_of_threads ):
   thread = MyThread( self.workQueue, self.resultQueue )
   self.threads.append(thread)

 def wait_for_complete(self):
  #等待所有线程完成。
  while len(self.threads):
   thread = self.threads.pop()
   #等待线程结束
   if thread.isAlive():#判断线程是否还存活来决定是否调用join
    thread.join()

 def add_job( self, callable, *args, **kwargs ):
  self.workQueue.put( (callable,args,kwargs) )

def test_job(id, sleep = 0.001 ):
 html = ""
 try:
  time.sleep(1)
  conn = urllib.urlopen('http://www.google.com/')
  html = conn.read(20)
 except:
  print  sys.exc_info()
 return  html

def test():
 print 'start testing'
 tp = ThreadPool(10)
 for i in range(50):
  time.sleep(0.2)
  tp.add_job( test_job, i, i*0.001 )
 tp.wait_for_complete()
 #处理结果
 print 'result Queue\'s length == %d '% tp.resultQueue.qsize()
 while tp.resultQueue.qsize():
  print tp.resultQueue.get()
 print 'end testing'
if __name__ == '__main__':
 test()
