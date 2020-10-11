import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor

class myQueue:

    def __init__(self, maxSize=0):
        self.maxSize = maxSize
        self.mutex = threading.Lock()
        self.queue = []
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)
    
    def get(self):
        time.sleep(random.randint(1,2))
        with self.not_empty:
            if len(self.queue):
                msg = self.queue.pop(0)
                print('get the msg', msg)
                self.not_full.notify()
            else:
                print('queue empty, wait')
                self.not_empty.wait()
            return msg
            

    def put(self, msg):
        time.sleep(random.randint(1,2))
        with self.not_full:
            if len(self.queue)>=self.maxSize:
                print('queue full, wait')
                self.not_full.wait()
            self.queue.append(msg)
            print('put the msg', msg)
            self.not_empty.notify()
             

# queue = []
# q = Queue(2, queue)
# exector = ThreadPoolExecutor(5)
# exector.submit(q.get())
# exector.submit(q.put(1))
# exector.submit(q.put(2))
# exector.submit(q.put(3))
# exector.submit(q.get())
# time.sleep(3)


# q.get()
# q.put(1)
# q.put(2)
# q.get()
# q.put(3)
# q.put(4)