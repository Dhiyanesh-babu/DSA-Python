# Node class to represent each element in the queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class to handle enqueue and dequeue operations
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Method to add an element to the queue
    def enqueue(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

        

    # Method to remove an element from the queue
    def dequeue(self):
        if self.front == None:
            return None
        temp = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp
        

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Dequeued:", q.dequeue())  # Output: 10
print("Dequeued:", q.dequeue())  # Output: 20
print("Dequeued:", q.dequeue())  # Output: 30






















