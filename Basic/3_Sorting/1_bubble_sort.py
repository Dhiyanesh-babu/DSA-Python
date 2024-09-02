# Naive
class Bubble:
    def __init__(self, data: list) -> list:
        self.nums = data
    def sort(self):
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-1):
                if self.nums[j] > self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
        return self.nums

sample = [2,10,8,7]
obj = Bubble(sample)
print(obj.sort())
## Time O(N^2)




# optimised for sorted array
class Bubble:
    def __init__(self, data: list) -> list:
        self.nums = data
    def sort(self):
        for i in range(len(self.nums)-1):
            print('hi')
            checked = False
            for j in range(len(self.nums)-1):
                if self.nums[j] > self.nums[j+1]:
                    checked = True
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
            if checked == False:
                break
        return self.nums
sample = [1,2,3,4,5]
obj = Bubble(sample)
print(obj.sort())
## Time O(N^2)


    


