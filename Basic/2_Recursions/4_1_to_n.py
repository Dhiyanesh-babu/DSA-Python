
import time
import sys
sys.setrecursionlimit(15000)

t1=time.time()
class n_to_1:
    def __init__(self, data) -> None:
        self.num = data

    def show(self):
        if self.num == 0:
            return 0
        n_to_1(self.num - 1).show()
        print(self.num)


sample = 3000
obj = n_to_1(sample)
obj.show()
t2=time.time()

t = t2 - t1
#print(t)



t1=time.time()

class n_to_11:
    k = None
    def __init__(self, data):
        self.num = data
        if n_to_11.k is None:
            n_to_11.k = data
    def show(self):
        if (self.num == 0):
            return 0
        print(n_to_11.k + 1 - self.num)
        n_to_11(self.num - 1).show()

sample = 3000
obj = n_to_11(sample)
obj.show()

tt = t2 - t1
print(t)
print(tt)

# second solution is tail recursive
# time efficient

