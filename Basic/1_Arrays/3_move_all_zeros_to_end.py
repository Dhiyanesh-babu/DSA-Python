# Naive approach

class MoveZeros:
    def __init__(self,data) -> None:
        self.data = data
    def move_zeros(self):
        self.zero_pos=0
        self.ans = []
        for number in self.data:
            if number != 0:
                self.ans.append(number)
            else:
                self.zero_pos = self.zero_pos+1
        for i in range(self.zero_pos):
            self.ans.append(0)
        return self.ans



sample = [8,5,0,10,0,20]
obj = MoveZeros(sample)
result =obj.move_zeros()
print(result)

# Time - O(N)
# Space - O(N)













# Efficient approach

class MoveZeros:
    def __init__(self,data) -> None:
        self.data = data
    def move_zeros(self):
        low = 0
        high = len(self.data)-1
        while low<=high:
            while self.data[low] != 0:
                low+=1
            while self.data[high] == 0:
                high-=1
            if low <= high: # important
                self.data[low] , self.data[high] = self.data[high], self.data[low]
        return self.data


sample = [8,5,0,10,0,20]
obj = MoveZeros(sample)
result =obj.move_zeros()
print(result)

# Time - O(N)
# Space - O(1)














class MoveZeros:
    def __init__(self,data) -> None:
        self.data = data
    def move_zeros(self):
        self.pos=0
        for i in range(len(self.data)):
            if self.data[i] !=0:
                self.data[i], self.data[self.pos] = self.data[self.pos], self.data[i]
                self.pos+=1
        return self.data


sample = [8,5,0,10,0,20]
obj = MoveZeros(sample)
result =obj.move_zeros()
print(result)

# Time - O(N)
# Space - O(1)







