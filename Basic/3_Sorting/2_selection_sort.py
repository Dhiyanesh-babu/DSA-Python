# optimised approach
class Selection:
    def __init__(self, data: list) -> list:
        self.nums = data
    def sort(self):
        for i in range(len(self.nums)):
            min_ind = i
            for j in range(i+1,len(self.nums)):
                if self.nums[j] < self.nums[min_ind]:
                    min_ind = j
            self.nums[i], self.nums[min_ind] = self.nums[min_ind], self.nums[i]
        return self.nums



sample = [2,10,8,7]
obj = Selection(sample)
print(obj.sort())
# Time O(N^2)
