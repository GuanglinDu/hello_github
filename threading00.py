# https://pymotw.com/2/threading/

import threading

def worker():
    """Thread worker function"""
    print 'Worker'
    return


def worker2(num):
    """Thread worker function"""
    print 'Worker 2: %s' % num
    return

    
if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    threads2 = []
    for i in range(5):
        t = threading.Thread(target=worker2, args=(i,))
        threads2.append(t)
        t.start()

