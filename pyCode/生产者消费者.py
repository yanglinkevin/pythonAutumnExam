import threading
from queue import Queue 
import time
import random
from concurrent.futures import ThreadPoolExecutor
from 阻塞队列 import myQueue
class Producer(threading.Thread):

    def __init__(self, q, msg):
        super().__init__()
        self.q = q
        self.msg = msg
        self.flag = True

    def produce(self):
        time.sleep(random.randint(1,2))
        self.q.put(self.msg)
        print('here is the produce msg', self.msg)

    def run(self):
        while self.flag:
            try:
                self.produce()
            except:
                print('producer error')
        print('producer stop')

    def stop(self):
        self.flag = False
            

class Consumer(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q
        self.flag = True
    def consume(self):
        time.sleep(random.randint(1,2))
        msg = self.q.get()
        print('here is the consumer msg', msg)
    def run(self):
        while self.flag:
            try:
                self.consume()
            except:
                print('error found')
        print('consumer stop')
    def stop(self):
        self.flag = False

if __name__ == "__main__":
    q = myQueue(5)
    executor = ThreadPoolExecutor()
    producer1 = Producer(q, 'msg1')
    producer2 = Producer(q, 'msg2')
    consumer1 = Consumer(q)
    consumer2 = Consumer(q)
    # executor.submit(producer1.produce())
    # executor.submit(producer2)
    # executor.submit(consumer1)
    # executor.submit(consumer2)
    producer1.start()
    producer2.start()
    consumer1.start()
    consumer2.start()

    time.sleep(10)
    producer1.stop()
    producer2.stop()
    consumer1.stop()
    consumer2.stop()






    
