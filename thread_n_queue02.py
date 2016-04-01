# http://www.ibm.com/developerworks/aix/library/au-threadingpython/

import Queue
import threading
import urllib2
import time

hosts = ["http://sina.com.cn", "http://baidu.com",
              "http://sohu.com", "http://163.com"]

queue = Queue.Queue()


class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
          
    def run(self):
        while True:
            # Grabs host from queue
            host = self.queue.get()
            
            # Grabs urls of hosts and prints first 1024 bytes of page
            url = urllib2.urlopen(host)
            #print url.read(1024)
            
            # Signals to queue job is done
            self.queue.task_done()

def main():
    # Spawns a pool of threads, and pass them queue instance 
    for i in range(5):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
              
    # Populates queue with data   
    for host in hosts:
        queue.put(host)
           
    # Wait on the queue until everything has been processed     
    queue.join()

if __name__ == '__main__':
    start = time.time()
    main()
    print "Elapsed Time: %s" % (time.time() - start)
