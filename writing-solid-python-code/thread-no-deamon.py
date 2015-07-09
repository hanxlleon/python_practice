#coding:utf-8
'''thread 没有守护线程，主线程结束后，不会等待子线程，子线程也会结束'''
from thread import start_new_thread
import time


def myfunc(num, delay):
    print 'calculate square of {1} delay for {0} seconds '.format(delay, num)
    time.sleep(delay)
    print 'calculate begin...'
    result = num ** 2
    print result
    return result


start_new_thread(myfunc, (2, 1))
start_new_thread(myfunc, (3, 2))

time.sleep(1)
