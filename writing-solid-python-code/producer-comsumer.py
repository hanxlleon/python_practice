#coding:utf-8
#Queue, threading.Condition(acquire, release, wait, notify), threading.Lock
#因为Queue已经包含了锁机制，代码里面的条件变量是不需要的
import threading
import Queue
import random


writelock = threading.Lock()

class Producer(threading.Thread):

    def __init__(self, q, con, name):
        super(Producer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print 'Producer ' + self.name + ' started'

    def run(self):
        while True:
            global writelock
            # self.con.acquire()
            if self.q.full():
                with writelock:
                    print 'q is full'
                # self.con.wait()
            else:
                value = random.randint(1, 10)
                with writelock:
                    print self.name + ' put ' + str(value) + ' into queue'
                self.q.put(self.name+":"+str(value))
                # self.con.notify()

            # self.con.release()


class Consumer(threading.Thread):

    def __init__(self, q, con, name):
        super(Consumer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print 'Consumer '+self.name+' started'

    def run(self):
        global writelock
        while True:
            # self.con.acquire()
            if self.q.empty():
                with writelock:
                    print 'queue is empty'
                # self.con.wait()
            else:
                value = self.q.get()
                with writelock:
                    print self.name + ' get value ' + value
                # self.con.notify()
            # self.con.release()


if __name__ == '__main__':
    q = Queue.Queue(10)
    con = threading.Condition()

    p1 = Producer(q, con, 'P1')
    p1.start()
    p2 = Producer(q, con, 'P2')
    p2.start()
    c = Consumer(q, con, 'C')

    c.start()


