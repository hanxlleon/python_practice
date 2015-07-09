import threading
import time


class Test(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print '{0} delay for {1}'.format(self.name, self.delay)
        time.sleep(self.delay)
        c = 0

        while True:
            print '{0} times for {1}'.format(c, self.name)
            c += 1
            if c == 3:
                print 'end of {0}'.format(self.name)
                break


if __name__ == '__main__':
    t1 = Test('Thread 1', 2)
    t2 = Test('Thread 2', 2)

    t1.start()
    print 'wait to end'
    t1.join()  # t2必须等待t1结束后才会开始

    t2.start()
    print 'end of main'