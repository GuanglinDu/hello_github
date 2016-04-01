# http://www.ibm.com/developerworks/aix/library/au-threadingpython/

import urllib2
import time

#hosts = ["http://yahoo.com", "http://amazon.com",
#              "http://ibm.com", "http://apple.com"]
hosts = ["http://sina.com.cn", "http://baidu.com",
              "http://sohu.com", "http://163.com"]

def no_thread_version():
    start = time.time()
    # Grabs urls of hosts and prints first 1024 bytes of page
    for host in hosts:
        url = urllib2.urlopen(host)
        #print url.read(1024)        
    print "Elapsed Time: %s" % (time.time() - start)


if __name__ == '__main__':
    no_thread_version()

