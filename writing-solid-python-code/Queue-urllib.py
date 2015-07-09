#coding:utf-8
import Queue
import os
import threading
import urllib2


class DownloadThread(threading.Thread):
    def __init__(self, queue):
        super(DownloadThread, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            print self.name +' begin download '+url
            self.download_file(url)
            self.queue.task_done()  # 下载完毕发送信号
            print self.name + ' download completed'

    @staticmethod
    def download_file(url):
        urlhandler = urllib2.urlopen(url)
        fname = os.path.basename(url)+'.html'
        with open(fname, 'wb') as f:
            while True:
                chunk = urlhandler.read(1024)
                if not chunk:
                    break
                f.write(chunk)


if __name__ == '__main__':
    urls = ['https://wiki.python.org/moin/WebProgramming',
            'https://www.createspace.com/3611970',
            'https://wiki.python.org/moin/Documentation'
            ]

    queue = Queue.Queue()

    # 创建线程池
    for i in range(5):
        t = DownloadThread(queue)
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)

    queue.join()
