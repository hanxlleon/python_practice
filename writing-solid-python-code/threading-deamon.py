#coding:utf-8
'''threading设置守护线程'''
import threading
import time


def myfunc(num, delay):
    print 'calculate square of {1} delay for {0} seconds '.format(delay, num)
    time.sleep(delay)
    print 'calculate begin...'
    result = num ** 2
    print result
    return result


t1 = threading.Thread(target=myfunc, args=(2, 3))  # 设置t1为守护线程，主线程退出不会等待守护线程
t2 = threading.Thread(target=myfunc, args=(3, 2))  # 设置t2为非守护线程，主线程需要等待t2结束后才能退出

print t1.isDaemon()
print t2.isDaemon()

t1.setDaemon(True)

t1.start()
t2.start()

time.sleep(1)
