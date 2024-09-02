# optimised approach
class Insertion:
    def __init__(self, data: list) -> list:
        self.nums = data
    def sort(self):
        for i in range(1,len(self.nums)):
            key = self.nums[i]
            j = i - 1
            while(j>=0 and self.nums[j]>key):
                self.nums[j+1] = self.nums[j]
                j = j - 1
            self.nums[j+1] = key 
        return self.nums



sample = [2,10,8,7]
obj = Insertion(sample)
print(obj.sort())
# Time O(N^2)