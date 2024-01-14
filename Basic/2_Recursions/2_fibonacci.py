import time

'''
t1=time.time()
class fibonaacci:
    def __init__(self,data) -> None:
        self.num = data
    def get_fibonacci(self):
        if self.num == 0 or self.num == 1:
            return self.num
        return fibonaacci(self.num-1).get_fibonacci() + fibonaacci(self.num-2).get_fibonacci()
    

sample = 40
obj = fibonaacci(sample)
ans = obj.get_fibonacci()

t2=time.time()

print(ans,t2-t1)

# Time O(2^N)
# Space O(2^N)

'''






import time


t1=time.time()
class fibonaacci:
    def __init__(self,data) -> None:
        self.num = data
        self.memo = {}
    def get_fibonacci(self):
        if self.num in self.memo:
            return self.memo[self.num]
        if self.num == 0 or self.num == 1:
            return self.num
        fib_value = fibonaacci(self.num-1).get_fibonacci() + fibonaacci(self.num-2).get_fibonacci()
        self.memo[self.num] = fib_value
        return fib_value
    

sample = 40
obj = fibonaacci(sample)
ans = obj.get_fibonacci()

t2=time.time()

print(ans,t2-t1)
