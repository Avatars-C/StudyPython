# -*- coding: UTF-8 -*-
#@function:Thread priority queue (Queue)
#@time:2019-3-20

"""
import threading
import time
import queue
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q

    def run(self):
        print("Staring" +self.name)
        #get lock
        process_data(self.name,self.q)
        print("Stoping"+self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s process %s" % (threadName,data))
        else:
            queueLock.release()
        time.sleep(1)


threadlist=["Thread-1","Thread-2","Thread-3"]
nameList=["One","Two","Three","Four","Five","Six"]
queueLock=threading.Lock()
workQueue=queue.Queue(10)
threads=[]
threadID=1
#创建新线程
for tName in threadlist:
    thread=myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

#填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

#通知线程是时候退出
exitFlag=1

#等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")

print("Hello")
"""

'''
for n in range(2, 13):    
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            if x >= n/2:
                break
    else:
                   # loop fell through without finding a factor
        print(n, 'is a prime number')
'''
'''
for num in range(2,10):
    if num % 2==0:
        print("Found an even number",num)
        continue
    print("Found number",num)
'''
"""
def f1(a,l=[]):
    l.append(a)
    return l


def f2(a,l=None):
    if l is None:
        l=[]
    l.append(a)
    return l

print("f1-------------->")
print(f1(1))
print(f1(2))
print(f1(3))
print("f2------------->")
print(f2(1))
print(f2(2))
print(f2(3))
"""

'''
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')
parrot(voltage='5.0', action='dead')
'''
'''
def concat(*args, sep="/"):
    return sep.join(args)
'''
'''
def add(y):
    return lambda y : y + 1


print(add(4))
'''
'''
from collections import deque
def my_function() -> "nobhbjtyfvnhug":
    """Do nothing, but document it.
    #
    # 
    # 
     No, really, it doesn't do anything.
    """
    pass
'''
'''
print(my_function.__doc__)
print(my_function.__annotations__)
def test_queue():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    queue.popleft()
    queue.popleft()
    return queue

print(test_queue())
'''

print("the first")
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print("the sencond")
#等价于
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)