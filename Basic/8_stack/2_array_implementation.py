class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.top = -1

    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack is full")
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        print('popped',self.arr[self.top])
        self.top -= 1

stack = Stack(10)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.pop()
stack.pop()


