class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self, val):
        self.queue.append(val)
    
    def pop(self):
        if not self.queue:
            return -1
        return self.queue.pop(0)
    
    def top(self):
        if not self.queue:
            return -1
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def clear(self):
        self.queue = []
    
queue = Queue()
n1 = int(input())
for i in range(n1):
    n2 = int(input())
    for j in range(n2):
        cmd = input().split(' ')
        if len(cmd)>1:
            queue.push(int(cmd[1]))
        elif cmd[0]=='POP':
            print(queue.pop())
        elif cmd[0]=='TOP':
            print(queue.top())
        elif cmd[0]=='SIZE':
            print(queue.size())
        else:
            queue.clear()
            
        
    