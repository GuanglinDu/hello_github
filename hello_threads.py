# http://www.ibm.com/developerworks/aix/library/au-threadingpython/

import threading
import datetime
        
class ThreadClass(threading.Thread):
    
    def run(self):
        now = datetime.datetime.now()
        print "%s says Hello World at time: %s" % (self.getName(), now)

if __name__ == '__main__':
    for i in range(2):
        t = ThreadClass()
        t.start()

