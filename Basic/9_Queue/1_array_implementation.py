class Queue:
    def __init__(self, capacity):
        self.cap = capacity
        self.size = 0
        self.arr = [None] * self.cap

    def is_full(self):
        return self.size == self.cap

    def is_empty(self):
        return self.size == 0

    def enqueue(self, x):
        if self.is_full():
            return False
        self.arr[self.size] = x
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued = self.arr[0]
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1
        return dequeued

    def get_front(self):
        if self.is_empty():
            return -1
        return self.arr[0]

    def get_rear(self):
        if self.is_empty():
            return -1
        return self.arr[self.size - 1]

    def display(self):
        if self.is_empty():
            return 0
        for i in range(self.size):
            print(self.arr[i], end="\t")
        print()
        return 0



class CircularQueue:
    def __init__(self, cap):
        self.cap = cap 
        self.queue = [None] * cap  
        self.front = 0  
        self.size = 0 

    def isFull(self):
        return self.size == self.cap

    def isEmpty(self):
        return self.size == 0

    def getFront(self):
        if self.isEmpty():
            return -1  
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1  
        return self.queue[(self.front + self.size - 1) % self.cap]
    def enqueue(self, x):
        if self.isFull():
            return  
        rear = (self.front + self.size) % self.cap
        self.queue[rear] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return  
        self.front = (self.front + 1) % self.cap
        self.size -= 1

cq = CircularQueue(3)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
# 10 20 30
print(cq.getFront())  
cq.dequeue()
cq.dequeue()
cq.enqueue(40)
# 30 40
print(cq.getFront())  
print(cq.getRear())   
cq.dequeue()
# 40
print(cq.getFront())  
print('circular over')



q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()
print("Deleted:", q.dequeue())
q.display()
print("Deleted:", q.dequeue())
q.display()
q.enqueue(60)
q.enqueue(70)
q.display()